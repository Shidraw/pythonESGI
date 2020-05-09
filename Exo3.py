import math

number = float(input('Saisissez un flottant:'))

if number > 0:
    print('Racine du nombre : ' + str(math.sqrt(number)))
else :
    print('ERREUR')