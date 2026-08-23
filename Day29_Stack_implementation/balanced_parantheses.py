def balanced_parantheseis(str):
    stack = []

    pairs = {')': '(', '}': '{', ']': '['}

    for ch in str:

        if ch in pairs.values():
            stack.append(ch)

        elif ch in pairs:

            if not stack:
                return False

            if stack.pop() != pairs[ch]:
                return False

    return not stack