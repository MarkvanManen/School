def standaardprijs(afstandKM):
    if afstandKM < 0:
        return 0
    elif afstandKM < 50:
        return afstandKM * 0.80
    elif afstandKM > 50:
        return afstandKM * 0.60 + 15

def ritprijs(leeftijd, weekendrit, afstandKM):
    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit:
            return 0.65 * standaardprijs(afstandKM)
        return 0.7 * standaardprijs(afstandKM)

    if weekendrit:
        return 0.6 * standaardprijs(afstandKM)
    return 0.1 * standaardprijs(afstandKM)


    # Oude manier

    #if (leeftijd < 12 and weekendrit == True) or (leeftijd >= 65 and weekendrit == True):
        #totaleprijs = 0.65 * standaardprijs(afstandKM)
    #elif (leeftijd < 12 and weekendrit == False) or (leeftijd >= 65 and weekendrit == False):
        #totaleprijs = 0.7 * standaardprijs(afstandKM)
    #elif (leeftijd > 12 and weekendrit == True) or (leeftijd < 65 and weekendrit == True):
        #totaleprijs = 0.6 * standaardprijs(afstandKM)
    #elif (leeftijd > 12 and weekendrit == False) or (leeftijd < 65 and weekendrit == False):
        #totaleprijs = 1 * standaardprijs(afstandKM)
    #else:
     #   print("error")
    #return str(totaleprijs)

leeftijd = eval(input('Wat is uw leeftijd?: '))
weekendrit = input("Rijst u in het weekend, ja of nee: ")
afstandKM = eval(input("Hoeveel kilometer gaat u reizen?: "))

if weekendrit == "ja" or weekendrit == "Ja":
    weekendrit = True
elif weekendrit == "nee" or weekendrit == "Nee":
    weekendrit = False


print("Uw kaartje kost " + str(ritprijs(leeftijd, weekendrit, afstandKM)) + ' euro.')


