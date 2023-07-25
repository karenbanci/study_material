import random

random.seed(1)
for n in range(3):
    print(f"número {random.random()}")

print("test 2 ------")
base_list = [i for i in range(0, 21)]
print(f"lista: {base_list}")

# aqui vou escolher 3 numeros dentro da base list
for n in range(3):
    print(random.choice(base_list))

my_choice_list = random.choices(base_list, k=10)
print(my_choice_list)