# Smart Vehicle Parking Hub

driver_name = input("Enter your name: ").strip().title()
vehicle_plate = input("Enter vehicle plate number: ").strip().upper()
check_in_hour = int(input("Enter check-in hour (24-hour format): "))
hours_parked = float(input("Enter total hours parked: "))

PARKING_RATE = 5.00

total_cost = hours_parked * PARKING_RATE
check_out_hour = int(check_in_hour + hours_parked)

print(f"""
=====================================
      SMART PARKING RECEIPT
=====================================

Driver Name      : {driver_name}
License Plate    : {vehicle_plate}
Check-in Hour    : {check_in_hour}
Hours Parked     : {hours_parked}
Check-out Hour   : {check_out_hour}

Rate Per Hour    : ${PARKING_RATE:.2f}
Total Cost       : ${total_cost:.2f}

=====================================
Thank you for using Smart Parking!
=====================================
""")