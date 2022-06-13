import os
import logging

import sqlite3
import urllib.request
import pandas as pd


class DataProcessing:
    def __init__(self) -> None:

        self.logger = logging.getLogger(__name__)

        url = "https://techassessment.blob.core.windows.net/aiap11-assessment-data/noshow.db"
        name = "noshow.db"

        if os.path.isfile(name):
            os.remove(name)

        urllib.request.urlretrieve(url, name)  # download

        cnx = sqlite3.connect(name)
        cursor = cnx.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        table_name = cursor.fetchall()[0]

        self.df = pd.read_sql_query("SELECT * FROM noshow", cnx)

        self.logger.info(f"Size of dataframe: {self.df.shape[0]}")

    def clean_data(self):

        self.df.dropna(inplace=True)

