x = int(input('Saisissez un nombre d ecriture : '))

file = open('test.txt', mode="w")
while x > 0:
    temp = str(input('Saisissez un texte à écrire dans le fichier : '))
    file.write(temp)
    file.write("\n")
    x -= 1
file.close()

file = open('test.txt')
content = file.readlines()
file.close()

print(content)