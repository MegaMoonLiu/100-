from No30 import pos_tags
import collections
import matplotlib.pyplot as plt


word_list = []

for word, pos in pos_tags:
    word_list.append(word)

data = collections.Counter(word_list)
plt.hist(data.values(), range(1, 10))
plt.show()
