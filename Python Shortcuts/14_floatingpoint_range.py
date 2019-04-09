# built-in range function can't generate float numbers
# so you must create a custom function to accomplish that goal.

def frange(start, end=None, inc=1.0):
    if end == None:
        # turn arguments into floats explicitly
        end = start + 0.0
        start = 0.0
    seq = []
    while 1:
        next = start + len(seq) * inc
        if inc > 0 and next >= end:
            break
        elif inc < 0 and next <= end:
            break
        seq.append(round(next, 2))
    return seq

for n in frange(5, 10, 0.25): print(n)
