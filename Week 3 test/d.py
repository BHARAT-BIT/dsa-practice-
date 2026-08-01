def countbits(n):
    bit_lst = [0] * n+1 
    for i in range(1,n+1):
        bit_lst[i] = (bit_lst[i] & bit_lst[i-1]) + 1

    return bit_lst    