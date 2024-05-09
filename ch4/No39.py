from No30 import pos_tags
import collections
import matplotlib.pyplot as plt

word_list = []

for word, pos in pos_tags:
    word_list.append(word)

data = collections.Counter(word_list)
data = sorted(data.values(), reverse=True)
# 低い順に並べる
# print(data)

plt.plot(data)
plt.xlabel("出現頻度順位")
plt.ylabel("出現頻度")

ax = plt.gca()
# 現在の軸(じく)を取得する
ax.set_yscale("log")
ax.set_xscale("log")
# 数値をlogする
plt.show()
