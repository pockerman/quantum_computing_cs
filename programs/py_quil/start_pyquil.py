#!/usr/bin/env python
# coding: utf-8

# # Deutch's Algorithm

# In[1]:


from pyquil import get_qc, Program
from pyquil.gates import CNOT, H 
import pyquil.api as api 
from pyquil.api import local_forest_runtime





if __name__ == '__main__':
	
	p = Program(H(0), CNOT(0, 1))

	with local_forest_runtime():
		qvm = api.QVMConnection(random_seed=42)
		
		result = qvm.run_and_measure(p, qubits=[0, 1], trials=10)
		print(result[0])
		print(result[1])
	



