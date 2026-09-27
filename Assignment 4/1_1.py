mask = input("Enter Subnet Mask: ")
parts = mask.split('.')
count = 0

for part in parts:
    count += bin(int(part)).count('1')

print("CIDR Notation: /" + str(count))