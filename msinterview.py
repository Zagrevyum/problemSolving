# code is in python3

def reformat(phoneNumbers: list) -> list:
    for index in range(len(phoneNumbers)):
        normalizedNumber = normalizenumber(phoneNumbers[index])
        phoneNumbers[index] = normalizedNumber
    return phoneNumbers


def normalizenumber(number: str) -> str:

    if number[3] == "-":
        normalizednumber = number.split("-")
        #print(normalizednumber)
        normalizednumber = normalizednumber[1] + "-" + normalizednumber[0] + "-" + normalizednumber[2]
        return normalizednumber
    return number[3:6]+"-"+number[0:3]+"-"+ number[6:]

numberlist = ["9998887777", "999-888-7777"]
print(reformat(numberlist))
assert reformat(numberlist) == ['888-999-7777', '888-999-7777']
