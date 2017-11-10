def seizoen(maandnummer):
    if maandnummer == 12 or maandnummer == 1 or maandnummer == 2:
        return 'Het is winter.'
    elif maandnummer == 3 or maandnummer == 4 or maandnummer == 5:
        return 'Het is lente.'
    elif maandnummer == 6 or maandnummer == 7 or maandnummer == 8:
        return 'Het is zomer.'
    elif maandnummer == 9 or maandnummer == 10 or maandnummer == 11:
        return 'Het is herfst.'
    else:
        return 'Dat is geen maand, pik.'

maandnummer = eval(input('Welk nummer heeft de maand?: '))
print(seizoen(maandnummer))