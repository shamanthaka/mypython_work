class Calculator:

    def __init__(self):
        pass

    def __init__(self, a, b, c=0):
        self.value1 = a
        self.value2 = b
        self.value3 = c

    def add(self):
        return self.value1 + self.value2

    def multiplication(self):
        return self.value1 * self.value2


    def division(a,b):
        return a/b

    @classmethod
    def my_mod(cls, a,b):
        cls(a,b)
        #return a%b
        return a % b






