# divident = int(input("Please enter divident :"))
# divider = int(input("Enter divider :"))

# factors = []

def my_function(divident, divider):
    counter = 0
    remainder = 0

    while divident>=divider:
        divident = divident - divider
        counter = counter + 1

    quotient = counter
    remainder = divident

    return quotient, remainder

# result = my_function(divident, divider)

# print(result[0])

# We have a function named my_functions
# which takes two arguments divident and divider
# and returns quotient and remainder

n = 8820

result_debug = my_function(8820, 2)

print(result_debug)


for range in (2, n):
    divider = 2
    result = my_function(divider, n)
    if (result[1]==0):
        print("Divided by " + repr(divider))
        result[0] = n
    


