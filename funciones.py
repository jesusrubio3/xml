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

def numjugadores(fichero):
    diccionario={}
    lista=[]
    nombreeqipos=equipos(fichero)
    for i in nombreeqipos:
        num=fichero.xpath('count(/League/Team[@id="%s"]/Players/person)'%i)
        diccionario={i:num}
        lista.append(diccionario)

    return lista

def delanteros(delanequipo,fichero):
    delan=fichero.xpath('/League/Team[@id="%s"]/Players/person[Position="DC"]/first_name/text()'%delanequipo)
    return delan

def equipojugador(jugador,fichero):
    jugador2=jugador.title()
    
    equipo=fichero.xpath('//person[first_name="%s"]/../../@id'%jugador2)
    return equipo

def estadio(fichero):
    diccionario={}
    lista=[]
    nombreeqipos=equipos(fichero)
    for i in nombreeqipos:
        anio=fichero.xpath('/League/Team[@id="%s"]/anio/text()'%i)
        diccionario={i:anio}
        lista.append(diccionario)
    
    

    
    return lista


        

