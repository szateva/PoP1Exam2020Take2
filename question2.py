# 13021326

""" 1) s is a string and strings are immutable in Python, hence the changed[i] = s[i].upper() code will cause error
 To fix it, instead of defining changed as the original string s it could be an empty sting to which then the changed
 characters can be concatenated.
 2) in range(start, stop) the stop is not inclusive, so the code in the present format will underrun and therefore
 the last character will not be checked. To fix it the code should be range(0, len(s)) """

""" Consider the function replace that, in the string s, changes from the lower case to
upper case every letter. It preserves all the other characters as they are. It returns the
changed string. You may assume that the function is used only with strings.
def replace(s):
changed = s
for i in range(0, len(s)-1):
if s[i]>='a' and s[i]<='z':
changed[i] = s[i].upper()
else:
changed[i] = s[i]
return changed
There are errors in this code that have the potential to either crash the program on
some valid input, or to return incorrect result.
 Find and describe up to three of such errors. In your description, not only state
the errors, but provide the explanation why they occur.
 Indicate how to correct them.
Recommended answer length up to 70 words plus any code. """

def replace(s):
    changed = ""
    for i in range(0, len(s)):
        if s[i]>='a' and s[i]<='z':
            changed += s[i].upper()
        else:
            changed += s[i]
    return changed

print(replace("HelLo"))