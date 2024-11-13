class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b): #Switch a and b
        return a - b

    def multiply(self, a, b):#add multiply in negative number and remove 1 from range(b)
        result = 0
        negative = False
        if  b < 0:
            negative = True
            b = -b
        
        for i in range(b):
            result = self.add(result, a)
        if negative:
            result = -result
        return result

    def divide(self, a, b):# change from a>b to a>=b, add division between negative number, divided 0 is undefined
        result = 0
        if b == 0:
            return print("Error")
        negative = False
        if b < 0:
            negative = True
            b = -b

        if  a < 0:
            negative = True
            a = -a

        while a >= b:
            a = self.subtract(a, b)
            result += 1

        if negative:
            result = result
        return result
    
    def modulo(self, a, b):# add modulus of negative number, modulus of 0 is undefined
        if b == 0:
            return print("Error")
        
        abs_a = a
        if abs_a < 0:
            abs_a = -abs_a
        abs_b = b
        if abs_b < 0:
            abs_b = -abs_b

        result = abs_a
        while result >= abs_b:
            result = result - abs_b

        if a < 0 and b < 0:
            return -result

        if a < 0 and b > 0:
            if result != 0:
                return b - result
            return 0
        
        if a > 0 and b < 0:
            if result != 0:
                return b + result
            return 0
        
        return result

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))