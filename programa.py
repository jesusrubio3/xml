from funciones import menu,lectura_xml,equipos,numjugadores

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
    menu2=menu()