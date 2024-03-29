# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


one_hundred = set(range(1,101))

sum_of = sum(one_hundred) ** 2


squares = set(x*x for x in range(1,101))

x =  sum_of - sum(squares)

# result is x = 25164150