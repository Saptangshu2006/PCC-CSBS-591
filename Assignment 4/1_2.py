cidr = int(input("Enter CIDR value: "))
bits = "1" * cidr + "0" * (32 - cidr)
mask = []
for i in range(0, 32, 8):
    mask.append(str(int(bits[i:i+8], 2)))
print("Subnet mask:", ".".join(mask))