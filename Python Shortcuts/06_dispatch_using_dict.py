# Use function as first class objects and
# dispatch using a list

def deal_with_a_cat():
    print("meow")

def deal_with_a_dog():
    print("bark")

def deal_with_a_bear():
    print("watch out for the *HUG*")

tokenDict = {
    "cat": deal_with_a_cat,
    "dog": deal_with_a_dog,
    "bear": deal_with_a_bear
    }

words = ["cat", "bear", "cat", "dog"]

for word in words:
    functionToCall = tokenDict[word]
    functionToCall()

    
