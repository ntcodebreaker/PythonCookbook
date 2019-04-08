# allows duplicated values
feats = {}

feats.setdefault("colors", []).append("red")
feats.setdefault("colors", []).append("blue")
feats.setdefault("colors", []).append("blue")
print(feats["colors"])

feats.setdefault("sizes", []).append("medium")
feats.setdefault("sizes", []).append("medium")
feats.setdefault("sizes", []).append("high")
print(feats["sizes"])


# remove item from a list item
feats["colors"].remove("red")
print(feats["colors"])

feats["sizes"].remove("high")
print(feats["sizes"])



# does not allow duplicated values
eggs = {}
eggs.setdefault("colors", {})["red"] = 1
eggs.setdefault("colors", {})["blue"] = 2
eggs.setdefault("colors", {})["blue"] = 3

eggs.setdefault("sizes", {})["medium"] = 2
eggs.setdefault("sizes", {})["medium"] = 3
eggs.setdefault("sizes", {})["high"] = 3

print(eggs)
