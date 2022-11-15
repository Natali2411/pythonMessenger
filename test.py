from copy import copy, deepcopy

d = {
    "d1": [[12, 13], [14, 15], 16],
}
d2 = d.copy()
assert d["d1"] is d2["d1"]
# print(d["d1"], d2["d1"])
d3 = deepcopy(d)
print(d3)
assert d["d1"] is d3["d1"]