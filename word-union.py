import sys

d = {}

with open("words-1.txt", "r" ) as f_src_1:
  words1 = f_src_1.readlines()

with open("words-2.txt", "r" ) as f_src_2:
  words2 = f_src_2.readlines()

i = 0
j = 0
k = 0
while i < len(words1):
    a = words1[i].strip()
    while j < len(words2):
        b = words2[j].strip()
        if a == b and a not in d:
            d[a] = k
            i += 1
            j = 0
        else:
            j += 1
    i += 1
    j = 0

for word in sorted(d):
    print(word)
