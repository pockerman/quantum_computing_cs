import numpy as np
from numpy import linalg as LA


class QSimulator(object):

    @staticmethod
    def bra(ket):
        """
        Computes the bra corresponding to the ket
        """

        return np.array([np.conjugate(item) for item in ket])
        # return np.conjugate(ket)

    def __init__(self, state_vector):
        """
        Constructor initialize with the initial state vector
        """
        self._state_vector = state_vector

    @property
    def state(self):
        """
        Returns the current state vector
        """
        return self._state_vector

    def position_probability(self, position_idx):
        """
        Returns the propbability that the particle
        is at the specified position index. This is simply the
        norm square of the correpsonding applitude divided by the 
        norm squared of the state vector
        """

        nominator = np.abs(self._state_vector[position_idx]) ** 2
        denominator = LA.norm(self._state_vector) ** 2

        return nominator / denominator

    def transition_amplitude(self, new_state):
        """
        Returns the transition applitude from 
        self._state_vector to new_state
        """

        # first compute the bra of the corresponding ending state
        bra = QSimulator.bra(ket=new_state)

        # take the dot product of the bra with the 
        # current state
        dot_product = np.dot(bra, self._state_vector)

        return dot_product

    def transition_probability(self, new_state):
        """
        Returns the propbability that the particle
        transitions to the new_state after an observation has been made.
        This is simply the absolute value of the transition amplitude
        squared see section 4.1 page 113 
        """

        amplitude = self.transition_amplitude(new_state=new_state)

        return np.abs(amplitude) ** 2

    def transition(self, u):
        """
        Given the unitary matrix propagate the state
        of the particle
        """
        self._state_vector = np.dot(u, self._state_vector)
