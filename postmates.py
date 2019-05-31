import json

"""
  monday: 10am -> 4pm
  tuesday: 10am -> 4pm
  wednesday: 11am -> 8pm
  thursday: 11am -> 8pm
  friday: 11am -> 2am
  saturday: 5pm -> 4am
"""
# day of week: 1 -> Monday, 2 -> Tuesday, ..., 7 -> Sunday
# time store as minutes since midnight
input_json = '''{
  "hours": [
    {
      "days": [1,2],
      "hours": {"start_min": 600, "end_min": 960}
    },
    {
      "days": [3,4],
      "hours": {"start_min": 660, "end_min": 1200}
    },
    {
      "days": [5],
      "hours": {"start_min": 660, "end_min": 120}
    },
    {
      "days": [6],
      "hours": {"start_min": 1020, "end_min": 240}
    }
  ]
}'''


# {u'hours': {u'start_min': 600, u'end_min': 960}, u'days': [1, 2]}
def is_store_open(example, dt):
    day = _day_of_week(dt)
    time = _minutes_since_midnight(dt)
    # print time
    dictionary = json.loads(example)
    for entry in dictionary['hours']:
        for day_open in entry['days']:
            if day == day_open and time >= entry['hours']['start_min']:
                new_end_min = entry['hours']['end_min']
                if entry['hours']['end_min'] < entry['hours']['start_min']:
                    new_end_min += (24 * 60)
                if time <= new_end_min:
                    return True
            if entry['hours']['end_min'] < entry['hours']['start_min'] and day == day_open + 1 and time <= \
                    entry['hours']['end_min']:
                return True
    return False

    return False  # or True


# Helper functions
import datetime


def _minutes_since_midnight(dt):
    midnight = datetime.datetime.combine(dt.date(), datetime.time())
    return (dt - midnight).seconds / 60


def _day_of_week(dt):
    return dt.isoweekday()


print(is_store_open(input_json, datetime.datetime.utcnow().replace(day=25, hour=17, minute=0)))