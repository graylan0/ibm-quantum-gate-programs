import qiskit
from qiskit import QuantumCircuit, Aer
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.extensions import UnitaryGate
import numpy as np

# Define the quantum circuit
qc = QuantumCircuit(3)

# Dr. Alexander Kim's CPHASE gate
phi = np.pi / 3  # Example phase angle
cphase_matrix = np.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, np.exp(1j * phi)]])
cphase_gate = UnitaryGate(cphase_matrix, label="CPHASE")
qc.append(cphase_gate, [0, 1])

# Dr. Sophia Patel's T-gate
qc.t(0)

# Dr. Michael Osei's Toffoli gate (CCNOT gate)
qc.ccx(0, 1, 2)

# Dr. Emma Nakamura's Hadamard gate
qc.h(0)

# Dr. Benjamin Singh's Pauli-X gate
qc.x(0)

# Dr. Olivia Kone's CNOT gate
qc.cx(0, 1)

# Draw the quantum circuit
qc.draw()

# Simulate the quantum circuit
simulator = Aer.get_backend('statevector_simulator')
result = simulator.run(qc).result()  # Directly pass the quantum circuit to the run method
statevector = result.get_statevector()

# Visualize the statevector on the Bloch sphere
plot_bloch_multivector(statevector)
