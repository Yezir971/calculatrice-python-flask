class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def evaluate(self):
        if isinstance(self.value, (int, float)):
            return self.value
        
        left_val = self.left.evaluate()
        right_val = self.right.evaluate()
        
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b if b != 0 else float('inf')
        }
        return ops[self.value](left_val, right_val)