
a, b, c = [int(x) for x in input().split()]

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

print("{} eh o maior".format(maior))
