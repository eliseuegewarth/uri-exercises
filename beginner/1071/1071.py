
x = int(input())
y = int(input())
if x > y:
	x, y = y, x
soma = 0
for i in range(x+1, y):
	if i%2!=0:
		soma = soma + i
print(soma)
