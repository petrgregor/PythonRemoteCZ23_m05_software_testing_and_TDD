class BasicCalculator:

    def add(self, num1, num2):
        if ((isinstance(num1, int) or
             isinstance(num1, float)) and
                (isinstance(num2, int) or
                 isinstance(num2, float))):
            return num1 + num2
        return None

    def subtract(self, num1, num2):
        if ((isinstance(num1, int) or
             isinstance(num1, float)) and
                (isinstance(num2, int) or
                 isinstance(num2, float))):
            return num1 - num2
        return None

    def multiply(self, num1, num2):
        if ((isinstance(num1, int) or
             isinstance(num1, float)) and
                (isinstance(num2, int) or
                 isinstance(num2, float))):
            return num1 * num2
        return None

    def divide(self, num1, num2):
        if ((isinstance(num1, int) or
             isinstance(num1, float)) and
                (isinstance(num2, int) or
                 isinstance(num2, float))):
            try:
                return num1 / num2
            except:
                return None
        return None
