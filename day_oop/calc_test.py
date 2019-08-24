from day_oop.Calculator import Calculator

if __name__  == '__main__':

    cal = Calculator(5, 6)
    result = cal.add()
    print(result)

    result = cal.multiplication()
    print(result)

    result = Calculator.division(45,9)
    print(result)

    result = Calculator.my_mod(45, 8)
    print(result)



