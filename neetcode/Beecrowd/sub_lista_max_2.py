"""
This module calculates the maximum subarray sum.
"""

# lista = [10, 5, -17, 20, 50, -1, 3, -30, 10]
cotacoes = [10, 80, 20, 40, 30, 50, 40, 60, 50, 70, 60, 10, 200]
lista = [cotacoes[i] - cotacoes[i-1] for i in range(1, len(cotacoes))]
print("lista", lista)

max_total = lista[0]
max_terminando_agora = lista[0]

inicio = 0
fim = 0

for i, atual in enumerate(lista[1:]):
    if atual >= max_terminando_agora + atual:
        max_terminando_agora = atual
        inicio = i +1
    else:
        max_terminando_agora += atual

    if max_terminando_agora > max_total:
        max_total = max_terminando_agora

        fim = i+1

print("soma máxima:", max_total)
print("inicio", inicio)
print("fim", fim)
