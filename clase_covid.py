# -*- coding: utf-8 -*-
from covid import Covid

# Creamos un objeto codiv
covid = Covid(source="worldometers")


# Defino una clase para porder utilizar con facilidad
class ClaseCovid():
    def __init__(self, pais):
        self.pais = pais
        self.diccionario_datos = covid.get_status_by_country_name(self.pais)
        
    
        self.confirmados = self.diccionario_datos["confirmed"]
        self.activos = self.diccionario_datos["active"]
        self.muertos = self.diccionario_datos["deaths"]
        self.recuperados = self.diccionario_datos["recovered"]
        self.muertos = self.diccionario_datos["deaths"]
        self.nuevosCasos = self.diccionario_datos["new_cases"]
        self.nuevosMuertos = self.diccionario_datos["new_deaths"]
        self.casosCriticos = self.diccionario_datos["critical"]
        self.poblacion = self.diccionario_datos["population"]

    def verificarCasos(self):
        if (self.muertos + self.recuperados + self.activos) == self.confirmados:
            return True
        else:
            return False
    
    def calculoMortalidad(self):
        # Calculo el porcentaje de muertos y redondeo el nº
        return round((self.muertos * 100) / self.confirmados, 2)

    def calculoNivelMortalidad(self):
        indiceMortalidad = self.calculoMortalidad()

        if indiceMortalidad < 2:
            return "Indice de mortalidad bajo"
        elif indiceMortalidad <= 3.5:
            return "Indice de mortalidad medio"
        else:
            return "Indice de mortalidad alto"
    
    def calculoRecuperados(self):
        return round((self.recuperados * 100) / self.confirmados, 2)  

    def calculoCasosCriticos(self):
        return round((self.casosCriticos * 100) / self.activos, 2)

    def calculoPoblacionContagiada(self):
        return round((self.confirmados * 100) / self.poblacion, 2)

    def __str__(self):
        return "Pais: {}; Casos confirmados: {}; Casos activos: {}; Muertos: {}; Recuperados: {}; Nuevos Casos: {}; Nuevos Muertos: {}; Casos Criticos: {}".format(
            self.pais, 
            self.confirmados, 
            self.activos, 
            self.muertos, 
            self.recuperados,
            self.nuevosCasos,
            self.nuevosMuertos,
            self.casosCriticos
            )
