# Lexicographical comparison of lists

a = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3, 4, 5, 7]


# Simulate cmp builtin function in python 3
def cmp(a, b):
    return (a > b) - (a < b)

def lexcmp(a, b):
    i = 0
    while i < len(a) and i < len(b):
        outcome = cmp(a[i], b[i])
        if outcome:
            return outcome
        i += 1
    return cmp(len(a), len(b))
    
print(lexcmp(a, b))
