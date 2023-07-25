class Car:
    def __init__(self, make: str):
        self._make = make

    def what_kind_of_car(self):
        print(f"I am a {self._make}")


class Cat:
    def __init__(self, breed: str):
        self._breed = breed

    def what_kind_of_cat(self):
        print(f"I am a {self._breed} cat")


class GrayColor:
    def __init__(self, shade: str):
        self._shade = shade

    def report_color(self):
        print(f"I am a {self._shade} gray")


class GreyCar(Car, GrayColor):
    def __init__(self, make: str, shade: str):s
        Car.__init__(self, make)
        GrayColor.__init__(self, shade)


class GreyCat(Cat, GrayColor):
    def __init__(self, breed: str, shade: str):
        Cat.__init__(self, breed)
        GrayColor.__init__(self, shade)


honda = GreyCar("honda fit", "dark")
honda.what_kind_of_car()
honda.report_color()

print("\n")
pompy = GreyCat("ciames", "light")
pompy.what_kind_of_cat()
pompy.report_color()