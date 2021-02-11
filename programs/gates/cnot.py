
import numpy as np


class CNOTGate(object):
    """
    CNOT or controlled NOT gate
    """

    def __init__(self):
        pass

    @property
    def matrix(self):
        return np.array([[1.0, 0.0, 0.0, 0.0],
                         [0.0, 1.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 1.0],
                         [0.0, 0.0, 1.0, 0.0]])

    def __call__(self, qubit1, qubit2):
        raise NotImplementedError("Gate not implemented yet")
