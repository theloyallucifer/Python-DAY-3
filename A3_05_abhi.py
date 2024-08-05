n = int(input("Enter the number: "))

count_prime = 0
count_comp = 0
while n!= -1:
    #n = int(input("Enter the number: "))
    for i in range(2,n) :
        if n%i ==0 :
           count_comp+=1
           break
    else :
        count_prime+=1
    n = int(input("Enter the number: "))

    
    
print("Total prime numbers is: ",count_prime)
print("Total composite numbers is: ",count_comp)
