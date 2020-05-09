import re

def verifyEmail(s):
    return re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", s)

temp = 'blabla@gmail.com'
temp1 = 'blabla.com'
temp2 = 'blabla@com'

print(verifyEmail(temp))
print(verifyEmail(temp1))
print(verifyEmail(temp2))