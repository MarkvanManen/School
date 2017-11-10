import datetime
outfile = open('hardlopers.txt', 'w')
vandaag = datetime.datetime.today()
s = vandaag.strftime('%a %d %b %Y')
outfile.write(s + '10:45:52, Miranda\n')
outfile.write(s + '10:46:04, Piet\n')
outfile.write(s + '10:47:27, Sacha\n')
outfile.write(s + '10:48:33, Karel\n')
outfile.write(s + '10:48:42, Kemal\n')
outfile.close()

print(s)