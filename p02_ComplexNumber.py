
"""class ComplexNumber:
    __re = None
    __img = None

    def __init__(self, real_part, img_part):
        self.re = real_part
        self.img = img_part

    @property
    def re(self):
        return self.__re

    @re.setter
    def re(self, real_part):
        # TODO: lze vkládat pouze čísla
        self.__re = real_part

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img_part):
        # TODO: lze vkládat pouze čísla
        self.__img = img_part

    def __eq__(self, other):
        return self.re == other.re and self.img == other.img

    def __repr__(self):
        return f"ComplexNumber(re={self.re}, img={self.img})"

    def __str__(self):
        return f"{self.re} + {self.img}i"  # FIXME

    def add(self, other):
        return ComplexNumber(self.re + other.re, self.img + other.img)
"""


class ComplexNumber:
    __re = 0
    __img = 0

    def __init__(self, real_part=0.0, img_part=0.0):
        self.re = real_part
        self.img = img_part

    def __eq__(self, other):
        return self.re == other.re and self.img == other.img

    def __lt__(self, other):
        return self.absolute_value() < other.absolute_value()

    def __gt__(self, other):
        return self.absolute_value() > other.absolute_value()

    def __repr__(self):
        return f"ComplexNumber(re={self.re}, img={self.img})"

    def __str__(self):
        if self.re == 0 and self.img == -1:
            return f"-i"
        if self.re == 0 and self.img != 0:
            return f"{self.img}i"
        if self.img == -1:
            return f"{self.re} - i"
        if self.img < 0:
            return f"{self.re} - {-self.img}i"
        if self.img == 0:
            return f"{self.re}"
        return f"{self.re} + {self.img}i"

    @property
    def re(self):
        return self.__re

    @re.setter
    def re(self, real_part):
        if isinstance(real_part, int) or isinstance(real_part, float):
            self.__re = real_part
        else:
            raise Exception

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img_part):
        if isinstance(img_part, int) or isinstance(img_part, float):
            self.__img = img_part
        else:
            raise Exception

    def add(self, other):
        return ComplexNumber(self.re + other.re, self.img + other.img)

    def subtract(self, other):
        return ComplexNumber(self.re - other.re, self.img - other.img)

    def multiply(self, other):
        a = self.re
        b = self.img
        c = other.re
        d = other.img
        return ComplexNumber(a * c - b * d, a * d + b * c)

    def divide(self, other):
        a = self.re
        b = self.img
        c = other.re
        d = other.img
        if c != 0 or d != 0:
            return ComplexNumber((a * c + b * d) / (c ** 2 + d ** 2), (b * c - a * d) / (c ** 2 + d ** 2))
        else:
            return None

    def conjugate(self):
        return ComplexNumber(self.re, -self.img)

    def absolute_value(self):
        a = self.re
        b = self.img
        return (a ** 2 + b ** 2) ** (1 / 2)
