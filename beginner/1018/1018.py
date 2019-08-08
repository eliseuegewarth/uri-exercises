
x = int(input())
r = x
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

print("{}".format(r))
print("{} nota(s) de R$ 100,00".format(c00))
print("{} nota(s) de R$ 50,00".format(c0))
print("{} nota(s) de R$ 20,00".format(v0))
print("{} nota(s) de R$ 10,00".format(d0))
print("{} nota(s) de R$ 5,00".format(c))
print("{} nota(s) de R$ 2,00".format(d))
print("{} nota(s) de R$ 1,00".format(um))
