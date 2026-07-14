# Inventory Management project

# setup of inventory  task 1
# brands of laptop we have in stock
laptops = ["Dell","HP","Apple","Asus","Lenovo"]

# prices of laptop
prices = [800,700,1200,600,500]

# accessing and slicing
print(laptops[0])
print(laptops[-1])

mid_laptop = laptops[1:4]

print(mid_laptop)

# replacing
laptops[2] = "Acer"

# advance operation
laptops.append("Samsung")
prices.extend([400])
prices.extend([300])
print(len(laptops))
print(len(prices))

# final display
print(f"""
            =====================
                Invectory Status   
                WE have total {len(laptops)} laptops on stock
                laptops availabe prices form {min(prices)}$ to {max(prices)}$""")