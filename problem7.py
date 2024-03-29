# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def is_prime(num):
    if num == 1:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


count = 0
i = 1
while count < 10001:
    if is_prime(i):
        count += 1
    i += 1

print(i-1)

# result is 104743
    
