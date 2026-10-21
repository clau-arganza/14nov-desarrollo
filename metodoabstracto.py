from abc import ABC, abstractmethod

class MandoDistancia(ABC):
    def __init__(self):
        self.encendido = False

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    def cambiar_estado(self):
        if self.encendido:
            self.apagar()
        else:
            self.encender()


class TV(MandoDistancia):
    def __init__(self):
        super().__init__()
        self.canal = 1

    def encender(self):
        self.encendido = True
        print("TV encendida.")

    def apagar(self):
        self.encendido = False
        print("TV apagada.")

    def cambiar_canal(self, canal):
        self.canal = canal
        print(f"Canal cambiado al {self.canal}.")


class ReproductorMusica(MandoDistancia):
    def __init__(self):
        super().__init__()
        self.pista = 1

    def encender(self):
        self.encendido = True
        print("Reproductor de música encendido.")

    def apagar(self):
        self.encendido = False
        print("Reproductor de música apagado.")

    def cambiar_pista(self, pista):
        self.pista = pista
        print(f"Reproduciendo la pista {self.pista}.")


class Luces(MandoDistancia):
    def __init__(self):
        super().__init__()
        self.intensidad = 50

    def encender(self):
        self.encendido = True
        print("Luces encendidas.")

    def apagar(self):
        self.encendido = False
        print("Luces apagadas.")

    def ajustar_intensidad(self, intensidad):
        if not 0 <= intensidad <= 100:
            raise ValueError("La intensidad debe estar entre 0 y 100.")
        self.intensidad = intensidad
        print(f"Intensidad ajustada al {self.intensidad}%.")


class ControlTemperatura(MandoDistancia):
    def __init__(self):
        super().__init__()
        self.temperatura = 20

    def encender(self):
        self.encendido = True
        print("Control de temperatura encendido.")

    def apagar(self):
        self.encendido = False
        print("Control de temperatura apagado.")

    def ajustar_temperatura(self, temperatura):
        self.temperatura = temperatura
        print(f"Temperatura ajustada a {self.temperatura}°C.")


class Rumba(MandoDistancia):
    def __init__(self):
        super().__init__()
        self.modo = "automatico"

    def encender(self):
        self.encendido = True
        print("Rumba empieza a limpiar.")

    def apagar(self):
        self.encendido = False
        print("Rumba se detiene.")

    def cambiar_modo(self, modo):
        self.modo = modo
        print(f"Modo de limpieza cambiado a {self.modo}.")


televisor = TV()
televisor.cambiar_estado()
televisor.cambiar_canal(5)
televisor.cambiar_estado()

rumba = Rumba()
rumba.cambiar_estado()
rumba.cambiar_estado()