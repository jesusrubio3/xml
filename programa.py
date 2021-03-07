from funciones import menu,lectura_xml,equipos,numjugadores,delanteros,equipojugador,estadio

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
    if menu2==4:
        jugador=input("introduce un jugador: ")
        
        if len(equipojugador(jugador,archivo))==0:
                print("ese jugador no está en la liga")
        else:
            for i in equipojugador(jugador,archivo):
                print("El equipo de %s es el %s"%(jugador,i))
    
    if menu2==5:
        anio=[]
        for i in estadio(archivo):
            for j in i.values():
                for z in j:
                    z=int(z)
                    anio.append(z)
        antiguo=min(anio)
        antiguo=str(antiguo)
        
        for i in estadio(archivo):
            for estadio,age in i.items():
                for x in age:
                    if x==antiguo:
                        print("el estadio más antiguo es el del %s"%estadio)
                
        
    menu2=menu()