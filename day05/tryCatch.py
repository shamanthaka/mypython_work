'''
Exception handling in python
'''

try:
    #value = 10 / 0
    number = int(input("Enter a number: "))
    value = 10/number
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
