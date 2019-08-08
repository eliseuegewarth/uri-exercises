
x,y = [int(x) for x in input().split()]

table = [0, 4.00, 4.50, 5.00, 2.00, 1.50]
total = table[x]*y
print("Total: R$ {0:.2f}".format(total))
