import logging
import os


def setup_logger():
    # Garante que a pasta de logs exista
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Cria um logger nomeado
    logger = logging.getLogger("marketing_pipeline")

    # Evita duplicação de logs (muito importante)
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    # Formato do log
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    # Handler para arquivo
    file_handler = logging.FileHandler("logs/pipeline.log")
    file_handler.setFormatter(formatter)

    # Handler para console (terminal)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Adiciona os handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# 🔥 INSTÂNCIA GLOBAL (ESSENCIAL)
logger = setup_logger()