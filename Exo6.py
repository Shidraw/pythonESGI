sentence = input('Saisissez votre email: ')

find = sentence.find('.com')
length = len(sentence)

if ('@' in sentence) & (length - find == 4):
    print('Email valide')
else:
    print('Email invalide')