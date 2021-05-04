# 13021326

""" Implement the function
balance(init_sum, int_rate, tfl, tax_rate, M)
that calculates the current balance of a savings bank account at the end of M months
period. The calculation must re
ect the following assumptions:
 In the beginning of the initial month, the balance is init_sum
 Every month, the monthly interest is calculated as int_rate percent of the bal-
ance s available in the beginning of this month
 Every month, the monthly tax is calculated as tax_rate percent of s - tfl, if
the balance s in the beginning of this month is greater than tfl (tax-free limit).
Otherwise, the monthly tax is 0.
 At the end of each month, the balance is updated by adding the monthly interest
and subtracting the monthly tax.
Indicative test cases:
balance(10000, 1, 20000, 1, 2) #must be approximately 10201
balance(25000, 2, 20000, 1, 2) #must be approximately 25904.5
balance(19800, 2, 20000, 1, 2) #must be approximately 20597.96 """