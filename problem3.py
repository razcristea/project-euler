# Problem 3
# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def is_prime(num):
    if num == 1:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

huge = 600851475143

# 600851475143 / 71 = 8462696833 / 839 = 10086647 / 1471 = 6857

for x in reversed(range(1,10000)):
    if is_prime(x):
        if huge % x == 0:
            print(x)

# result is 6857
# 6857
# 1471
# 839
# 71