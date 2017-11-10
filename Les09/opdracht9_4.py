import csv

with open('artikel,csv', 'w', newline = '') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter = ';')
    writer.writerow(('artikelnummer', 'artikelcode', 'naam', 'voorraad', 'prijs'))
    while True:
        artikelnummer = input('Wat is het artikelnummer: ')
        if artikelnummer == 'einde':
            break
        artikelcode = input('Voer de artikelcode in: ')
        Naam = input('Wat is uw naam? ')
        Voorraad = input('Wat is de voorraad? ')
        Prijs = input('Wat is de prijs? ')
        writer.writerow(('artikelnummer', 'artikelcode', 'naam', 'voorraad', 'prijs'))