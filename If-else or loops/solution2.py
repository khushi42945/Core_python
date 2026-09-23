# 1. Electricity Bill Calculator
# Problem Statement:
# Write a program to calculate the total electricity bill based on the number of units consumed, using slab-based pricing and an additional surcharge condition:
# First 100 units: ₹5 per unit
# Next 100 units (101 to 200 units): ₹7 per unit
# Above 200 units: ₹10 per unit
# Surcharge: If the total base bill exceeds ₹500, apply an additional 10% surcharge on the bill amount.

unit=int(input("enter the number of units"))
bill=1

if unit<=100:
    bill=unit*5
elif unit<=200:
    bill=(100*5)+((unit-100)*7)
else:
    bill=(100*5)+(100*7)+((unit-200)*10)                    

if bill>500:
    surcharge=bill*0.10
    tb=bill+surcharge
else:
    tb=bill


print("total bill is",tb)
    