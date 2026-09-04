def isValid(s):
    low = 0
    high = 0

    for ch in s:

        if ch == '(':
            low += 1
            high += 1

        elif ch == ')':
            low -= 1
            high -= 1

        elif ch == '*':
            low -= 1      # '*' acts as ')'
            high += 1     # '*' acts as '('

        # We cannot have fewer than 0 unmatched '('
        low = max(low, 0)

        # Even the maximum possibility went negative
        if high < 0:
            return False

    return low == 0