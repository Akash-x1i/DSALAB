def infix_to_postfix(expression):
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

    # Convert infix expression to postfix using a stack
    stack = []
    postfix = ""
    for char in expression:
        if char.isalnum():  # Operand
            postfix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  # Remove '(' from the stack
        elif is_operator(char):
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix += stack.pop()
            stack.append(char)

    while stack:
        postfix += stack.pop()

    return postfix

# Example: Convert infix expression A+B*C+D to postfix
infix_expression = "A+B*C+D"
postfix_expression = infix_to_postfix(infix_expression)
print("Infix Expression:", infix_expression)
print("Postfix Expression:", postfix_expression)
