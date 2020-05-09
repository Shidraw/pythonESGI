import re

def verifyEmail(s):
    return re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", s)

file = open('test2.txt', mode='r')
content = file.readlines()
for line in content:
    if verifyEmail(line):
        print('Email correct : ' + line)
    else:
        print('Email incorrect : ' + line)
file.close()