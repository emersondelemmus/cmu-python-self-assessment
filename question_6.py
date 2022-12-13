#Consider the following dictionary d:

d = {1: {2: {3: "3"}},
     2: {"a": 2},
     "3": 1,
     "b": "a",
     "c": "b",
     3: 2}
#What is the output of:

print(d[d[d["3"]][d[2][d[d["c"]]]][3]])