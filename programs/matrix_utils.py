"""
Matrix utilities to solve exercises
"""

import numpy as np


def is_unitary_matrix_complex(matrix):
    I = np.identity(matrix.shape[0])
    u_T = matrix.T.conj()

    return np.allclose(I, np.dot(u_T, matrix)) and np.allclose(I, np.dot(matrix, u_T))


def is_unitary_matrix(matrix):

    I = np.identity(matrix.shape[0])
    u_T = matrix.T

    return np.allclose(I, np.dot(u_T, matrix)) and np.allclose(I, np.dot(matrix, u_T))
