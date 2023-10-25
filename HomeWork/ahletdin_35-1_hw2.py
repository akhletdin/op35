class Fiqure:
    unit = "sm"

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Fiqure):
    p = 3.1415

    def __init__(self, radius):
        super(Circle, self).__init__()
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def colculate_area(self):
        return round(self.p * (self.__radius ** 2), 2)

    def info(self):
        return f"radius : {self.__radius}{self.unit}, area : {self.colculate_area()}{self.unit}"


class RightTriangle(Fiqure):
    def __init__(self, side_a, side_b):
        super(RightTriangle, self).__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    @property
    def side_a(self):
        return self.__side_a

    @side_a.setter
    def side_a(self, value):
        self.__side_a = value

    @property
    def side_b(self):
        return self.__side_b

    @side_b.setter
    def side_b(self, value):
        self.__side_b = value

    def colculate_area(self):
        return round(1 / 2 * (self.__side_a * self.__side_b), 2)

    def info(self):
        return f"side_a : {self.__side_a}{self.unit}, side_b : {self.__side_b}{self.unit}, area:" \
               f" {self.colculate_area()}{self.unit}"

def creat_figurs():
    circle = Circle(4)
    circle2 = Circle(6)

    triangle1 = RightTriangle(15, 16)
    triangle2 = RightTriangle(10, 7)
    triangle3 = RightTriangle(8, 6)
    figurs = [circle, circle2, triangle1, triangle2, triangle3]
    return figurs


figures = creat_figurs()

for figure in figures:
    print(figure.info())