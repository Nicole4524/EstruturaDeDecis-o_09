#Faça um Programa que leia três números e mostre-os em ordem decrescente.

x = float(input("Insira o primeiro número:"))
y = float(input("Insira o segundo número:"))
z = float(input("Insira o terceiro número:"))

if x > y and x > z and y > z:
    print("A ordem decrescente é:", {x}, {y}, {z})
elif x > y and x > z and z > x:
    print("A ordem decrescente é:", {x}, {z}, {y})

elif y > x and y > z and y > z:
    print("A ordem decrescente é:", {y}, {x}, {z})
elif y > x and y > z and z > x:
    print("A ordem decrescente é:", {y}, {z}, {x})

elif z > x and z > y and x > y:
    print("A ordem decrescente é:", {z}, {x}, {y})
elif z > x and z > y and y > x:
    print("A ordem decrescente é:", {z}, {y}, {x})