def is_armstrong_number(number):
    noOfDigit = len(str(number))
    ArmstrongNumber = 0
    for i in str(number):
        ArmstrongNumber += int(i)**noOfDigit
    if ArmstrongNumber == number:
        return True
    else:
        return False
