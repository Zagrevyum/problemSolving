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
    today = _day_of_week(dt)
    current_time = _minutes_since_midnight(dt)
    # print time
    rest_schedule = json.loads(example)['hours']
    for daily_schedule in rest_schedule:
        for day_open in daily_schedule['days']:
            open_time = daily_schedule['hours']['start_min']
            close_time = daily_schedule['hours']['end_min']
            if open_time > close_time and today == day_open + 1 and current_time <= close_time:
                return True
            if today == day_open and current_time >= open_time and (open_time > close_time or current_time <= close_time):
                return True
    return False


# Helper functions
import datetime


def _minutes_since_midnight(dt):
    midnight = datetime.datetime.combine(dt.date(), datetime.time())
    return (dt - midnight).seconds / 60


def _day_of_week(dt):
    return dt.isoweekday()

#saturday case True
print(is_store_open(input_json, datetime.datetime.utcnow().replace(day=25, hour=17, minute=0)))
#sunday case True
print(is_store_open(input_json, datetime.datetime.utcnow().replace(day=26, hour=2, minute=0)))
#sunday case False
print(is_store_open(input_json, datetime.datetime.utcnow().replace(day=26, hour=12, minute=0)))
