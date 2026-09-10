phonebook = {'Anirach': '777-1111', 'Mickey': '777-2222', 'Donald': '777-3333'}

print(phonebook)

print(phonebook['Mickey'])
print(phonebook.get['Donald'])

key = 'Pluto'
if key in phonebook:
    print(phonebook['Pluto'])
else:
    print(key + 'not in phonebook')

phonebook['Simpsop'] = '777-4567'
phonebook['Simpsop'] = '777-4444'
phonebook['Simpsop'] = '777-2122'