import math
radio = input("Ingrese el radio: ")
perimetro = 2 * math.pi * int(radio)
area = math.pi * int(radio) **2
print("El perímetro es:" + str(perimetro) + "\n\r")
print("El área es:" + str(area))