fruits = {"apple", "banana", "cherry"}

fruits.add("orange")
print(fruits)

fruits.remove("orange")
print(fruits)

fruits.discard("orange")
print(fruits)

removed_item = fruits.pop()
print(removed_item)
print(fruits)

fruits.clear()
print(fruits)