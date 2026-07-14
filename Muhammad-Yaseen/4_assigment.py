# lets start

coffee_p = float(input("Enter the price of one coffee :"))
coffee_q = int(input("Enter the price of  coffee quntity:"))
total = coffee_p * coffee_p

print(f"""
=====================================
      SMART coffee RECEIPT
=====================================

coffee price      : ${coffee_p}
coffee quantity   : ${coffee_q}
Total bill        : ${total:.2f}

=====================================
            Thank you !
=====================================
""")