import logging


logging.basicConfig(
    filename="logs/software_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def registrar_evento(mensaje):
    logging.info(mensaje)


def registrar_error(mensaje):
    logging.error(mensaje)