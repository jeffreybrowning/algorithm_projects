# def is_matched(expression):
#     if len(expression) % 2 != 0: return False
#
#     mid = len(expression) // 2
#     char_map = {'}': '{', ')': '(', ']': '['}
#     first_half = expression[:mid]
#     second_half = expression[mid:]
#
#     for i in range(len(first_half)):
#         if char_map.get(first_half[-i - 1], first_half[-i - 1]) != char_map.get(second_half[i], second_half[i]):
#             return False
#
#     return True


# ^ WRONG closed braces can happen any time



def is_matched(expression):
    stack = []
    char_map = {
        '{': '}',
        '(': ')',
        '[': ']'
    }

    for x in expression:
        if x in char_map:
            stack.append(x)
        if x in char_map.values():
            if not stack:
                return False
            if char_map[stack.pop()] != x:
                return False
    if stack == []:  # missed this part
        return True
    return False