
#exception handling in python

try:
    number = int(input("enter a number:"))
    value = 10/number
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)