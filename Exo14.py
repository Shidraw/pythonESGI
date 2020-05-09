def est_premier(n) :
    if n < 2:
        return False
    i = 2

    while i < n and n%i != 0:
        i += 1
    return i == n

max = int(input('Saisissez le nb de nb premiers à afficher : '))
cpt = 0
start = 2
while cpt < max:
    if est_premier(start):
        cpt += 1
        print(start)
        start += 1
    else:
        start += 1

