# inventory management
inventory = ["dell","hp","apple","asus","lenovo"]
price=[800,700,1200,600,500]
# accessing
print(inventory[0])
print(inventory[-1])
mid_laptop = inventory[1:4]
print(mid_laptop)
# modifying data
inventory[2]="acer"

price[0]=850

inventory.append("samsung")
price.extend([400,300])
print(price)
print(len(inventory))
print(len(price))
print(f"we have {len(inventory)}  laptop available starting from {min(price)}$ to the {max(price)}$")
