from No30 import pos_tags
import collections

words = []

for i in range(len(pos_tags)):
    words.append(pos_tags[i][0])

# print(words)

count = collections.Counter(words)
# print(count.most_common())
