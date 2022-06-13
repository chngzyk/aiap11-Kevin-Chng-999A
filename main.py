import logging

from src.data_processing import data_processing


def main():

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info("Running machine learning pipeline")

    data_processor = data_processing()


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
