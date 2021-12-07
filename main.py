# divident = int(input("Please enter divident :"))
# divider = int(input("Enter divider :"))

n = int(input("Please enterf a number to factor :"))
d = 2

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

factors = []

# n = 84
# d = 2

# result_2 = my_function(n, d)

# print(n)
while (n != 1):
    if my_function(n, d)[1] ==0:
        n = my_function(n, d)[0]
        # print(n)
        factors.append(d)
    else:
        d = d +1

print(factors)


# if result_2[1]==0:
#     factors.append(d)
#     n = result_2[0]
#     print(n)
# else:
#     d = d+1
# 
# print(n, d)
# 
# if result_2[1]==0:
#     factors.append(d)
#     n = result_2[0]
#     print(n)
# else:
#     d = d+1
# 
#     
# print(n, d)
# print(factors)
# result_debug = my_function(8820, 19)

# print(result_debug)

# while n != 1:
#     result_debug = my_function(n, d)
#     if result_debug[1]==0:
#         print("It is a factor : ")
#         n = result_debug[0]
#         d = d+1
#     else:
#         print("Not a factor")
    



# for range in (2, n):
#     divider = 2
#     result = my_function(divider, n)
#     if (result[1]==0):
#         print("Divided by " + repr(divider))
#         result[0] = n
    


