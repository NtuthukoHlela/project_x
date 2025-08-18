'''
programmer: ntuthuko hlela
goal: test snippets of code
'''
import re

import pandas as pd

'''
l = list(range(1,10))
print(l)
del l[1]
print(l)

p = ['Unnamed: 117',  'Unnamed: 118',  'Unnamed: 119', 'Unnamed: 120', 'CHPT']

final_list = []
for i in p:
    o = re.sub(r'(Unnamed: \d*)', "",i)
    if o != "":
        final_list.append(o)


print(final_list)

'''
s = ["n", "t", "u"]

k = pd.DataFrame({"x": [1,2,3,4], "y": [5,6,7,8]})
z = pd.DataFrame({"z": [11,21,31,41]})
l = pd.concat([k,z], axis=1)
print(l)