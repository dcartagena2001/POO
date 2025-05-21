from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"

class Planeta:
    def __init__(self, nombre=None, cantidad_satelites=0, masa=0, volumen=0, 
    diametro=0, distancia_sol=0, tipo=TipoPlaneta.TERRESTRE, es_observable=False):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.es_observable = es_observable

    def imprimir(self):
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidad_satelites}")
        print(f"Masa del planeta = {self.masa}")
        print(f"Volumen del planeta = {self.volumen}")
        print(f"Diámetro del planeta = {self.diametro}")
        print(f"Distancia al Sol = {self.distancia_sol}")
        print(f"Tipo de planeta = {self.tipo.value}")
        print(f"Es observable = {self.es_observable}")

    def calcular_densidad(self):
        if self.volumen == 0:
            return None
        return self.masa / self.volumen

    def es_planeta_exterior(self):
        UA = 149_597_870  # km
        limite_exterior = 3.4 * UA
        return self.distancia_sol > limite_exterior

if __name__ == "__main__":
    tierra = Planeta("Tierra", 1, 5.9736e24, 1.08321e12, 12742, 150_000_000, TipoPlaneta.TERRESTRE, True)
    for planeta in [tierra]:
        planeta.imprimir()
        densidad = planeta.calcular_densidad()
        print(f"Densidad del planeta = {densidad:.2f} kg/km³" if densidad else "Densidad no disponible")
        print(f"Es planeta exterior = {planeta.es_planeta_exterior()}")
        print()
