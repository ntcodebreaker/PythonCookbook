# You can flatten a sequence -this is extract the scalar elements of a list 
# that is in turn an element inside another list- using an boolean function that
# tells you is some object is a scalar value and a recursive function

from __future__ import generators

def isScalar(obj):
    def canLoopOver(obj):
        try: iter(obj)
        except: return False
        else: return True
        
    def isStringLike(obj):
        try: obj + ""
        except: return False
        else: return True
    return isStringLike(obj) or not canLoopOver(obj)

# returns a flatten sequence through recursion
def flatten(seq, result=None, scalarp=isScalar):
    if result is None: result = []
    for item in seq:
        if scalarp(item):
            result.append(item)
        else:
            flatten(item, result)
    return result

# enumerates a flatten sequence through recursion
def flatten22(seq, scalarp=isScalar):
    for item in seq:
        if scalarp(item): 
            yield item
        else:
            for subitem in flatten22(item):
                yield subitem
    
    
seq = [1, 2, 3, 4, [5, 6, 7, [2, 2, 2, 2], 8], 9, 10, [11, 12, 13, 14], 15]
print(flatten(seq))
# for n in flatten22(seq): print(n)
