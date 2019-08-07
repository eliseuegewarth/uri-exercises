
x, cents = input().split('.')
x = int(x)
c00 = x//100
x = x%100
c0 = x//50
x = x%50
v0 = x//20
x = x%20
d0 = x//10
x = x%10
c = x//5
x = x%5
d = x//2
x = x%2
um = x

cents = int(cents)
cent50 = cents//50
cents = cents%50
cent25 = cents//25
cents = cents%25
cent10 = cents//10
cents = cents%10
cent5 = cents//5
cents = cents%5

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(c00))
print("{} nota(s) de R$ 50.00".format(c0))
print("{} nota(s) de R$ 20.00".format(v0))
print("{} nota(s) de R$ 10.00".format(d0))
print("{} nota(s) de R$ 5.00".format(c))
print("{} nota(s) de R$ 2.00".format(d))

print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(um))
print("{} moeda(s) de R$ 0.50".format(cent50))
print("{} moeda(s) de R$ 0.25".format(cent25))
print("{} moeda(s) de R$ 0.10".format(cent10))
print("{} moeda(s) de R$ 0.05".format(cent5))
print("{} moeda(s) de R$ 0.01".format(cents))
