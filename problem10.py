# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from time import time

def is_prime(num):
    if num == 1:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


result = set()

start = time()

for i in range(2,2000001):
    if is_prime(i):
        result.add(i)

duration = (time() - start)

print(f'Result is {sum(result)}. Generated in {duration} seconds.')

# Result is 142913828922. Generated in 28.985161066055298 seconds.
