from excepciones import ReservaError


class Reserva:

    def __init__(self, cliente, servicio):

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):

        if self.estado == "Cancelada":
            raise ReservaError(
                "No se puede procesar una reserva cancelada"
            )

        return self.servicio.calcular_costo()