naam = input('Wat is je voornaam: ')

def namen():
    aantalkeernaam = {}
    for aantal in naam:
        if aantal in aantalkeernaam:
            aantalkeernaam[aantal] += 1
        else:
            aantalkeernaam[aantal] = 1
    return aantalkeernaam

print(namen())