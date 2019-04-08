# use list comprehesions to simplify the meaning
# of lambda expressions.

def printlist(lst):
    for item in lst: print(item, end=", ")

oldlist = [n for n in range(31)]

newlist = map(lambda n: n + 23, oldlist)
newlist = [n + 23 for n in oldlist]

newlist = filter(lambda n: n > 25, oldlist)
newlist = [n for n in oldlist if n > 25]

newlist = map(lambda n: n + 23, filter(lambda n: n > 25, oldlist))
newlist = [n + 23 for n in oldlist if n > 25]

printlist(newlist)
