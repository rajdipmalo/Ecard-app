# test file
import random

# Generate a random 12-digit number Aadhar
random_number = random.randint(10**11, 10**12 - 1)
print(random_number)

#PAN Card XJHQR3842P
import random
import string

# Generate first 5 random uppercase letters
first_part = ''.join(random.choices(string.ascii_uppercase, k=5))
print(string.ascii_uppercase)
print(random.choices(string.ascii_uppercase, k=5))
print("*".join(random.choices(string.ascii_uppercase, k=5)))
print(" ".join(random.choices(string.ascii_uppercase, k=5)))
print("".join(random.choices(string.ascii_uppercase, k=5)))
# Generate middle 4 random digits
middle_part = ''.join(random.choices(string.digits, k=4))
# Generate last random uppercase letter
last_part = random.choice(string.ascii_uppercase)
# Combine all parts
key = first_part + middle_part + last_part

#voter id ABC1234567
#First 3 letters – Represent the state or region (e.g., DEL for Delhi, UPA for Uttar Pradesh)
#Last 7 digits – A unique identifier for the voter within the constituency

first_part = ''.join(random.choices(string.ascii_uppercase, k=3))
last_part = ''.join(random.choices(string.digits, k=7))
key = first_part + last_part


#driving
# SS-RR-YYYY-NNNNNNN

#SS – State Code (e.g., DL for Delhi, MH for Maharashtra)
#RR – RTO (Regional Transport Office) Code
#YYYY – Year of Issue
#NNNNNNN – Unique Serial Number
#Example: DL-01-2022-1234567 

part1 = ''.join(random.choices(string.ascii_uppercase, k=2))
part2 = ''.join(random.choices(string.digits, k=2))
part3 = ''.join(random.choices(string.digits, k=7))
key = part1+"-"+part2+"-2025-"+part3
    
