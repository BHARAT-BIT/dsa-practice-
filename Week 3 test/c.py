def countbits(n):
    lst = []
    for num in range(0,n+1):
        count = 0 
        for i in range(num.bit_length):
            if num & (1<<i):
                count+= 1
        lst.append(count)
    return lst         

       