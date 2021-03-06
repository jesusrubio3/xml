from funciones import menu,lectura_xml,equipos,numjugadores,delanteros

archivo=lectura_xml("liga.xml")
menu2=menu()

while menu2!=6:
    if menu2==1:
        print("Estos son todos los equipos de la liga:")
        for i in equipos(archivo):
            print(i)
    
    if menu2==2:
        print("Estos son los jugadores que tiene cada equipo:")
        for i in numjugadores(archivo):
            for j in i:
                print("%s tiene %d jugadores"%(j,i[j]))
    
    if menu2==3:
        nombre_equipo=input("Introduce el nombre del equipo(se recomienda ver la opción 1 para saber los equipos): ")
        print("Estos son los delanteros del %s"%nombre_equipo)
        for i in delanteros(nombre_equipo,archivo):
            if len(delanteros(nombre_equipo,archivo))==0:
                print("no tiene delanteros.")
            else:   
                print(i)
    menu2=menu()