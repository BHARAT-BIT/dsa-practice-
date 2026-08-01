def unique_number(num):
    result = 0
    for n in num:
        result ^= n 
    return result     