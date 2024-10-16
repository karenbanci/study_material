n, taxa = map(int, input().split())
cotacoes = list(map(int, input().split()))
variacoes = [cotacoes[i] - cotacoes[i - 1] for i in range(1, len(cotacoes))]

if n == 1:
    print(0)
    exit()

max_total = variacoes[0]
max_terminando_agora = variacoes[0]

resultado = 0

for i, atual in enumerate(variacoes[1:]):
    # print("i---------------", i)
    # print("max_terminando_agora:", max_terminando_agora)
    # print("max_total:", max_total)
    # print("resultado:", resultado, "\n")

    max_terminando_agora = max(atual, max_terminando_agora + atual)
    max_total = max(max_total, max_terminando_agora)

    if max_terminando_agora < max_total - taxa:
        if max_total - taxa > 0:
            resultado += max_total - taxa
        max_terminando_agora = 0
        max_total = 0

if max_total > taxa:
    resultado += max_total - taxa

print(resultado)
