input_string = input("Enter a string: ")

modifined_string = ""

vowels = "aeiouAEIOU"

for char in input_string:
    upper_char = char.upper()
    if upper_char in vowels:
        modifined_string += "*"
    else:
        modifined_string += upper_char
        
print("Modifine string:", modifined_string)