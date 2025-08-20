class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_postfix(expression):
    stack = Stack()
    postfix = []
    tokens = tokenize(expression)

    for token in tokens:
        if token.isnumeric() or is_float(token):
            postfix.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while (not stack.is_empty() and
                   precedence(token) <= precedence(stack.peek())):
                postfix.append(stack.pop())
            stack.push(token)

    while not stack.is_empty():
        postfix.append(stack.pop())

    return postfix

def evaluate_postfix(postfix):
    stack = Stack()
    for token in postfix:
        if token.isnumeric() or is_float(token):
            stack.push(float(token))
        else:
            right = stack.pop()
            left = stack.pop()
            result = apply_operator(left, right, token)
            stack.push(result)
    return stack.pop()

def apply_operator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    elif op == '^':
        return a ** b
    else:
        raise ValueError(f"Unknown operator {op}")

def tokenize(expression):
    tokens = []
    value = ''
    for ch in expression:
        if ch.isdigit() or ch == '.':
            value += ch
        else:
            if value != '':
                tokens.append(value)
                value = ''
            if ch.strip():
                tokens.append(ch)
    if value != '':
        tokens.append(value)
    return tokens

def is_float(string):
    try:
        float(string)
        return True
    except:
        return False

if __name__ == "__main__":
    expr = input("Enter infix expression: ")
    postfix_expr = infix_to_postfix(expr)
    print("Postfix expression:", ' '.join(postfix_expr))
    result = evaluate_postfix(postfix_expr)
    print("Evaluation result:", result)
