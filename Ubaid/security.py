# tech inventory and security control system

authorized_staff= ("izhar","ubaid","wajid","sahil","majid")
staff_names =(input("enter person name :"))
if staff_names not in authorized_staff  :
    print ("access denied")
else:
    item_names = ["keyboard","mouse","monitor","cpu"]
    inventory_status = []
    for items in item_names:
        status= input(f"enter your status of the {items} working or broken : ")
        inventory_status.append(status)

    for i in range (len(item_names)):
         if inventory_status[i] == "broken":
             print(f"the {item_names[i]} needs immediate repair")
         else:
             print(f"{item_names[i]} is functional")

      # calculation

    for j in range(len(item_names)):
           if inventory_status [j]== "broken":
             broken=j+1

    if broken > 0:
        print(f" {broken} moderate maintenance is required ")





