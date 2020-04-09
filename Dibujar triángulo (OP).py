 # awa?
from time import sleep
pln = 0

#Los números Mason.
def ln():
    de = str(input('¿Mostrar números de línea? (Y/[N]): ') or 'N')
    global pln
    if de.capitalize() == 'Y':
        pln = 1

def heh(line,alt):
    des = None
    if line == 69:
        des = '\n' + ' '*(int(alt)-5) +'( ͡° ͜ʖ ͡°)'
    else:
        des = ''
    return des

def ies():
    mn = 3
    mx = 69
    d = '*'
    al = None

    #Obtener input y comprobar si es número entero.
    try:
        al = int(input('Introduce la altura del triángulo: \033[1;36m'))
    except ValueError:
        print('\033[0;0mPor favor introduce un número entero.')
        sleep(1)
        ies()

    #Dibújame bb
    if not al < mn and not al > mx:
        #Pre-draw
        print(f'\033[0;0mDibujando triángulo de \033[1;36m{al}\033[0;0m de alto.\n')
        sleep(.7)

        v = al+1
        for i in range(al):
            v-=1
            if pln:
                print(f'\033[1;36m{i+1:2d}\033[0;0m| '+' '*v + d*(((i+1)*2)-1) + str(heh(i+1,al)))
            else:
                print(f' '*v + d*(((i+1)*2)-1) + str(heh(i+1,al)))
            sleep(.8/al)
        print('\n\033[1;36mDibujado\033[0;0m.')
        sleep(.7)
        rei()
    else:
        print(f'\033[0;0mPor favor introduce un número entre \033[1;36m{mn}\033[0;0m y \033[1;36m{mx}\033[0;0m.')
        sleep(.7)
        ies()

#Repetimos maybe.
def rei():
    eh = str(input('¿Dibujar otro? ([Y]/N): ') or 'Y')
    if eh.capitalize() != 'Y':
        print('bai.')
        exit()
    else:
        ies()

# Título
print('\033[1;36m-= \033[0;0mTriangular drawer 3000 \033[1;36m=-\033[0;0m')

#Animación inicial
for w in range (0,5):
    z = ' Cargando' + '.'* w
    if w != 4:
        print (z, end="\r")
        sleep(.5)
    else:
        print ('\033[1;36mCargado\033[0;0m.', end="\r")
        sleep(.8)

ln()
ies()
exit()