from No30 import pos_tags
import collections
import matplotlib.pyplot as plt

result = []

for i in range(len(pos_tags)):
    if pos_tags[i][0] == "alic":
        result.append(pos_tags[i + 1][0])

print(result)
count = collections.Counter(result)

word_list = []
count_list = []

for i in range(10):
    word_list.append(count.most_common()[i][0])
    count_list.append(count.most_common()[i][1])

plt.bar(x=word_list, height=count_list)
plt.show()
