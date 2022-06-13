import logging

import numpy as np

from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score


class Model:
    def __init__(self, data) -> None:
        self.data = data

        self.logger = logging.getLogger(__name__)

    def build_model(self):
        at_columns_name = [
            "branch",
            "booking_month",
            "arrival_month",
            "checkout_month",
            "country",
            "room",
            "platform",
            "price",
            "no_show",
        ]

        drop_columns_name = ["price", "no_show"]

        X = self.data.drop(at_columns_name, axis=1)
        y = self.data["no_show"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=2, stratify=y
        )

        enc = OneHotEncoder(handle_unknown="ignore")
        enc.fit(X_train)

        X_encoded_train = enc.transform(X_train).toarray()
        X_encoded_test = enc.transform(X_test).toarray()

        clf = RandomForestClassifier(max_depth=5, random_state=0)
        clf.fit(X_encoded_train, y_train)
        y_pred = clf.predict(X_encoded_test)

        self.logger.info(f1_score(y_test, y_pred, average="macro"))
        self.logger.info(precision_score(y_test, y_pred, average="macro"))
        self.logger.info(recall_score(y_test, y_pred, average="macro"))

        unique, counts = np.unique(y_pred, return_counts=True)

        result = np.column_stack((unique, counts))
        self.logger.info(result)

