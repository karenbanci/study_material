# Read the file entrada.txt
# with open("escada_perfeita.txt", "r", encoding="utf8") as file:
#     lines = [line.strip() for line in file.readlines()]
#     print('teste', lines )

# qtd_blocos = lines[0]
# print("quantidade de bloco primeiro exemplo", qtd_blocos)

QTD_COLUNA = int(input())
qtd_blocos_por_coluna = list(map(int, input().split()))

QTD_TOTAL_BLOCOS = 0

#1 saber a quantidade total que tem de blocos
QTD_TOTAL_BLOCOS = sum(qtd_blocos_por_coluna)

#2 descobrir a escada perfeita
QTD_MINIMA = sun(range(QTD_COLUNA +1))

#3 base da escada
qtd_sobra = (QTD_TOTAL_BLOCOS - QTD_MINIMA)
qtd_base = qtd_sobra // QTD_COLUNA

if qtd_sobra % QTD_COLUNA != 0:
    print(-1)
    exit()

# para cada coluna j
BLOCOS_MOVIDOS = 0
for j in range(QTD_COLUNA):
    qtd_necessaria_coluna_j = j+1 + qtd_base

    if(qtd_blocos_por_coluna[j] > qtd_necessaria_coluna_j):
        BLOCOS_MOVIDOS += qtd_blocos_por_coluna[j] - qtd_necessaria_coluna_j

print(BLOCOS_MOVIDOS)

"""
dada uma coluna qualquer

1) sobra blocos
entrada[j] = 12
perfeita[j] = 9
mover = entrada[j] - perfeita[j]


2) quantidade exata de blocos
entrada[j] = 12
perfeita[j] = 12
mover?

3) faltam blocos
entrada[j] = 8
perfeita[j] = 12
mover??

se sobra de blocos > que zero, precisa mover
se sobra de blocos = a zero, nao precisa mover
se sobra de blocos < que zero, faltam blocos

a última coluna tem que ter pelo menos a quantidade do numero da coluna, se é coluna n0 5, tem que ter pelo menos 5 blocos, a penúltima coluna tem que ter pelo menos 4 blocos e assim por diante

"""
