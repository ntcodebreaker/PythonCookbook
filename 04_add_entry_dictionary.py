# Use the function "setdefault" to modify the mutable elements of a dict.
# If the key does exist it is used, otherwise it is created and then used.

bookIndex = {}

def addWord(word, pageNum):
    bookIndex.setdefault(word, []).append(pageNum)

addWord("umbrella", 12)
addWord("umbrella", 32)
addWord("umbrella", 35)

print(bookIndex)
