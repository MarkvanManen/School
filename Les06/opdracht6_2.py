lijst = eval(input('Geef een lijst met minimaal 10 strings: '))
nieuwelijst = []

for product in lijst:
    if len(product) == 4:
        nieuwelijst.append(product)

print('De nieuw-gemaakte lijst met alle vier-letter strings is: ' + str(nieuwelijst))

