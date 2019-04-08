# Creates a dictionary by sending keyword arguments to a function
# without require them to be quoted.
def makeDictOutOfKwArgs(**kwargs):
    return kwargs

newDict = makeDictOutOfKwArgs(a = 101, b = 201, c = 301)
print(newDict)


# Takes in the items of an existant dictionary and some others as
# separate keyword arguments to return a new dictionary.
def copyDictWithNewValues(*args, **kwargs):
    d = { }
    for k, v in args: d[k] = v
    d.update(kwargs)
    return d

myDict = { "white": 0, "black": 1 }
myNewDict = copyDictWithNewValues(*myDict.items(), yellow = 2, green = 3)
print(myNewDict)

