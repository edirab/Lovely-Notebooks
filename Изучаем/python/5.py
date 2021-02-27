"""
aybe it's a cipher? Maybe, but we don’t know for sure.

Maybe you can call it "homomorphism"? i wish I know this word before.

You need to check that the 2 given strings are isometric. This means that a character from one string can become a match for characters from another string.

One character from one string can correspond only to one character from another string. Two or more characters of one string can correspond to one character of another string, but not vice versa.

Input: Two arguments. Both strings.

Output: Boolean.

Precondition:
both strings are the same size
"""

def isometric_strings(str1: str, str2: str) -> bool:
    # your code here
    d = {}

    for elem in enumerate(str1):
        if elem[1] not in d.keys():
            d[elem[1]] = str2[elem[0]]
        else:
            if d[elem[1]] != str2[elem[0]]:
                return False
    #print(str(d))
    return True



print(isometric_strings('add', 'egg'))
print(isometric_strings('foo', 'bar'))

# These "asserts" are used for self-checking and not for an auto-testing
assert isometric_strings('add', 'egg') == True
assert isometric_strings('foo', 'bar') == False
assert isometric_strings('', '') == True
assert isometric_strings('all', 'all') == True
print("Coding complete? Click 'Check' to earn cool rewards!")
