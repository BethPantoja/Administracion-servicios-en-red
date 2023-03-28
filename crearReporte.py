from getSNMP import consultaSNMP
from reportlab.platypus import Table
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import time

def reporteAgente():
    print()
    
    with open("ListaAgentes.txt", "r") as archivo:
        devices = archivo.readlines()

    i = 1
    print("Agentes: ")
    with open("ListaAgentes.txt", "r") as archivo:
        for line in archivo:
            print(str(i) + "\t" + line)
            i = i + 1
    numero = int(input("Agente a generar reporte: ")) - 1
    datos = devices[numero].split()

    comunidad = datos[0]
    version = datos[1]
    puerto = datos[2]
    ip = datos[3]

    datosSNMP = consultaSNMP(comunidad, ip, "1.3.6.1.2.1.1.1.0", puerto)
    sistemaOpe = " "
    if datosSNMP.find("Linux") == 1:
        sistemaOpe = datosSNMP.split()[0]
    else:
        sistemaOpe = datosSNMP.split()[12]
    
    nombredis = consultaSNMP(comunidad, ip, "1.3.6.1.2.1.1.5.0", puerto)
    contact = consultaSNMP(comunidad, ip, "1.3.6.1.2.1.1.4.0", puerto)
    ubi = consultaSNMP(comunidad, ip, "1.3.6.1.2.1.1.6.0", puerto)
    numInter = consultaSNMP(comunidad, ip, "1.3.6.1.2.1.2.1.0", puerto)

  

    i = 1
    interfaces = []
    while i <= int(numInter):
        interfaz = consultaSNMP(comunidad, ip, "1.3.6.1.2.1.2.2.1.7." + str(i), puerto)
        interfaces.append(interfaz)
        i = i + 1

    timestr = time.strftime("%Y%m%d-%H%M%S")

    pdf = canvas.Canvas("Reporte interfaz" + timestr + ".pdf",pagesize=A4)
    pdf.setTitle("REPORTE")
    w, h = A4
    pdf.setFont("Times-Roman",18,1)
    pdf.drawString(50, 750, "Administración de Servicios en Red")
    pdf.drawString(50, 725, "Práctica 1: Adquisición de Información")
    pdf.setFont("Times-Roman",16,1)
    pdf.drawString(50, 700, "Alumna: Pantoja Rodríguez Lizbeth      Grupo: 4CM14")
    
   

    
    if sistemaOpe.find("Linux") ==1:        
        pdf.drawImage("linux.png",500,700,width=60,height=50)
    else:
        pdf.drawImage("windows.png",500,700,width=60,height=50) 

    pdf.setFont("Times-Roman",16,2)
    pdf.drawString(50, 650, "Información del inventario:")
    pdf.setFontSize(14)
    pdf.drawString(75, 625, "Nombre del Agente: " + nombredis)
    pdf.drawString(75, 600, "Sistema operativo: " + sistemaOpe)
    pdf.drawString(75, 575, "Información de contacto: " + contact)
    pdf.drawString(75, 550, "Ubicacion: " + ubi)
    pdf.drawString(75, 525, "Cantidad de  interfaces: " + numInter)
    
    pdf.setFont("Times-Roman",16,2)
    pdf.drawString(50, 500, "Información del interfaces:")
    pdf.setFontSize(14)
    i = 1
    matriz = [["Interfaz", "Estatus"]]
    while i <= int(numInter):
        if i == 6:
            break
        if sistemaOpe.find("Linux") != -1:
            descrInterfaz = consultaSNMP(comunidad, ip, "1.3.6.1.2.1.2.2.1.2." + str(i), puerto)
        else:
            res = consultaSNMP(comunidad, ip, "1.3.6.1.2.1.2.2.1.2." + str(i), puerto)[3:]
            descrInterfaz = bytes.fromhex(res).decode('utf-8')

        estadoInterfaz = consultaSNMP(comunidad, ip, "1.3.6.1.2.1.2.2.1.7." + str(i), puerto)

        if estadoInterfaz == " 1":
            matriz.append([descrInterfaz, "Activo"])
        elif estadoInterfaz == " 2":
            matriz.append([descrInterfaz, "Inactivo"])
        else:
            matriz.append([descrInterfaz, "-"])
        i = i + 1

    width = 300
    height = 300
    x = 100
    y = 350
    f = Table(matriz)
    f.wrapOn(pdf, width, height)
    f.drawOn(pdf, x, y)
    
    pdf.save()

    return print("Se ha creado el reporte")
