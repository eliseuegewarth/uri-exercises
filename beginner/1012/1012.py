
pi = 3.14159
a, b, c = [float(x) for x in input().split()]

print("TRIANGULO: {0:.3f}".format(a*c/2))
print("CIRCULO: {0:.3f}".format(pi*c*c))
print("TRAPEZIO: {0:.3f}".format(c*(a+b)/2))
print("QUADRADO: {0:.3f}".format(b*b))
print("RETANGULO: {0:.3f}".format(a*b))
