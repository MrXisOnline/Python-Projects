class Cars:
    def __init__(self, speed, color):
        print(speed, color, sep="\n")
        self.__speed = speed
        self.__color = color

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        print(self.__speed)

    def set_color(self, value):
        self.__color = value

    def get_color(self):
        print(self.__color)

    pass


class SuperCars(Cars):
    pass


My_car = Cars("130mph", "Blue")
My_car.get_speed()
My_car.set_speed("140mph")
My_car.get_speed()
Sup_Car = SuperCars("350mph", "Magenta Blue")
