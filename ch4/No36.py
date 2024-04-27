from No35 import words
import collections
import matplotlib.pyplot as plt

count = collections.Counter(words)
reuslt = count.most_common()

word_list = []
count_list = []

for i in range(10):
    word_list.append(reuslt[i][0])
    count_list.append(reuslt[i][1])

plt.bar(x=word_list, height=count_list)
plt.show()
