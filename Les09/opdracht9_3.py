import csv

hoogstescore = 0

with open('gamers.csv', 'r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter = ';')
    for row in reader:
        score = int(row[2])
        if score > hoogstescore:
            hoogstescore = score
            hoogste_naam = row[0]
            hoogste_datum = row[1]

print('De hoogste score is: ' + str(hoogstescore) +  ' op ' + str(hoogste_datum) + ' behaald door ' + str(hoogste_naam))