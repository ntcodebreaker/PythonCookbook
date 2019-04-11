# Create a list of lists using comprehensions 
# so items are not immutable.
def CreateMultilistNoReference():
    multi = [[0 for col in range(5)] for row in range(10)]
    multi[0][0] = 'Changed'

    for n in multi: print(n)


# Create a list of lists by multiplying  
# so items are mutable.
def CreateMultilistReference():
    row = [0] * 5
    multi = [row] * 10
    multi[0][0] = 'Changed'

    for n in multi: print(n)


CreateMultilistNoReference()
print()
CreateMultilistReference()
