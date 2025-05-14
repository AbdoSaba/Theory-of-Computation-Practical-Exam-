class NFAtoDFA:
    def __init__(self, nfa, start_state, accept_states, alphabet):
        """Initialize the NFA to DFA converter with the NFA structure"""
        self.nfa = nfa 
        self.start_state = start_state  # Start NFA
        self.accept_states = set(accept_states)  
        self.alphabet = [a for a in alphabet if a != 'ε']  # exclude epsilon
        self.dfa_states = [] 
        self.dfa_transitions = {}  
        self.dfa_accept_states = set()  

    def epsilon_closure(self, states):
        """compute the epsilon-closure for a given set of states"""
        stack = list(states)
        closure = set(states)
        while stack:
            state = stack.pop()
            for nxt in self.nfa.get(state, {}).get('ε', []):
                if nxt not in closure:
                    closure.add(nxt)
                    stack.append(nxt)
        return frozenset(closure)

    def move(self, states, symbol):
        """Return the set of states reachable from input states using the symbol"""
        result = set()
        for state in states:
            for nxt in self.nfa.get(state, {}).get(symbol, []):
                result.add(nxt)
        return result

    def convert(self):
        """Convert the NFA to a DFA using subset construction algorithm"""
        start = self.epsilon_closure({self.start_state})
        self.dfa_states.append(start)
        unmarked = [start]  

        while unmarked:
            current = unmarked.pop()
            for symbol in self.alphabet:
                moved = self.move(current, symbol)  
                closure = self.epsilon_closure(moved) 
                if not closure:
                    continue
                if closure not in self.dfa_states:
                    self.dfa_states.append(closure)
                    unmarked.append(closure)
                self.dfa_transitions[(current, symbol)] = closure  

        """Mark DFA accept states if any subset contains an NFA accept state"""
        for state in self.dfa_states:
            if state & self.accept_states:
                self.dfa_accept_states.add(state)

        return {
            'states': self.dfa_states,
            'transitions': self.dfa_transitions,
            'start': start,
            'accept': self.dfa_accept_states
        }

"""Example usage to test the conversion"""
if __name__ == "__main__":
    nfa = {
        'q0': {'ε': ['q1']},
        'q1': {'a': ['q1'], 'b': ['q2']},
        'q2': {}
    }
    start = 'q0'
    accept = ['q2']
    alphabet = ['a', 'b', 'ε']

    converter = NFAtoDFA(nfa, start, accept, alphabet)
    dfa = converter.convert()
    # Print the DFA structure
    print("DFA States:")
    for s in dfa['states']:
        print(set(s))
        
    # Print the DFA start state
    print("DFA Accept States:")
    for s in dfa['accept']:
        print(set(s))
        
    # Print the DFA transitions
    print("DFA Transitions:")
    for (src, sym), dst in dfa['transitions'].items():
        print(f"{set(src)} --{sym}--> {set(dst)}")
