# use assignment as expression.
# Python does not support assignments as expressions. Thus
# you can wrap a value around a simple class.
# This is helpful when you want to transliterate a program
# from a language which supports this feature like C.

class DataHolder:
    def __init__(self, value = None):
        self.value = value
        
    def set(self, value):
        self.value = value
        return value
        
    def get(self):
        return self.value
        

import builtins
builtins.DataHolder = DataHolder
builtins.data = DataHolder()

def processline(line): print("->", line)

# You are not allowed to do this: "while f.readline:"
with open("09_stmt_as_expression.txt", "r", encoding="utf-8") as f:
    while data.set(f.readline()):
        processline(data.get())
