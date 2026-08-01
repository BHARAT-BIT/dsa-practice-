def is_leap(year):  
    if(year%100==0):
        return False 
    elif(year%4==0 or year%400==0):
        return True
    else:
        return False    
  
    

  
year = int(input())
is_leap(year)
print