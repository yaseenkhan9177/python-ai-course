# cafe bill

coffee_name = input("enter coffee name like (black,espresso,americano,latte) : ")
price = float(input("enter the price of the cafe : "))

# quantity
quantity = int(input("how much coffee do you want : "))

total_bill = quantity * price


print(f"""            =========================
                 caffee bill
            ========================  
                your order : {coffee_name} 
                price      : {price}
                total bill : {total_bill}
""")