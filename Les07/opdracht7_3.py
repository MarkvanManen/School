cijfers = {'Kees':'6.5', 'Koek':'9.2', 'Klaas':'4.5', 'Pieter':'8.7', 'Gerard':'6.7', 'Jacob':'9.7', 'Stefan':'8.4', 'Soepkip':'5.4', 'Bernhard':'9.5'}

def goedecijfers():
    for naam in cijfers:
        if str(cijfers[naam]) > str(9.0):
            print(cijfers(naam))
        else:
            None

print (goedecijfers())

