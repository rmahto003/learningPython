# This function takes two arguments of type integers
# and returns qutioent and remainder
# Date created: 11-Dec-2021
# Place: Siliguri
# Author: Barun Sir

def d_vide(divident, divider):
    quotient = 0

    while divident>=divider:
        divident = divident - divider
        quotient = quotient + 1

    return quotient, divident

