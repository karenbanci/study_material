# Read the file entrada.txt
with open("escada_perfeita.txt", "r", encoding="utf8") as file:
    lines = [line.strip() for line in file.readlines()]
    print('teste', lines )
