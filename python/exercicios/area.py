#calculo de area
a = float(input())
b = float(input())
c = float(input())
pi = 3.14159

print("TRIANGULO:"+str(round(((a*c)/2),3)))
print("CIRCULO:"+str(round((c*c)*pi,3)))
print("TRAPEZIO:"+str(round((((a+b)*c)/2),3)))
print("QUADRADO:"+str(round((b*b),3)))
print("RETANGULO:"+str(round((a*b),3)))