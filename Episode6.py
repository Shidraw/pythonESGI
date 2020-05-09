def checkValue(line):
    words = line.split("\\")
    if words[2] < words[3]:
        return True
    return False


content = input("Saisissez le nom de votre fichier : ")
file = open(content + '.txt', "r")

lines = file.readlines()
file.close()

for line in lines:
    if checkValue(line):
        print(line[4:9] + " " + line[11:16])
        print("OUI")
    else:
        print(line[4:8] + " " + line[10:14])
        print("NON")