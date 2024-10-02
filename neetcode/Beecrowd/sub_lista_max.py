"""
This module calculates the maximum subarray sum.
"""

lista = [10, 5, -17, 20, 50, -1, 3, -30, 10]

max_total = lista[0]
max_terminando_agora = lista[0]

for atual in lista[1:]:
    max_terminando_agora = max(atual, max_terminando_agora + atual)
    max_total = max(max_total, max_terminando_agora)

print(max_total)
