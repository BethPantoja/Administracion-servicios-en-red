from crearReporte import reporteAgente


def agregarAgente():
    print()
    print("\n Para agregar un nuevo agente es necesario que ingrese los siguientes datos:\n")
    comunidad = input("Comunidad: ")
    version = input("Version: ")
    puerto = input("Puerto: ")
    ip = input("Host: ")

    with open("ListaAgentes.txt", "a") as archivo:
        archivo.write(comunidad + " " + version + " " + puerto + " " + ip + "\n")
    
    archivo.close()


def cambiarAgente():
    print()
    i = 1
    print("Agentes guardados en el archivo txt: \n")
    with open("ListaAgentes.txt", "r") as archivo:
        datos = archivo.readlines()
    print("ID \t\tAgentes\n ")

    with open("ListaAgentes.txt", "r") as archivo:
        for line in archivo:
            print(str(i) + "\t" + line)
            i = i + 1

    borrar=int(input("Ingrese el ID del Agente que desea cambiar:"))    
    i = 1
    print()
    comunidad = input("Comunidad: ")
    version = input("Version: ")
    puerto = input("Puerto: ")
    ip = input("IP: ")
    print()

    with open("ListaAgentes.txt", "w") as archivo:
        for line in datos:
            if i != borrar:
                archivo.write(line)
            else:
                archivo.write(comunidad + " " + version + " " + puerto + " " + ip + "\n")
            i = i + 1
    borrar = borrar + 1
    
    archivo.close()


def borrarAgente():
    print()
    i = 1
    print("Agentes guardados en el archivo txt: ")

    with open("ListaAgentes.txt", "r") as archivo:
        datos = archivo.readlines()
    print("ID \t\tAgentes: ")
    with open("ListaAgentes.txt", "r") as archivo:
        for line in archivo:
            print(str(i) + "\t\t" + line)
            i = i + 1


    
    borrar=int(input("Ingrese el ID del Agente que desea borrar:"))    
    i = 1
    with open("ListaAgentes.txt", "w") as archivo:
        for line in datos:
            if i != borrar:
                archivo.write(line)
            i = i + 1
    archivo.close()




print("\n\t Sistema de Administracion de Red \n\n")
print("\n\t Práctica 1- Adquision de Información \n")
print("\n Alumna:\t Lizbeth Pantoja Rodríguez")
print("\n\t Grupo: 4CM14 \t\t Boleta: 2014081159")
print("---------------------------------------------------")


while True:
    print("")
    print("Elija una opción:\n")    
    print("\t 1) Agregar Agente")
    print("\t 2) Cambiar informacion de Agente")
    print("\t 3) Eliminar informacion de dipostivo")
    print("\t 4) Generar reporte")
    print("----------------------------------------")
    print("0. Salir")
    print()
    option = int(input("Ingrese la accion: "))
    if option == 1:
        agregarAgente()
    elif option == 2:
        cambiarAgente()
    elif option == 3:
        borrarAgente()
    elif option == 4:
        reporteAgente()
    elif option == 0:
        print("Haz salido del Sistema de Administracion de Red")
        break
    else:
        print("Error")
    print()