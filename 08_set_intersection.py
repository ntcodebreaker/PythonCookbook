# Find common keys in two dictionaries.

def CreateDict(**kwds):
    return kwds
    
dict1 = CreateDict(zope = "zzzzz", python = "rocks", ruby = "japanese")
dict2 = CreateDict(python = "rocks", pearl = "$", ruby = "dadada")

# using the traditional way
intersect = []
for item in dict1.keys():
    if item in dict2.keys():
        intersect.append(item)

print(intersect)

# using list comprehesions
intersect = [k for k in dict1 if k in dict2]
print(intersect)

