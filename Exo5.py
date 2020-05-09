pSeuil = 2.3
vSeuil = 7.41

pEnceinte = float(input('Saisissez la pression de l enceinte: '))
vEnceinte = float(input('Saisissez le volume de l enceinte: '))

if (pEnceinte > pSeuil) & (vEnceinte > vSeuil):
    exit()
elif pEnceinte>pSeuil:
    print('Veuillez augmenter le volume de l enceinte')
elif vEnceinte>vSeuil:
    print('Veuillez diminuer le volume de l enceinte')
else:
    print('Tout va bien')