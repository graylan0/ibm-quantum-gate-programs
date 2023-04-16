from qiskit import QuantumCircuit

# Create a quantum circuit with 5 qubits (2 control qubits, 1 target qubit, 2 ancilla qubits)
qc = QuantumCircuit(5)

# Define the control qubits, target qubit, and ancilla qubits
control1 = 0
control2 = 1
target = 2
ancilla1 = 3
ancilla2 = 4

# Toffoli gate decomposition
qc.cx(control2, ancilla1)
qc.tdg(ancilla1)
qc.cx(control1, ancilla1)
qc.t(ancilla1)
qc.cx(control2, ancilla1)
qc.tdg(ancilla1)
qc.cx(control1, ancilla1)
qc.cx(control1, control2)
qc.tdg(control2)
qc.cx(control1, control2)
qc.t(control1)
qc.s(control2)

# Custom controlled-controlled-Y gate
qc.sdg(ancilla2)
qc.cx(control2, ancilla2)
qc.s(ancilla2)
qc.cx(control1, ancilla2)
qc.tdg(ancilla2)
qc.cx(control2, ancilla2)
qc.t(ancilla2)
qc.cx(control1, ancilla2)
qc.s(ancilla2)
qc.t(control2)

# Draw the custom controlled-controlled-Y gate circuit
qc.draw()
