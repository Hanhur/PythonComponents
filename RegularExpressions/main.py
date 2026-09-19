# Регулярные выражения в Python. Декораторы property, setter, deleter

import re

string = "There are 300 spartans right now defending their ground"
find = re.search(r"\d+", string)
print(find)