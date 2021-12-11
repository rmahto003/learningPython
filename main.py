from divide_module import d_vide

n = int(input("Please enter a number to factorise :"))
d = 2

factors = []


# We have a function named d_vides
# which takes two arguments divident and divider
# and returns quotient and remainder

while (n != 1):
    if d_vide(n, d)[1] ==0:
        n = d_vide(n, d)[0]
        factors.append(d)
    else:
        d = d +1

print(factors)


