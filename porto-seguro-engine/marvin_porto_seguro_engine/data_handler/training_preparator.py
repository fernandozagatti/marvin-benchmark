#!/usr/bin/env python
# coding=utf-8

"""TrainingPreparator engine action.

Use this module to add the project main code.
"""

from .._compatibility import six
from .._logging import get_logger

from marvin_python_toolbox.engine_base import EngineBaseDataHandler

__all__ = ['TrainingPreparator']


logger = get_logger('training_preparator')


class TrainingPreparator(EngineBaseDataHandler):

    def __init__(self, **kwargs):
        super(TrainingPreparator, self).__init__(**kwargs)

    def execute(self, params, **kwargs):
        from sklearn.model_selection import train_test_split

        train, test = train_test_split(self.marvin_initial_dataset, test_size=0.3)

        train_y = train.target
        train_x = train.drop("target", axis=1)

        test_y = test.target
        test_x = test.drop("target", axis=1)

        self.marvin_dataset = {'train_x': train_x, 'train_y': train_y, 'test_x': test_x, 'test_y': test_y}

