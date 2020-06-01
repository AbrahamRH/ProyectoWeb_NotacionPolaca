"""
Para este program Infijo, postfijo, and prefijo conversión de expresiones
Por ejemplo:
Infijo: 1 * (2 + 3) / 4
Postfijo: 1 2 3 + * 4 /
Prefijo: / * 1 + 2 3 4

"""

from __future__ import division
import eel
eel.init('web')



OPERATORS = set(['+', '-', '*', '¬', '/','^', '(', ')'])
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


# INFIJO ===> POSTFIJO





def infix_to_postfix(formula):
    stack = []
    global output
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()
            stack.append(ch)

    while stack: output += stack.pop()
    print(output)
    return output

# INFIJO ===> PREFIJO

def infix_to_prefix(formula):
    op_stack = []
    global exp_stack
    exp_stack = []
    for ch in formula:
        if not ch in OPERATORS:
            exp_stack.append(ch)
        elif ch == '(':
            op_stack.append(ch)
        elif ch == ')':
            while op_stack[-1] != '(':
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append(op + b + a)
            op_stack.pop()
        else:
            while op_stack and op_stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[op_stack[-1]]:
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append(op + b + a)
            op_stack.append(ch)


    while op_stack:
        op = op_stack.pop()
        a = exp_stack.pop()
        b = exp_stack.pop()
        exp_stack.append(op + b + a)
    print(exp_stack[-1])
    return exp_stack[-1]



@eel.expose
def Postfija(data):
     infix_to_postfix(data)
     eel.callbackPosfija(output)

@eel.expose
def Prefija(data):
     infix_to_prefix(data)
     eel.callbackPrefija(exp_stack[-1])

eel.start('index.html', size = (1000, 800))


