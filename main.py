from etl.extract import extract_campaign_data
from etl.transform import transform_campaign_data
from etl.load import load_campaign_data
from database.connection import get_database_connection
from utils.logger import setup_logger


def run_pipeline():
    logger = setup_logger()

    try:
        logger.info("Iniciando pipeline")

        df = extract_campaign_data()
        logger.info("Dados extraídos")

        df = transform_campaign_data(df)
        logger.info("Dados transformados")

        connection = get_database_connection()

        load_campaign_data(df, connection)
        connection.close()

        logger.info("Dados carregados no banco e CSV")

        print("Pipeline executado com sucesso")
        print(df)

    except Exception as e:
        logger.error(f"Erro no pipeline: {e}")
        print("Erro ao executar pipeline:", e)


if __name__ == "__main__":
    run_pipeline()