
class ComplexNumber:
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
