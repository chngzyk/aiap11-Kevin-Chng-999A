import logging

from src.data_processing import DataProcessing


def main():

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info("Running machine learning pipeline")

    data_processor = DataProcessing()
    data_processor.clean_data()


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
