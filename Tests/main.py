
from time import sleep





str1 = "abdgggda"
str2 = "abdggda"


indexes_bad = []
good_indexes = []
for i in range(8):
    if str[i] != str2[i]:
        indexes_bad.append(i)
    else:
        good_indexes.append(i)



print(good_indexes)
print(indexes_bad)