class GestorSistema:

    def __init__(self):

        self.clientes = []
        self.servicios = []
        self.reservas = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)

    def mostrar_clientes(self):

        print("\nCLIENTES REGISTRADOS")

        for cliente in self.clientes:
            print(cliente.descripcion())

    def mostrar_servicios(self):

        print("\nSERVICIOS REGISTRADOS")

        for servicio in self.servicios:
            print(servicio.nombre)

    def mostrar_reservas(self):

        print("\nRESERVAS REGISTRADAS")

        for reserva in self.reservas:
            print(
                reserva.cliente.descripcion(),
                "-",
                reserva.estado
            )