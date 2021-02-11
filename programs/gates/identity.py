"""
Identity gate
"""

import numpy as np


class IdentityGate(object):
    """
    Identity gate
    """

    def __init__(self):
        pass

    @property
    def matrix(self):
        return np.eye(2)

    def __call__(self, qubit):
        return qubit

