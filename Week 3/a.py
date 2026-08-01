ip_string = input("Enter you string : ")
reversed_string = ip_string[::-1]
if ip_string == reversed_string:
    print(f"The string {ip_string} is Palindrome")
else:
    print(f"The string {ip_string} is not Palindrome")    