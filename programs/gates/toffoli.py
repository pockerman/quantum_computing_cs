import numpy as np


class ToffoliGate(object):
    """
    Toffoli gate
    """

    def __init__(self):
        pass

    @property
    def matrix(self):
        return np.array([[1.0, 0.0, 0.0, 0.0, 0., 0., 0., 0.],
                         [0.0, 1.0, 0.0, 0.0, 0., 0., 0., 0.],
                         [0.0, 0.0, 1.0, 0.0, 0., 0., 0., 0.],
                         [0.0, 0.0, 0.0, 1.0, 0., 0., 0., 0.],
                         [0.0, 0.0, 0.0, 0.0, 1.0, 0., 0., 0.],
                         [0.0, 0.0, 0.0, 0.0, 0., 1.0, 0., 0.],
                         [0.0, 0.0, 0.0, 0.0, 0., 0., 0., 1.0],
                         [0.0, 0.0, 0.0, 0.0, 0., 0., 1.0, 0.]
                         ])

    def __call__(self, qubit):
        raise NotImplementedError("Gate application not implemented")
