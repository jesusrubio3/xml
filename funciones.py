from lxml import etree

def menu():
    numero=int(input("""Elige una opción:
    1 Listar todos los equipos de la liga.
    2 Número de jugadores de cada equipo. 
    3 Introduce un equipo para saber el nombre de sus delanteros.
    4 Introduce un jugador para saber su equipo.
    5 Para saber el estadio más antiguo.
    6 Para salir.
    Opción: """))
    return numero

def lectura_xml(xml):
    doc=etree.parse(xml)
    return doc

def equipos(fichero):
    listado=fichero.xpath('/League/Team/@id')
    return listado

