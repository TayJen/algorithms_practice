stack = []
raw_input = input()

def is_valid_sequence():
    for scob in raw_input:
        if scob in '({[':
            stack.append(scob)
        elif len(stack):
            if scob == ')':
                elem = stack.pop()
                if elem != '(':
                    return False
            elif scob == '}':
                elem = stack.pop()
                if elem != '{':
                    return False
            elif scob == ']':
                elem = stack.pop()
                if elem != '[':
                    return False
        else:
            return False

    if len(stack):
        return False

    return True


if is_valid_sequence():
    print('YES')
else:
    print('NO')
