with open("poems.txt", "r") as file:
    content = file.read()
    if "Twinkle" in content:
        print("The word 'Twinkle' is present in the file.")
    else:
        print("The word 'Twinkle' is not present in the file.")    