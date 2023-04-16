# ibm-quantum-gate-programs
IBM Quantum Programs (Running)


The provided code is already written in Qiskit, which is a quantum computing framework developed by IBM. The code demonstrates how to create a custom unitary gate using a predefined unitary matrix U, apply the custom gate to a quantum circuit with two qubits, and then measure the qubits. The measurement outcomes are then visualized using a histogram.

Since the code is already in Qiskit, there is no need to convert it to Qiskit. However, I can provide a brief explanation of the code:

The code starts by importing the necessary modules from Qiskit and NumPy.

A unitary matrix U is defined, representing the custom gate. The matrix is parameterized by an angle theta, which is set to π/4.

The custom gate is created using the UnitaryGate class from Qiskit, and the gate is labeled as "Custom Gate."

A quantum circuit qc with two qubits is created.

The custom gate is applied to both qubits in the circuit using the append method.

Measurements are added to both qubits using the measure_all method.

The circuit is printed for visualization.

The Qiskit Aer simulator is used to simulate the circuit. The circuit is transpiled and run on the simulator, and the measurement outcomes are obtained.

The measurement outcomes (counts) are visualized using the plot_histogram function.

The code is a complete example of how to create and simulate a quantum circuit with a custom gate in Qiskit.


![image](https://user-images.githubusercontent.com/34530588/232253933-9cdc1f01-73e6-4a90-b6a6-837597d9b9e9.png)

![image](https://user-images.githubusercontent.com/34530588/232262508-d0fc587b-e215-4c84-8baa-195a4ca1be75.png)

![image](https://user-images.githubusercontent.com/34530588/232262517-0d069757-34eb-47f2-b59e-6eba945bcbac.png)

![image](https://user-images.githubusercontent.com/34530588/232262524-670d4a7e-2681-4e84-ad63-61b8dba97c4c.png)

![image](https://user-images.githubusercontent.com/34530588/232262540-49eac186-948a-47b8-9157-28dd25bd943a.png)
