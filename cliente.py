import re
from entidades import Entidad
from excepciones import DatosInvalidosError


class Cliente(Entidad):

    def __init__(self, identificador, nombre, correo, telefono):

        super().__init__(identificador)

        if len(nombre.strip()) < 3:
            raise DatosInvalidosError("Nombre inválido")

        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            raise DatosInvalidosError("Correo inválido")

        if not telefono.isdigit():
            raise DatosInvalidosError("Teléfono inválido")

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    def descripcion(self):
        return f"Cliente: {self.__nombre}"
print("\nPRUEBA SEGUNDO CLIENTE")

try:

    cliente2 = Cliente(
        5,
        "Maria Lopez",
        "maria@gmail.com",
        "3201234567"
    )

    print(cliente2.descripcion())

except Exception as e:

    print(e)
    