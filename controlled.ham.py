# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, transpile
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from ibm_quantum_widgets import *
from qiskit_aer import AerSimulator

# qiskit-ibmq-provider has been deprecated.
# Please see the Migration Guides in https://ibm.biz/provider_migration_guide for more detail.
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Estimator, Session, Options

# Loading your IBM Quantum account(s)
service = QiskitRuntimeService(channel="ibm_quantum")


def create_mcx_gate(num_control_qubits):
    # The total number of qubits is the number of control qubits plus one target qubit
    num_qubits = num_control_qubits + 1
    
    # Create a quantum circuit with the specified number of qubits
    qc = QuantumCircuit(num_qubits)
    
    # Define the control qubits as all qubits except the last one
    control_qubits = list(range(num_control_qubits))
    
    # Define the target qubit as the last qubit
    target_qubit = num_control_qubits
    
    # Apply the multi-controlled X gate
    qc.mct(control_qubits, target_qubit)
    
    return qc

# Example usage: create a multi-controlled X gate with 3 control qubits
num_control_qubits = 3
mcx_gate = create_mcx_gate(num_control_qubits)

# Draw the circuit
mcx_gate.draw('mpl')
