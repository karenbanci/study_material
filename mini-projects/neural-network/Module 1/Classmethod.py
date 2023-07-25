class Dog:

    number_of_dogs = 0

    def __init__(self, name: str):
        self._name = name
        Dog.number_of_dogs += 1

    @classmethod
    def how_many_dogs(cls):
        return cls.number_of_dogs

    @property
    def name(self):
        return self._name

    def talk(self):
        print(f"{self._name} says 'woof!'")

dog_one = Dog("Nala")
print(dog_one.name)
print(f"There are {Dog.number_of_dogs} dogs")
dog_two = Dog("Theo")
print(dog_two.name)
print(f"There are {Dog.number_of_dogs} dogs")