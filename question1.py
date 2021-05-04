# 13021326

""" The function takes two lists of numbers of equal length and returns a list of the same length
containing the arithmetic mean of the elements of the original lists index by index. """

""" Consider the following recursive function:
def fun(L1, L2):
if L1==[] and L2==[]:
return []
else:
return [(L1[0]+L2[0])/2]+fun(L1[1:], L2[1:])
Assume that the function is only called on a pair of lists of equal size containing
numbers.
Find the best English description of the purpose of this function. The use of mathe-
matical formulas or code in your description should be minimal, this is important in
marking. Recommended answer length up to 35 words. """

def fun(L1, L2):
    if L1==[] and L2==[]:
        return []
    else:
        return [(L1[0]+L2[0])/2]+fun(L1[1:], L2[1:])

L1 = [1, 2, 3, 4, 5]
L2 = [4, 4, 4, 4, 4]

print(fun(L1, L2))