from collections import Counter

def compterMots(s):
    return Counter(s)

l = ['Blue', 'Yellow', 'blue', 'Blue', 'Green']

print(compterMots(l))