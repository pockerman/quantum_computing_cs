import numpy as np


class HadamardGate(object):

    """
    Hadamard gate
    """

    def __init__(self):
        pass

    @property
    def matrix(self):
        return np.array([[1.0/np.sqrt(2.0), 1.0/np.sqrt(2.0)],
                         [1.0/np.sqrt(2.0), -1.0/np.sqrt(2.0)]])

    def __call__(self, qubit):
        return self.matrix.dot(qubit)