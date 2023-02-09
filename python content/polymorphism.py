class Shark():
    def swim(self):
        print("The shark is swimming.")

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")


class Clownfish():
    def swim(self):
        print("The clownfish is swimming.")

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")

"""
No código acima, ambas as classes Sharke Clownfishpossuem três métodos com o mesmo nome em comum.
No entanto, cada uma das funcionalidades desses métodos difere para cada classe.
"""

#Vamos instanciar essas classes em dois objetos:

sammy = Shark()
sammy.skeleton()
# The shark's skeleton is made of cartilage.

casey = Clownfish()
casey.skeleton()
# The clownfish's skeleton is made of bone.

"""
Para mostrar como o Python pode usar cada um desses diferentes tipos de classe da mesma maneira, podemos primeiro criar um for loop que itera por meio de uma tupla de objetos. Então podemos chamar os métodos sem nos preocuparmos com o tipo de classe de cada objeto. Vamos assumir apenas que esses métodos realmente existem em cada classe.
"""

sammy = Shark()

casey = Clownfish()

for fish in (sammy, casey):
    fish.swim()
    fish.swim_backwards()
    fish.skeleton()

"""
The shark is swimming.
The shark cannot swim backwards, but can sink backwards.
The shark's skeleton is made of cartilage.
The clownfish is swimming.
The clownfish can swim backwards.
The clownfish's skeleton is made of bone.
"""

def in_the_pacific(fish):
    fish.swim()

in_the_pacific(sammy)
# The shark is swimming.

in_the_pacific(casey)
# The clownfish is swimming.

"""
Ao permitir que objetos diferentes aproveitem funções e métodos de maneiras semelhantes por meio do polimorfismo, o uso desse recurso do Python fornece maior flexibilidade e capacidade de extensão do seu código orientado a objeto.
"""
