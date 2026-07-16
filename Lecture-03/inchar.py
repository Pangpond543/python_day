incher = input("input one character: ")
if incher >= 'A' and incher <= 'Z':
    print("You in put Upper Case Letter ", incher)
elif incher >= 'a' and incher <= 'z':
    print("You in put Lower Case Letter ", incher)
elif incher >= '0' and incher <= '9':
    print("You in put Number ", incher)
else:
    print("It's not a letter or number.", incher)