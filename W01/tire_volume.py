from datetime import datetime
import math

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10**7
volume = round(volume, 2)


print(f"The approximate volume is {volume} liters")

current_date = datetime.now().strftime("%Y-%m-%d")

with open("volumes.txt", "at") as file:
    file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume}\n")

purchase = input("Would you like to purchase tires with these dimensions? (yes/no): ").strip().lower()
if purchase == "yes":
    phone_number = input("Please enter your phone number: ")
    with open("volumes.txt", "at") as file:
        file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume}, {phone_number}\n")

