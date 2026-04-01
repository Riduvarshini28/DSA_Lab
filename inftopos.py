#infix to postfix

def prec(op):
    if op in "+-": return 1
    if op in "*/": return 2
    return 0

def infix_to_postfix(exp):
    stack = []
    res = ""

    for ch in exp:
        if ch.isalnum():
            res += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack[-1] != '(':
                res += stack.pop()
            stack.pop()
        else:
            while stack and prec(ch) <= prec(stack[-1]):
                res += stack.pop()
            stack.append(ch)

    while stack:
        res += stack.pop()

    return res

# Function Call
print(infix_to_postfix("A+B*C"))
