def str_result(s):
    return "".join(ch.lower() for ch in s if ch.isalnum())
result = str_result("Hello, World! 123")
print(result)