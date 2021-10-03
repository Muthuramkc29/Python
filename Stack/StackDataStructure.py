from Stack import Stack

def reverse_string_using_stack_deque(strings):
    stack = Stack()
    for string in strings:
        stack.push(string)

    return_string = ""
    while not stack.is_empty():
        return_string += stack.pop()

    return return_string


s = input()
result = reverse_string_using_stack_deque(s)
print(result)
