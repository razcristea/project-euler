# Problem 1
# Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.
import timeit

def multiples(num):
    x = []
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            x.append(i)
    return( sum(x) )


# multiples(1000)
# # result is 233168

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

argument = 1000
wrapped = wrapper(multiples, argument)

elapsed_time = timeit.timeit(wrapped, number=1000)
print(multiples(argument))
print('\nResult generated in {} ms.'.format(round(elapsed_time,2)))