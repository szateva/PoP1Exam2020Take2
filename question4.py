# 13021326

""" Assume f(x) and g(x) are functions that are dened for numbers x and their return
values are also numbers. Implement a higher-order function:
 func_max(f,g)
that takes as parameters the functions f and g as above. It returns the function h(x)
that is dened on numbers x and the return value of this function on a given x is equal
to the maximum of m and n, where m = f(x) and n = g(x). Importing any libraries
is NOT allowed.
Indicative test cases:
def double(x):
return 2*x
def square(x):
return x*x
h1 = func_max(double, square)
assert h1(1) == 2 #must be True
assert h1(3) == 9 #must be True
h2 = func_max(double, abs)
#abs is standard Python function computing absolute value of number
assert h2(-2) == 2 #must be True"""