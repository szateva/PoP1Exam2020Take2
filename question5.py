# 13021326

""" Implement the function
balance(init_sum, int_rate, tfl, tax_rate, M)
that calculates the current balance of a savings bank account at the end of M months
period. The calculation must reflect the following assumptions:
 In the beginning of the initial month, the balance is init_sum
 Every month, the monthly interest is calculated as int_rate percent of the bal-
ance s available in the beginning of this month
 Every month, the monthly tax is calculated as tax_rate percent of s - tfl, if
the balance s in the beginning of this month is greater than tfl (tax-free limit).
Otherwise, the monthly tax is 0.
 At the end of each month, the balance is updated by adding the monthly interest
and subtracting the monthly tax.
Indicative test cases:
balance(10000, 1, 20000, 1, 2) #must be approximately 10201
balance(25000, 2, 20000, 1, 2) #must be approximately 25904.5
balance(19800, 2, 20000, 1, 2) #must be approximately 20597.96 """

def balance(init_sum, int_rate, tfl, tax_rate, M):
    s = init_sum
    for m in range(M):
        interest = s*int_rate/100
        if s > tfl:
            tax = (s - tfl) * tax_rate/100
        else:
            tax = 0
        s += interest - tax
    return s

# Indicative test cases:
print(balance(10000, 1, 20000, 1, 2)) #must be approximately 10201
print(balance(25000, 2, 20000, 1, 2)) #must be approximately 25904.5
print(balance(19800, 2, 20000, 1, 2)) #must be approximately 20597.96