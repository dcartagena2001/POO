#%%
from enum import Enum

class TipoCombustible(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    BIODIESEL = "Biodiésel"
    GAS_NATURAL = "Gas Natural"

class TipoAutomovil(Enum):
    CIUDAD = "Ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"

class TipoColor(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"

class Automovil:
    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_auto,
                 num_puertas, asientos, velocidad_max, color):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_auto = tipo_auto
        self.num_puertas = num_puertas
        self.asientos = asientos
        self.velocidad_max = velocidad_max
        self.color = color
        self.velocidad_actual = 0

    def acelerar(self, incremento):
        if self.velocidad_actual + incremento <= self.velocidad_max:
            self.velocidad_actual += incremento
        else:
            print("No se puede superar la velocidad máxima.")

    def desacelerar(self, decremento):
        if self.velocidad_actual - decremento >= 0:
            self.velocidad_actual -= decremento
        else:
            print("No se puede desacelerar a velocidad negativa.")

    def frenar(self):
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia):
        if self.velocidad_actual > 0:
            return distancia / self.velocidad_actual
        else:
            print("La velocidad actual es cero, no se puede calcular el tiempo.")
            return None

    def imprimir(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Motor:", self.motor)
        print("Tipo de combustible:", self.tipo_combustible.value)
        print("Tipo de automóvil:", self.tipo_auto.value)
        print("Número de puertas:", self.num_puertas)
        print("Cantidad de asientos:", self.asientos)
        print("Velocidad máxima:", self.velocidad_max)
        print("Color:", self.color.value)

# --- MAIN ---
if __name__ == "__main__":
    auto1 = Automovil("Ford", 2018, 3, TipoCombustible.DIESEL, TipoAutomovil.EJECUTIVO,
                      5, 6, 250, TipoColor.NEGRO)


    auto1.imprimir()
    auto1.velocidad_actual = 100
    print("Velocidad actual:", auto1.velocidad_actual)

    auto1.acelerar(20)
    print("Velocidad actual:", auto1.velocidad_actual)

    auto1.desacelerar(50)
    print("Velocidad actual:", auto1.velocidad_actual)

    auto1.frenar()
    print("Velocidad actual:", auto1.velocidad_actual)

    auto1.desacelerar(20)