class Animal:
    def __init__(self, name):
        self._name = name

    def make_a_noise(self):
        print(f"{self._name} says... 'Really? I am a quiet animal'")


class JackRabbit(Animal):
    def __init__(self, name):
        super().__init__(name)


class Antelope(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_a_noise(self):
        print(f"{self._name} says... 'BLEEEEAT'")


class Jackalope(JackRabbit, Antelope):
    def __init__(self, name):
        Animal.__init__(self, name)


fierce_creature = Jackalope("Fierce Creature")
fierce_creature.make_a_noise()