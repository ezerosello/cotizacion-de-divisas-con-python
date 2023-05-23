from tkinter import *
import requests
from bs4 import BeautifulSoup as b


def escribir_info_web(archivo):
    web = requests.get('https://www.bna.com.ar/Personas')
    contenido_web = web.content
    soup = b(contenido_web, "html.parser")

    cotizaciones = soup.find("table",{"class":"table cotizacion"})
    cotizaciones_texto = cotizaciones.text

    archivo.write(cotizaciones_texto)
    archivo.seek(0)


def leer_datos(archivo):
    linea = archivo.readline()
    lista = []
    lista_datos = []

    while(linea):
        lista.append(linea)
        linea = archivo.readline()

    for i in lista:
        if i != "\n":
            lista_datos.append(i)

    return lista_datos


def interfaz(archivo, lista):
    raiz = Tk()
    raiz.title("Cotización de billetes")
    raiz.resizable(False, False)
    raiz.geometry("500x320")
    raiz.config(bg="light green")

    fondo_titulo = Frame(raiz, width ="500", height="50", bg="green").pack()
    titulo = Label(fondo_titulo, text = "Cotización de billetes", bg="green", fg="white", font=("Arial", 12, "bold")).place(x=165,y=10)

    datos_mostrados = Label(raiz, text = "Divisa:\n\nCompra:\n\nVenta:", bg = "light green", font= ("Arial", 12, "bold")).place(x=10, y = 60)

    datos_dolar = Label(raiz, text= str(lista[3] + "\n" + lista[4] + "\n" + lista[5]), bg="light green",
                        font= ("Arial", 12, "bold")).place(x=100, y=60)
    datos_euro = Label(raiz, text= str(lista[6] + "\n" + lista[7] + "\n" + lista[8]), bg = "light green",
                       font= ("Arial", 12, "bold")).place(x=250, y=60)
    datos_real = Label(raiz, text= str(lista[9] + "\n" + lista[10] + "\n" + lista[11]),
                       bg = "light green", font= ("Arial", 12, "bold")).place(x=400, y=60)
    disclaimer_real = Label(raiz, text="*cotización cada\n 100 unidades", bg="light green", font=("Arial", 8, "bold")).place(x=390, y=160)

    boton_copiar = Button(raiz, bg="green", fg="white", text= "        Copiar datos a un        \narchivo de texto", 
                          command=lambda:archivo.write(str(lista[3] + lista[4] + lista[5] +"\n"+ lista[6] + lista[7] + lista[8] +"\n"+ lista[9] \
                                                           + lista[10] + lista[11] + "(*) cotización cada 100 unidades."))+archivo.seek(0)).place(x=175, y=200)

    disclaimer = Label(raiz, text= "Datos extraídos de la web del Banco de la Nación Argentina\n Los valores mostrados son en pesos argentinos",
                       bg="light green", font=("Arial", 8, "bold")).place(x=83, y = 260)

    raiz.mainloop()


def interfaz_error():
    raiz = Tk()
    raiz.geometry("215x100")
    raiz.resizable(False, False)
    raiz.title("Error")
    texto_error = Label(raiz, text="Hubo un error\nRevisá tu conexión a internet", font=("Arial", 10, "bold")).place(x=10, y=10)

    boton_ok = Button(raiz, text="          OK          ", command=lambda: raiz.destroy()).place(x=63 ,y=60)

    raiz.mainloop()


def main():
    try:
        archivo1 = open("datos_web.txt","r+")
        archivo2 = open("datos_copiados.txt", "w")

        escribir_info_web(archivo1)
        lista = leer_datos(archivo1)

        interfaz(archivo2, lista)

        archivo1.close()
        archivo2.close()

    except:
        interfaz_error()


main()