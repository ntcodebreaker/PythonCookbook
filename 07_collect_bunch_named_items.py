# Every class has an inner dictionary. You can use
# that dict to group a bunch of variables into an 
# object. Once put together, you can refer the items using
# a neater object notation (not a dictionary).

class Bunch():
    def __init__(self, **kwds):
        self.__dict__.update(kwds)
        
x, y = 3, 4
        
b = Bunch(datum = y, squared = y * y, coord = x)

print(b.datum, b.squared, b.coord)
