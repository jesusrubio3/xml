from funciones import menu,lectura_xml,equipos

archivo=lectura_xml("liga.xml")
menu2=menu()

while menu2!=6:
    if menu2==1:
        print("Estos son todos los equipos de la liga:")
        for i in equipos(archivo):
            print(i)
    menu2=menu()