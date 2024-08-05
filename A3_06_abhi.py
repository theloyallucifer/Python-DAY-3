r = int(input("Enter the limit: "))

a=0
b=1
i=0
s=0
c=0
while c<=r:
    a=b
    b=c
    c = a+b
    if c%2==0 and c<=r:
        s+=c 
print("The sum of even places in fibonacci series is: ",s)       
  
