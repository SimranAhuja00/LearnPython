from math import sqrt
n = int(input("Enter the integer number: ")) 
prime_flag = 0
if(n > 1):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        print("True, it is a prime number")
    else:
        print("False, it is not a prime number")
else:
    print("False")
