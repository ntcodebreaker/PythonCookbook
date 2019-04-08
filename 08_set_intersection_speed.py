# Several means to find common keys in two dictionaries.

import time

def timeo(func, n = 1000):
    def void(): pass
    start = time.clock()
    for i in range(n): void()
    stend = time.clock()
    overhead = stend - start
    start = time.clock()
    for i in range(n): func()
    stend = time.clock()
    thetime = stend-start
    return func.__name__, thetime - overhead

def filterfunc(k): return k in evens

# Iterate using the keys method
def badsloway():
    intersect = []
    for k in first500.keys():
        if k in evens.keys():
            intersect.append(k)
    return intersect

# Abbreviate using the in operator
def simpleway():
    intersect = []
    for k in first500.keys():
        if k in evens:
            intersect.append(k)
    return intersect

# Using list comprehesions
def pyth22way():
    return [k for k in first500 if k in evens]

# Using the filter builtin function (this is the fastest way)
def filterway():
    return filter(filterfunc, first500.keys())


    
first500 = {}
for i in range(500): first500[i] = 1

evens = {}
for i in range(0, 1000, 2): evens[i] = 1
    
for f in simpleway, pyth22way, filterway, badsloway:
    print("%s: %.2f" % timeo(f))
