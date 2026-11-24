# Practical 03: Stack ADT and Applications

## Practical Number
Practical 03

## Practical Title
Stack ADT and Applications

## Problem Statement
Implement a Stack ADT using a fixed-capacity Python list with an explicit `top`. Implement `push`, `pop`, `peek`, `isEmpty`, and `isFull` operations. Use the stack for parenthesis matching and postfix expression evaluation.

## Concepts Used
- Fixed-capacity Stack ADT (`[None] * capacity`, `top = -1`)
- Stack Overflow and Underflow checks
- Balanced bracket checking (`()`, `{}`, `[]`)
- Postfix expression evaluation (`+`, `-`, `*`, `/`, `%`, `^`)

## Operations Implemented
- `StackADT`: `push(item)`, `pop()`, `peek()`, `isEmpty()`, `isFull()`
- `check_parentheses(expr)` — Checks whether brackets in `expr` are balanced.
- `evaluate_postfix(expr)` — Evaluates a space-separated postfix expression.

## How to Execute
```bash
cd "/home/satwik-rai/DS USING PYTHON LAB PRACTICALS/Lab_Practicals/Practical_03"
python3 main.py
```

## Sample Input and Output
```text
Top element: 20 | isFull: False
Popped: 20 10 | isEmpty: True
Parentheses '{[a+(b*c)]}': True
Parentheses '([)]'       : False
Postfix '10 2 8 * + 3 -' : 23
Postfix '-5 3 +'         : -2
```

## Important Edge Cases Handled
- Non-positive capacity (`<= 0`).
- Stack Overflow (`isFull`) and Stack Underflow (`isEmpty`).
- Empty expression, unmatched closing brackets, mismatched brackets, and unclosed brackets.
- Empty postfix expression, insufficient operands, division/modulo by zero, and malformed postfix expressions.
