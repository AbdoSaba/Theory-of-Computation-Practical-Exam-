class CFGAmbiguityChecker:
    def __init__(self, grammar, start_symbol):
        """Initialize the class with the grammar and start symbol"""
        self.grammar = grammar  # dictionary: Non-terminal -> list of productions
        self.start = start_symbol  # starting symbol of the grammar
        self.memo = {}  # memoization for parsed results

    def parse(self, symbol, string):
        """
        Returns all possible parse trees for a given string starting from a symbol.
        Each parse tree is represented as a tuple: (symbol, [children])
        """
        key = (symbol, string)
        if key in self.memo:
            """Return cached result if available"""
            return self.memo[key]

        results = []

        """If symbol is terminal, check for direct match with string"""
        if symbol not in self.grammar:
            if symbol == string:
                results.append((symbol, []))
            self.memo[key] = results
            return results

        """Try each production rule for the current non-terminal"""
        for prod in self.grammar[symbol]:
            """Handle epsilon (empty string) production"""
            if prod == ['ε']:
                if string == '':
                    results.append((symbol, []))
                continue

            """Try all ways to split string according to production symbols"""
            def backtrack(parts, s):
                if not parts:
                    """If no parts left, check if string is also empty"""
                    return [[]] if s == '' else []
                first, *rest = parts
                trees = []
                for i in range(len(s)+1):
                    left = s[:i]
                    right = s[i:]
                    left_trees = self.parse(first, left)
                    if left_trees:
                        rest_trees = backtrack(rest, right)
                        for lt in left_trees:
                            for rt in rest_trees:
                                trees.append([lt] + rt)
                return trees

            subtrees = backtrack(prod, string)
            for st in subtrees:
                results.append((symbol, st))

        """Save results to memo and return"""
        self.memo[key] = results
        return results

    def is_ambiguous(self, string):
        """Check if the string has more than one parse tree"""
        trees = self.parse(self.start, string)
        return len(trees) > 1


"""Example usage"""
if __name__ == "__main__":
    grammar = {
        'E': [['E', '+', 'E'], ['E', '*', 'E'], ['(', 'E', ')'], ['id']],
    }
    checker = CFGAmbiguityChecker(grammar, 'E')
    test_str = 'id+id*id'

    ambiguous = checker.is_ambiguous(test_str)
    print(f"Is '{test_str}' ambiguous? {ambiguous}")
