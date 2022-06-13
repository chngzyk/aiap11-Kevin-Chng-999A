import logging


def main():

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info("Running machine learning pipeline")


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
