#  Theory of Computation Practical Exam 

## Name: Abdulrahman Nashat Elsayed Abu Saba Elesawy
## Section: <Section : 4 >

### Tasks Implemented:
1. NFA (with ε-transitions) to DFA converter
2. Turing Machine simulator for unary addition
3. CFG ambiguity checker (detect if a string has multiple parse trees)

---

### How does each project work :

#### 1. NFA to DFA
[nfa_to_dfa+converter.py
](url)

##### How it works:

1. **Epsilon-Closure Calculation**  
   For any set of NFA states, the epsilon-closure is computed by finding all states reachable through ε-transitions. This forms the basis for DFA states.

2. **Subset Construction**  
   - The start state of the DFA is the epsilon-closure of the NFA start state.  
   - For each DFA state (which is a set of NFA states), and for each input symbol (excluding ε), the algorithm computes the set of reachable NFA states by:  
     a) Moving on the input symbol from all states in the DFA state.  
     b) Taking the epsilon-closure of the resulting states.  
   - This new set forms a new DFA state if it hasn’t been processed before.  
   - Transitions are recorded from the current DFA state to the new DFA state on the input symbol.

3. **Accept States**  
   Any DFA state that contains at least one NFA accept state is marked as an accept state.

##### Data Structures:

- The NFA is represented as a dictionary mapping each state to its transitions, where transitions are dictionaries from symbols (including 'ε') to lists of next states.
- DFA states are represented as frozensets of NFA states.
- DFA transitions are stored in a dictionary keyed by (DFA state, input symbol).

##### Summary:

The program systematically explores reachable subsets of NFA states, building the DFA states and transitions on-the-fly, ensuring only reachable states are included. This approach efficiently converts an NFA with ε-transitions into a minimal equivalent DFA.
