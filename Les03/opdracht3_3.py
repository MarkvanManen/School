leeftijd = int(input( 'Geef je leeftijd: '))
paspoort = input('Nederlands paspoort: ')
if leeftijd > 17 and paspoort == 'ja':
    print ('Gefeliciteerd, je mag stemmen')
else:
    print ('Sorry, je mag nog niet stemmen.')