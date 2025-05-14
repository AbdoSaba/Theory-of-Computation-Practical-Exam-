class TuringMachine:
    def __init__(self, tape):
        """Initialize the Turing Machine with the input tape"""
        self.tape = list(tape) + ['_'] * 10  # Extend tape with symbols
        self.head = 0  # Head start 
        self.state = 'q0'  # Initial state

    def step(self):
        """perform one step of the Turing Machine"""
        symbol = self.tape[self.head]  # Read symbol under head

        if self.state == 'q0':
            """state q0: move right over 1s, look for '+'"""
            if symbol == '1':
                self.head += 1
            elif symbol == '+':
                self.tape[self.head] = '_'  
                self.state = 'q1'  # move to state q1
                self.head += 1
            else:
                self.state = 'halt'  # halt on unexpected symbol

        elif self.state == 'q1':
            """state q1: move right over 1s, stop at blank and add '1'"""
            if symbol == '1':
                self.head += 1
            elif symbol == '_':
                self.tape[self.head] = '1'  # Write new 1
                self.state = 'q2'  # move to state q2
                self.head -= 1
            else:
                self.state = 'halt'  # Halt on invalid symbol

        elif self.state == 'q2':
            """state q2: move left back to the start or halt"""
            if self.tape[self.head] == '1':
                self.head -= 1
            elif self.tape[self.head] == '_':
                self.state = 'halt'  # halt when reaching left end
                self.head += 1
            else:
                self.head -= 1  # keep moving left for other symbols

    def run(self):
        """run the Turing Machine until it halts"""
        while self.state != 'halt':
            self.step()
        """return final tape content without trailing blanks"""
        return ''.join(self.tape).rstrip('_')

# Test the Turing Machine the same in the PDF
# Example: 111 + 11 = 1111


if __name__ == "__main__":
    tm = TuringMachine("111+11")  
    result = tm.run()
    print("Result on tape:", result)  
