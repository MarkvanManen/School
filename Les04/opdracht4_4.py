cijferlijst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
cijferinpassword = False

def new_password(oldpassword, newpassword):
    cijferinpassword = False
    for nummer in cijferlijst:
        if nummer in newpassword:
            cijferinpassword = True
    if oldpassword != newpassword and len(newpassword) >= 6 and cijferinpassword:
        return True
    else:
        return False

oldpassword = input("Wat is je oude wachtwoord?: ")
newpassword = input('Wat is je nieuwe wachtwoord?: ')

if new_password(oldpassword, newpassword) == True:
    print('Je wachtwoord is veranderd')
else:
    print('Je wachtwoord voldoet niet aan de eisen')





