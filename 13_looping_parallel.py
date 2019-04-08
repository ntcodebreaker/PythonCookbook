seq = ["nestor", "hugo", "gomez", "franco", 45, 22, False, "Python"]

# Show items and indexes from sequence using the range function
for i in range(len(seq)):
    print("index", i, seq[i])
    

# Show items and indexes from sequence using a wrap class
class Indexed:
    def __init__(self, seq):
        self.seq = seq
    def __getitem__(self, i):
        return self.seq[i], i

for item, index in Indexed(seq):
    print("index", index, item)


# Show items and indexes from sequence using the zip function
def IndexedFunc(seq):
    indices = range(len(seq))
    return zip(seq, indices)
    
zipped = IndexedFunc(seq)
for tuple in zipped:
    print("index", tuple[1], tuple[0])
    
