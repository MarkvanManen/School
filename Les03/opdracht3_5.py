getallenrij = [2, 4, 6, 8, 10, 9, 7]
deelbaar = []

for getal in getallenrij:
    if getal % 2 == 0:
        deelbaar.append(getal)

print(deelbaar)