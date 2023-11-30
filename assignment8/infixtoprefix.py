def infix_to_prefix(expression):
    # Helper function to determine the precedence of operators
    def precedence(operator):
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/':
            return 2
        else:
            return 0  # For parentheses

    # Helper function to check if a character is an operator
    def is_operator(char):
        return char in ['+', '-', '*', '/']

    # Step 1: Reverse the infix expression
    reversed_expression = expression[::-1]

    # Step 2: Replace '(' with ')' and vice versa
    reversed_expression = reversed_expression.replace('(', 'temp').replace(')', '(').replace('temp', ')')

    # Step 3: Convert the reversed infix expression to postfix using a stack
    stack = []
    postfix = ""
    for char in reversed_expression:
        if char.isalnum():  # Operand
            postfix += char
        elif char == ')':
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':
                postfix += stack.pop()
            stack.pop()  # Remove '(' from the stack
        elif is_operator(char):
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix += stack.pop()
            stack.append(char)

    while stack:
        postfix += stack.pop()

    # Step 4: Reverse the postfix expression to get the prefix expression
    prefix = postfix[::-1]
    return prefix


# Example: Convert infix expression A+B*C+D to prefix
infix_expression = "A+B*C+D"
prefix_expression = infix_to_prefix(infix_expression)
print("Infix Expression:", infix_expression)
print("Prefix Expression:", prefix_expression)
