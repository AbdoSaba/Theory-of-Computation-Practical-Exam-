#  Theory of Computation Practical Exam 

## Name: Abdulrahman Nashat Elsayed Abu Saba Elesawy
## Section: < 4 >

### Tasks Implemented:
1. Write a Python function that converts a given NFA (with e-transitions) to an equivalent DFA using the subset construction algorithm.
2. Write a program that takes a CFG and checks if a given string has more than one parse tree, indicating that the grammar is ambiguous for that string.
3. Simulate a Turing Machine that computes the sum of two unary numbers separated by a +. **Example** input: 111+11 Output: 11111.

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

#### 2. Turing Machine Simulator
[python turing_machine/machine.py
](url)
##### How it works:

1. **Tape and Head**  
   The tape is represented as a list of symbols (characters), initially containing the input string plus extra blank symbols (`'_'`) to allow movement.  
   The head is an index pointing to the current tape cell being read or written.

2. **States and Transitions**  
   The machine has a finite set of states (`q0`, `q1`, `q2`, and `halt`), and transitions define how the machine moves between states based on the current symbol under the head.  
   For example, in state `q0`, the machine moves right over `'1'` symbols until it finds `'+'`, which it erases and switches to state `q1`.

3. **Operation**  
   - In `q0`, the machine scans the first unary number until it finds the plus sign.  
   - In `q1`, it moves right over the second unary number until it reaches a blank, then writes a `'1'` to extend the first number (effectively adding).  
   - In `q2`, the machine moves left to the start and then halts.

4. **Halting**  
   The machine halts when it reaches the `halt` state, and the tape content represents the sum of the two unary numbers.

##### Summary:

This implementation manually simulates the Turing Machine’s tape, head movement, state transitions, and symbol rewriting without using external libraries. It illustrates the fundamental principles of Turing Machines and how they compute by reading and writing symbols on an infinite tape.

