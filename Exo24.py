from math import pi

def cube(n):
    return n*n*n

def volumeSphere(rayon):
    return 4/3 * pi * cube(rayon)

print(volumeSphere(3))