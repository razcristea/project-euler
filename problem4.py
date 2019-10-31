# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


for x in range(100, 1000):
    for y in range(100,1000):
        z = x * y
        i = [n for n in str(z)]
        j = i[::-1]
        if i == j:
            print(f'{x} and {y} equals {z}')

# 993 and 913 = 906609 is the correct result