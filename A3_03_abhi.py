a = int(input("Enter a positive integer: "))
b = int(input("Enter another positive integer: "))
lcm = 0
if a>b :
    lcm = a
    while lcm>=a:
        if lcm%a == 0 and lcm%b == 0:
            break
        lcm+=1
else:
    lcm = b
    while temp>=b:
        if lcm%a == 0 and lcm%b == 0:
            break
        lcm+=1
print("LCM is ", lcm)
