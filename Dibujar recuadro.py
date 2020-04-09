# awa?
ancho = int(input('Introduce la anchura del rectángulo: '))
alto = int(input('Introduce la altura del rectángulo: '))
dibujo = '·'
espacio = ' '
if ancho != alto:
    for i in range(alto):
        if i == 0 or i == (alto-1):
            print(dibujo * ancho)
        else:
            print(dibujo + espacio * (ancho-2) + dibujo)
else:
    print('La altura y anchura de un rectángulo NO pueden ser iguales')