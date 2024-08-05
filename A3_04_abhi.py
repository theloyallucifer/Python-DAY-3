initial = int(input("Enter initial number: "))
final = int(input("Enter final number: "))

s=0

for i in range(initial,final) :
    for j in range(2,i) :
        if i%j ==0 :
           break
    else :
       s=s+i

print("Sum of all prime numbers in the given range is: ",s)

