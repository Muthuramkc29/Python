from Stack import Stack

def check_for_pair(open_brack, close_brack):
    if open_brack == '[' and close_brack == ']':
        return True

    if open_brack == '{' and close_brack == '}':
        return True

    if open_brack == '(' and close_brack == ')':
        return True

    return False

def balanced_paranthesis(strings):
    stack = Stack()
    for ch in strings:
        if ch == '[' or ch == '{' or ch == '(':
            stack.push(ch)
        if ch == ']' or ch == '}' or ch == ')':
            if stack.is_empty():                      # len(self.container) == 0
                return False
            if not check_for_pair(stack.pop(),ch):
                return False

    return stack.is_empty()

print(balanced_paranthesis("({a+b})"))
print(balanced_paranthesis("))((a+b}{"))
print(balanced_paranthesis("((a+b))"))
print(balanced_paranthesis("))"))
print(balanced_paranthesis("[a+b]*(x+2y)*{gg+kk}"))
