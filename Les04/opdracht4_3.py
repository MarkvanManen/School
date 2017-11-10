def lang_genoeg(lengte):
    if lengte >= int(120):
        return True

lengte = int(input('Hoe lang ben je?: '))
if lang_genoeg(lengte) == True:
    print('Je bent lang genoeg!')
else:
    print('Sorry, je bent te klein!')
