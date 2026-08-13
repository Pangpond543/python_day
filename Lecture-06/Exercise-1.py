heroes = ["Ironman", "Thor", "Hulk", "Spiderman"]
exit = True
while exit:
    print(f'heroes: {heroes}')

    heroes.append(input("Add Heroes: ").capitalize())
    print(f'heroes: {heroes}')

    heroes.insert(int(input("Insert index: ")), input("Insert Heroes: ").capitalize())
    print(f'heroes: {heroes}')

    remove_ = input(f'Remove Heroes: ').capitalize()
    while remove_ not in heroes:
        remove_ = input(f'Pleas enter name in Heroes: ').capitalize()
    heroes.remove(remove_)
    print(f'heroes: {heroes}')

    heroes.sort()
    n = int(input("Display Sorted Heroes ('1'Ascending / '2'Descending: " ))
    if n == 1:
        print(heroes)
    if n == 2:
        heroes.reverse()
        print(heroes)
        
    e =  input("exit? Y/N: " ).upper()
    if e == "N":
        exit = True
    else:
        exit = False