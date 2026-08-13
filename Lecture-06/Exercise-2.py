inventory = [
    ["Apple", 50, 0.75],
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]

def update_inventory(inventory, item_name: str, quantity_sold: int ) :
    for r in range(len(inventory)):
        if item_name in inventory[r]:
            n = inventory[r].pop(1)     # ไม่ต้อง pop ออกมาก็สามารถทำแบบนี้ได้ inventoty[r][1] -= quantity_sold
            inventory[r].insert(1, n - quantity_sold)
    return inventory

# update_inventory("Orange", 20)

def calculate_total_value(inventory):
    total = 0
    for r in inventory:
        # print(r[1])
        total += (r[1] * r[2])
    return total
    
# calculate_total_value()

def find_most_expensive(inventory):
    count = 0
    for r in inventory:
        if r[2] > count:
            count = r[2]
            result = r[0]
    return result
    
# find_most_expensive()

def add_item(inventory, item_name: str, quantity: int, price: float):
    inventory.append([item_name, quantity, price])
    return inventory
    
#--------------------------------------

update_inventory(inventory, "Banana", 20)
print("Total Value:", calculate_total_value(inventory))
print("Most Expensive:", find_most_expensive(inventory))

add_item(inventory, "Eggs", 30, 0.25)

print("Final Inventory:", inventory)