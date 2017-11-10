import random

def gooien():
    global worp1
    global worp2
    global uitslag
    worp1 = random.randrange(1, 7)
    worp2 = random.randrange(1, 7)
    uitslag = worp1 + worp2

def monopolyworp():
    gooien()
    if worp1 == worp2:
        print(str(worp1) + ' + ' + str(worp2) + ' = ' + str(uitslag) + '(dubbel)')
        gooien()
        if worp1 == worp2:
            print(str(worp1) + ' + ' + str(worp2) + ' = ' + str(uitslag) + '(dubbel)')
            gooien()
            if worp1 == worp2:
                print(str(worp1) + ' + ' + str(worp2) + ' = ' + str(uitslag) + '(dubbel)')
                gooien()
                if worp1 == worp2:
                    print(str(worp1) + ' + ' + str(worp2) + ' = ' + '(direct naar de gevangenis)')
    print(str(worp1) + ' + ' + str(worp2) + ' = ' + str(uitslag))

monopolyworp()

