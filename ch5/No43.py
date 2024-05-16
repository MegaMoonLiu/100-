import MeCab
import itertools
from No42 import kakari_list

mecab = MeCab.Tagger("")
NV_list = []
Flag1 = 0
Flag2 = 0

kakari_list_flatten = list(itertools.chain.from_iterable(kakari_list))
# print(kakari_list_flatten)
# 文章はリストになっているため、1次元配列にする

for line in kakari_list_flatten:

    text = line.split("\t")

    pretext = mecab.parse(text[0]).split("\t")
    # 前の文
    backtext = mecab.parse(text[1]).split("\t")
    # 後ろの文
    for ptemp in pretext:
        pp = ptemp.split(",")[0]
        if pp == "名詞":
            Flag1 = 1
        # 前の文は名詞なら
    for btemp in backtext:
        bb = btemp.split(",")[0]
        if bb == "動詞":
            Flag2 = 1
        # 後ろの文は動詞なら
    if Flag1 == 1 and Flag2 == 1:
        NV_list.append(line)
        # listに入れます
    Flag1 = 0
    Flag2 = 0

print(NV_list)
# 出力
# ['計算\tという',
#  'コンピュータ\tという',
#  '道具を\t用いて',
#  '知能を\t研究する',
#  '一分野を\t指す',
#  '知的行動を\t代わって',
#  '人間に\t代わって',
#  'コンピューターに\t行わせる',……
