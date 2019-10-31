# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

c = 1
for a in range(1000):
    for b in range(1000):
        if c > 0 and c > b:
            c = 1000 - (a + b)
            if a > 0 and b > 0 and a < b and a+b+c == 1000 and (a*a + b*b == c*c):
                print(f'The Pythagorean triplet is: { a } { b } { c } and their product is {a*b*c}')


# The Pythagorean triplet is: 200 375 425 and their product is 31875000