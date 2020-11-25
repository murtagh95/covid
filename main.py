# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from covid import Covid
from crear_objeto import crearObjeto

# Creo la ventana   
raiz = Tk()
raiz.title("Covid")
raiz.geometry("200x70")
raiz.resizable(0,0)

covid1 = Covid(source="worldometers")
PAISES = covid1.list_countries()

def crearPrimeraPantalla():
    raiz.deiconify()

    miFrame1 = Frame(raiz)
    miFrame1.pack()

    # Le pido al Usuario que eliga un pais
    paisLabel = Label(miFrame1, text="Por favor eleguir un país de la lista")
    paisLabel.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    def creoObjetoYSegundaPantalla(evento):
        # Creo el objeto y se lo paso a la segunda pantalla
        crearSegundaPantalla(crearObjeto(pais.get()))
        


    # Añado una lista con los paises 
    pais = StringVar()
    listaPaises =ttk.Combobox(miFrame1, state="readonly", textvariable=pais)
    listaPaises.grid(row=1, column=0)
    # Agrego las opciones
    listaPaises["value"] = PAISES
    # Llamamos a una función cuando se eligue una opción
    listaPaises.bind("<<ComboboxSelected>>", creoObjetoYSegundaPantalla)

    raiz.mainloop()



def volverAtras(segundaVentana):
    segundaVentana.destroy()
    crearPrimeraPantalla()


def crearSegundaPantalla(covid):
    
    # Llamo a la variable global de la ventana
    global raiz
    # Creo una segunda ventana
    segundaVentana = Toplevel(raiz)
    segundaVentana.resizable(0,0)
    # Desaparesco la primer ventana
    raiz.withdraw()

    # Informamos de que país es la información
    cadenaLabelPais = covid.pais + " es el pais del que provienen los siquientes datos"
    paisLabel = Label(segundaVentana, text=cadenaLabelPais, fg="green")
    paisLabel.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Mostramos los casos confirmados
    confirLabel = Label(segundaVentana, text="Casos confirmados:")
    confirLabel.grid(row=1, column=0)
    confirInfo = Label(segundaVentana, text=str(covid.confirmados), fg="red")
    confirInfo.grid(row=1, column=1)

    # Mostramos los recuperados
    recupeLabel = Label(segundaVentana, text="Recuperados:")
    recupeLabel.grid(row=2, column=0)
    recupeInfo = Label(segundaVentana, text=str(covid.recuperados), fg="red")
    recupeInfo.grid(row=2, column=1)

    # Mostramos los casos activos
    activosLabel = Label(segundaVentana, text="Casos activos:")
    activosLabel.grid(row=3, column=0)
    activosInfo = Label(segundaVentana, text=str(covid.activos), fg="red")
    activosInfo.grid(row=3, column=1)

    # Mostramos los muertos
    muertosLabel = Label(segundaVentana, text="Muertos:")
    muertosLabel.grid(row=4, column=0)
    muertosInfo = Label(segundaVentana, text=str(covid.muertos), fg="red")
    muertosInfo.grid(row=4, column=1)

    # Mostramos los casos criticos
    muertosLabel = Label(segundaVentana, text="Casos criticos:")
    muertosLabel.grid(row=5, column=0)
    muertosInfo = Label(segundaVentana, text=str(covid.casosCriticos), fg="red")
    muertosInfo.grid(row=5, column=1)

    # Mostramos el porcentaje de recuperados
    porceRecuperadosLabel = Label(segundaVentana, text="Porcentaje de Recuperados:")
    porceRecuperadosLabel.grid(row=6, column=0)
    porceRecuperadosInfo = Label(segundaVentana, text=str(covid.calculoRecuperados()) + "%", fg="red")
    porceRecuperadosInfo.grid(row=6, column=1)

    # Mostramos el porcentaje de muertos 
    porceMuertosLabel = Label(segundaVentana, text="Porcenjate de muertos:")
    porceMuertosLabel.grid(row=7, column=0)
    porceMuertosInfo = Label(segundaVentana, text=str(covid.calculoMortalidad()) + "%", fg="red")
    porceMuertosInfo.grid(row=7, column=1)

    # Mostramos el nivel de mortalidad <2 → índice bajo, entre 2 y 3.5 → índice medio, >3.5 → índice alto
    nivelMortalidadLabel = Label(segundaVentana, text="Nivel de mortalidad:")
    nivelMortalidadLabel.grid(row=8, column=0)
    nivelMortalidadInfo = Label(segundaVentana, text=str(covid.calculoNivelMortalidad()), fg="red")
    nivelMortalidadInfo.grid(row=8, column=1)

    # Mostramos el porcentaje de casos criticos respecto a los casos activos
    porceCriticosLabel = Label(segundaVentana, text="Porcentaje de criticos respecto a activos:")
    porceCriticosLabel.grid(row=9, column=0)
    porceCriticosInfo = Label(segundaVentana, text=str(covid.calculoCasosCriticos()) + "%", fg="red")
    porceCriticosInfo.grid(row=9, column=1)

    # Mostramos el porcentaje de contagiados respecto a la poblacion total
    porceContagiadosLabel = Label(segundaVentana, text="Porcentaje de contagiados respecto a poblacion:")
    porceContagiadosLabel.grid(row=10, column=0)
    porceContagiadosInfo = Label(segundaVentana, text=str(covid.calculoPoblacionContagiada()) + "%", fg="red")
    porceContagiadosInfo.grid(row=10, column=1)

    botonVolver = Button(segundaVentana, text="Volver a tras", command=lambda : volverAtras(segundaVentana))
    botonVolver.grid(row=11, column=0)


    raiz.mainloop()
crearPrimeraPantalla()
