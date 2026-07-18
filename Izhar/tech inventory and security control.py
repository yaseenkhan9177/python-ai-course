# tech inventory and security control
# security setup
authorized_staff = ('izhar','ubaid','wajid','umair','yaseen')
authorized_name = input("enter your name if you are authorized : ")

if authorized_name in authorized_staff:

    inventory = ['keyboard', 'mouse','moniter','CPU']
    inventory_status = []

    for item in inventory:
        status = input(f"enter the status of {item} (working/broken) : ")

        inventory_status.append(status)


    for i in range(len(inventory_status)):
        if inventory_status[i] == "broken":
                print(f"Alert! the {inventory[i]} needs immediate repair")


        elif inventory_status[i] == "working":
                print(f" The {inventory[i]} is functional")
    #   calculation of broken item

    for i in range(len(inventory_status)):
        if inventory_status[i] == "broken":
            broken =+ 1
    if broken > 0:
        print(f"there are {broken}) item is broken. Moderate maintanance required")

    if broken == 1 or broken == 2:
        print("STATUS : Moderate maintenace required")
    elif broken >= 3:
        if authorized_name == 'izhar':
            print("Manager, Please initiate emergency shutdown. ")
        else:
            print("System failure: Please contact to the supervisor immediately")

#     final summary display result
    print(f"""
        =======final report=======
        Helle Mr.{authorized_name}
        broken items :      {broken}
        
        
        
        """)



else:
    print("access denied")