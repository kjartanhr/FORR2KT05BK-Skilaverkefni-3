class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, v):
        self.result += v
        return self.result
    def subtract(self, v):
        self.result -= v
        return self.result
    def multiply(self, v):
        self.result *= v
        return self.result
    def divide(self, v):
        self.result /= v
        return self.result
    def modulus(self, v):
        self.result %= v
        return self.result
    def power(self, v):
        self.result **= v
        return self.result
    # and er frátekið orð í python, nota _g as in "gate"
    def and_g(self, a, b):
        return True if a == True and b == True else False
    def or_g(self, a, b):
        return True if a == True or b == True else False
    def not_g(self, a):
        return True if a == False else False

def main():
    result = Calculator()
    print(result.add(8))
    print(result.subtract(1))
    print(result.multiply(2))
    print(result.divide(2))
    print(result.power(4))
    print(result.modulus(2))

    gate = Calculator()
    print(gate.and_g(True, False))
    print(gate.and_g(True, True))
    print(gate.or_g(True, False))
    print(gate.or_g(False, False))
    print(gate.not_g(True))
    print(gate.not_g(False))

if __name__ == '__main__':
    main()