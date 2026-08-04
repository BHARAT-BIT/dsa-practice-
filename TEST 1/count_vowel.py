def count_vowels(string):
    vowels = "aeiouAEIOU"
    count=0
    for i in string:
        if i in vowels:
            count+=1
        else:
            pass
    return count 
string=input("Enter your string: ")
print(f"The no. of vowels in your string is {count_vowels(string)}")        
