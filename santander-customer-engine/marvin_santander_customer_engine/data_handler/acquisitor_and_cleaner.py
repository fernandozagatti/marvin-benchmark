#!/usr/bin/env python
# coding=utf-8

"""AcquisitorAndCleaner engine action.

Use this module to add the project main code.
"""

from .._compatibility import six
from .._logging import get_logger

from marvin_python_toolbox.engine_base import EngineBaseDataHandler

__all__ = ['AcquisitorAndCleaner']


logger = get_logger('acquisitor_and_cleaner')


class AcquisitorAndCleaner(EngineBaseDataHandler):

    def __init__(self, **kwargs):
        super(AcquisitorAndCleaner, self).__init__(**kwargs)

    def execute(self, params, **kwargs):
        import marvin_santander_customer_engine
        import pandas as pd
        import os

        path = os.path.join(os.environ["MARVIN_DATA_PATH"], "santander_customer_train.csv")
        train = pd.read_csv(path)

        self.marvin_initial_dataset = train

