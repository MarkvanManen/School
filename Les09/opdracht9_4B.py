import csv

with open('artikel.csv', 'r') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter = ';')
    duurste_artikel = 0
    for row in reader:
        prijs = float(row['Prijs'])
        if prijs > duurste_artikel:
            duurste_artikel = prijs
            duurste_naam = row['Naam']

print('Het duurste artikel is ' + str(duurste_naam) + ' en die kost ' + str(duurste_artikel))
