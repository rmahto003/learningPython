n = int(input("Please enter a number to factorise :"))
d = 2

factors = []

def my_function(divident, divider):
    counter = 0
    remainder = 0

    while divident>=divider:
        divident = divident - divider
        counter = counter + 1

    return counter, remainder

# We have a function named my_functions
# which takes two arguments divident and divider
# and returns quotient and remainder

factors = []

while (n != 1):
    if my_function(n, d)[1] ==0:
        n = my_function(n, d)[0]
        factors.append(d)
    else:
        d = d +1

print(factors)

