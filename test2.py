# -*- coding: utf-8 -*-
# time: 2023/10/2 12:10
# file: test2.py
# author: Felix_Zhang
# email: yuqizhang247@gmail.com

from z3 import *

def token_swapping_solver(AG, C):
    n = max(max(e) for e in AG) + 1
    total_steps = 2*len(C)  # Assuming worst case where each CNOT requires a SWAP before it

    s = Solver()

    # Mapping for each time step and each qubit
    tau = [[Int(f'tau_{i}_{j}') for j in range(n)] for i in range(total_steps)]

    # Initial mapping is identity
    for j in range(n):
        s.add(tau[0][j] == j)

    for t in range(0, total_steps, 2):
        # Looping with a stride of 2 since we are accounting for potential SWAP before each CNOT
        a, b = C[t // 2]  # Fetch the CNOT gate for this time step

        # Check if CNOT can be executed directly
        direct_execution = Or(And(tau[t][a] == tau[t+1][a], tau[t][b] == tau[t+1][b]), And(tau[t][a] == tau[t+1][b], tau[t][b] == tau[t+1][a]))

        # Add constraints for possible SWAP
        for (x, y) in AG:
            possible_swap = And(tau[t][x] == tau[t+1][y], tau[t][y] == tau[t+1][x])
            s.add(Or(direct_execution, possible_swap))

            for j in range(n):
                # All other qubits, except the swapped or executed ones, should remain in their positions
                s.add(Implies(And(j != x, j != y), tau[t][j] == tau[t+1][j]))

    if s.check() == sat:
        m = s.model()
        return [[m.evaluate(tau[i][j]).as_long() for j in range(n)] for i in range(total_steps)]
    return None


# def token_swapping_solver(AG, C ,k_max):
#     # AG is a list of edges in the architecture graph.
#     # C is a list of edges representing the CNOT gates in the circuit.
#     n = max(max(e) for e in AG) + 1  # Number of qubits, assuming qubits are labeled from 0 to n-1
#     k = 0
#
#     while k <= k_max:
#
#         s = Solver()
#
#         # Define the mapping variables for each step and each qubit
#         tau = [[Int(f'tau_{i}_{j}') for j in range(n)] for i in range(k+1)]
#
#         # Initial and final mapping constraints
#         for j in range(n):
#             s.add(tau[0][j] == j)  # initial mapping is identity
#
#         for i in range(k):
#             for a, b in AG:
#                 # If a and b are swapped
#                 swapped = And(tau[i][a] == tau[i + 1][b], tau[i][b] == tau[i + 1][a])
#                 # If a and b are not swapped
#                 not_swapped = And(tau[i][a] == tau[i + 1][a], tau[i][b] == tau[i + 1][b])
#                 s.add(Or(swapped, not_swapped))
#
#                 # Ensure that all other qubits, except a and b, remain in their positions
#                 for j in range(n):
#                     s.add(Implies(And(j != a, j != b), tau[i][j] == tau[i + 1][j]))
#
#         # Gate constraints for CNOT gates in the circuit
#         for a, b in C:
#             s.add(Or([And(tau[k][a] == x, tau[k][b] == y) for x, y in AG]))
#
#         for i in range(k + 1):
#             for j in range(n):
#                 for l in range(j + 1, n):
#                     s.add(tau[i][j] != tau[i][l])
#
#         if s.check() == sat:
#             m = s.model()
#             return [[m.evaluate(tau[i][j]).as_long() for j in range(n)] for i in range(k+1)]
#
#         k += 1
#
#     return None

def extract_swaps(mapping_sequence):
    swaps = []
    for i in range(1, len(mapping_sequence)):
        prev_mapping = mapping_sequence[i-1]
        curr_mapping = mapping_sequence[i]
        swapped = [j for j in range(len(prev_mapping)) if prev_mapping[j] != curr_mapping[j]]
        if swapped:
            swaps.append(tuple(swapped))
    return swaps



if __name__ == '__main__':

    AG = [(0,1),(1,2),(2,3),(3,0)]
    C = [(0,1),(1,2),(3,0)]

    solution = token_swapping_solver(AG, C )

    # if solution:
    swaps = extract_swaps(solution)
    print("Initial Mapping:", solution[0])
    print("SWAP operations:")
    for swap in swaps:
        print(swap)
    # else:
    #     print("No solution found within the given k_max.")
