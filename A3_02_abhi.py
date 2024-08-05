
   
num = int(input("Enter a number to check if it is an Armstrong number: "))
digits = str(num)

num_digits = len(digits)

sum_of_powers = 0

for i in digits :
    sum_of_powers = sum_of_powers + (int(i) ** num_digits)

if sum_of_powers == num :
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
