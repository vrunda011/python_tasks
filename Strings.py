import re

str = "hello world, this is new world, new world hello, hello"
clean = re.sub('[^A-Za-z0-9]+', ' ', str)
lst = clean.split(" ")

freq = {}

for word in lst:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)