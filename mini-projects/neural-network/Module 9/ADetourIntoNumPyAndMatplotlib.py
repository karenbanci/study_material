import matplotlib.pyplot as plt
import numpy as np
from collections import OrderedDict


# tuples are (species, age, weight in pounds)
pet_list = [
    ("Cat", 5, 12),
    ("Rabbit", 1, 1.5),
    ("Dog", 1, 30),
    ("Cat", 7, 5),
    ("Rabbit", 2, 2.5),
    ("Dog", 5, 25),
    ("Bird", 23, .5),
    ("Rabbit", 1, 1.7),
    ("Dog", 2, 12),
    ("Cat", 3, 7),
    ("Rabbit", 4, 2.3),
    ("Dog", 12, 47),
    ("Cat", 12, 10),
    ("Bird", 13, .1),
    ("Dog", 7, 31),
    ("Cat", 11, 9),
    ("Rabbit", 2, 2.5),
    ("Cat", 1, 8),
    ("Bird", 11, .2),
    ("Cat", 2, 5),
    ("Bird", 3, .6),
    ("Rabbit", 2, 4.9),
    ("Cat", 7, 7),
    ("Bird", 7, .3),
    ("Rabbit", 1, 1.5)
]

""""
pet_dict.get(item[0]) nos diria quantos animais de estimação do tipo item[0]
temos em mãos - talvez item[0] sejam coelhos. Mas e se ainda não carregamos
nenhum coelho? O segundo argumento para dict ou OrderedDict é a resposta 
padrão. Se a chave que estamos solicitando não existir, o dict retornará esse
valor em vez de lançar um erro. Neste caso, queremos retornar zero - indicando
que ainda não registramos nenhum coelho. Assim, pet_dict.get(item[0], 0)
retorna quantos de um determinado animal de estimação já registramos e +1
adiciona mais um a esse número. O resultado é armazenado de volta no dicionário
 e a chave é criada se ainda não existir. Quando esse loop é concluído, temos
 um dicionário que resume quantos de cada tipo de animal de estimação temos.
 Você pode imprimir (pet_dict) para ver o resultado.
"""
for item in pet_list:
    pet_dict[item[0]] = pet_dict.get(item[0], 0) +1

labels = pet_dict.keys()
sizes = pet_dict.values()

pie_chart = plt.figure(0)
colors = ['orange', 'yellow', 'green', 'lightskyblue']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.show()

"""
pie_chart = plt.figure(0) pie_chart.show() Não é obrigatório.
Podemos usar plt como o objeto que manterá nosso gráfico atual.
No entanto, criaremos dois gráficos (um gráfico de pizza e um histograma)
e queremos salvar os dois. Chamar plt.figure(0) cria um novo objeto de
plotagem que podemos criar e retornar.
"""

# histograma
hist = plt.figure(1)
ages = [item[1] for item in pet_list]
bins = np.arange(0.5, 100.5, 5)
plt.hist(ages, bins=bins, )
plt.xticks(bins)
plt.xlim([min(ages) - 1, max(ages) + 5])
hist.show()