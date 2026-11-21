from servicios import Asesoria
from servicios import AlquilerEquipo
from cliente import Cliente
from servicios import ReservaSala
from reserva import Reserva
from gestor import GestorSistema


gestor = GestorSistema()

cliente1 = Cliente(
    1,
    "Yersson Naranjo",
    "correo@gmail.com",
    "3001234567"
)

sala = ReservaSala(3, 50000)

reserva1 = Reserva(cliente1, sala)

reserva1.confirmar()

gestor.agregar_cliente(cliente1)
gestor.agregar_servicio(sala)
gestor.agregar_reserva(reserva1)

gestor.mostrar_clientes()
gestor.mostrar_servicios()
gestor.mostrar_reservas()

print("\nCosto de la reserva:", reserva1.procesar())
from gestor_logs import registrar_evento

registrar_evento("Prueba del sistema Software FJ")

from gestor_logs import registrar_error

try:

    cliente_error = Cliente(
        2,
        "Juan",
        "correo_malo",
        "3001234567"
    )

except Exception as e:

    print("Error detectado:", e)

    registrar_error(
        f"Error al registrar cliente: {e}"
    )

    print("\nPRUEBA TRY - EXCEPT - ELSE")

try:

    cliente2 = Cliente(
        3,
        "Carlos Perez",
        "carlos@gmail.com",
        "3109876543"
    )

except Exception as e:

    print("Error:", e)

else:

    print("Cliente registrado correctamente")

    print("\nPRUEBA TRY - EXCEPT - FINALLY")

try:

    sala_error = ReservaSala(3, -5000)

except Exception as e:

    print("Error detectado:", e)

finally:

    print("Finalizó la validación del servicio")

    print("\nPRUEBA RESERVA CANCELADA")

try:

    reserva_cancelada = Reserva(cliente1, sala)

    reserva_cancelada.cancelar()

    print("Estado:", reserva_cancelada.estado)

    reserva_cancelada.procesar()

except Exception as e:

    print("Error controlado:", e)

    registrar_error(
        f"Error al procesar reserva cancelada: {e}"
    )

    print("\nPRUEBA SOBRECARGA")

costo_base = sala.calcular_costo()

print(
    "Costo normal:",
    sala.calcular_total(costo_base)
)

print(
    "Costo con IVA:",
    sala.calcular_total(costo_base, 19)
)

print(
    "Costo con IVA y descuento:",
    sala.calcular_total(costo_base, 19, 10)
)
print("\nPRUEBA TELEFONO INVALIDO")

try:

    cliente_telefono = Cliente(
        4,
        "Pedro Gomez",
        "pedro@gmail.com",
        "ABC123"
    )

except Exception as e:

    print("Error controlado:", e)

    registrar_error(
        f"Telefono invalido: {e}"
    )
print("\nPRUEBA ALQUILER EQUIPO")

equipo = AlquilerEquipo(
    2,
    3,
    30000
)

print(
    "Costo alquiler:",
    equipo.calcular_costo()
)

print("\nPRUEBA ASESORIA")

asesoria = Asesoria(
    4,
    80000
)

print(
    "Costo asesoria:",
    asesoria.calcular_costo()
)
