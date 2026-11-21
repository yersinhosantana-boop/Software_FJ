from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, nombre, tarifa):

        if tarifa <= 0:
            raise ValueError("La tarifa debe ser mayor a cero")

        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def calcular_costo(self):
        pass

    def calcular_total(
        self,
        costo_base,
        impuesto=0,
        descuento=0
    ):

        total = costo_base

        total += costo_base * (impuesto / 100)

        total -= costo_base * (descuento / 100)

        return total       
    


class ReservaSala(Servicio):

    def __init__(self, horas, tarifa):

        super().__init__("Reserva de Sala", tarifa)
        self.horas = horas

    def calcular_costo(self):
        return self.horas * self.tarifa


class AlquilerEquipo(Servicio):

    def __init__(self, cantidad, dias, tarifa):

        super().__init__("Alquiler de Equipo", tarifa)

        self.cantidad = cantidad
        self.dias = dias

    def calcular_costo(self):
        return self.cantidad * self.dias * self.tarifa


class Asesoria(Servicio):

    def __init__(self, horas, tarifa):

        super().__init__("Asesoría", tarifa)

        self.horas = horas

    def calcular_costo(self):
        return self.horas * self.tarifa