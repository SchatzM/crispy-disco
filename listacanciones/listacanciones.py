import random
import xmltodict
import json

# Función que procesa el xml 'library' obteniendo información de las canciones
# y espera como parámetro el modo de respuesta deseada, ya sea 
# 'random' ('r'), 'lista' ('l') o por defecto 'diccionario' ('d').

def listacanciones(modo='d'):
    uarx = 'lib/library.xml'
    with open(uarx) as lib:
        base = xmltodict.parse(lib.read())['library']['track']
    if isinstance(modo, str):
        m = str(modo)
        if m in {'diccionario','d'}:
            return json.dumps(base)
        elif m in {'lista','random','l','r'}:
            lst = []
            for sng in base:
                lst.append(sng['name'])
            if m in {'random','r'}:
                return random.choice(lst)
            return lst
    else:
        return 'Parámetro no válido.'

print(listacanciones(False))