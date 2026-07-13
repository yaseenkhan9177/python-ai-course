# vehicles parking hub
# input
name = input("enter driver name:")
plate = input("enter vehicle plate :")
check_in =int(input("enter check_in hours:"))
hours=float(input("enter total hours parked:"))

# string manipulation
name =name.strip().title()
plate =plate.upper()

#in+hours) calculation
rate= 5.0
total_cost =hours*rate
check_out=int(check_in)
# output
print(f"""==========parking receipt========
      driver name: {name}
      vehical plate: {plate}
      check_in hours: {check_in}
      hours parked: {hours}
      check_out: {check_out}
      total cost: {total_cost}
      ======================
      thank you!""")