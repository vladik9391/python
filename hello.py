from collections import OrderedDict
from requests import get, post

d = OrderedDict([
    ('pen', 3),
    ('pineapple', 3),
    ('apple', 3)
])

print(d.keys())
