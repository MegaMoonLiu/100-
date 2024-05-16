import MeCab
from No41 import all_sentense
from No40 import PATH


mecab = MeCab.Tagger("")
text_dic = {}
i = 0
kakari_prelist = []
kakari_list = []
for line in all_sentense:
    text = ""
    for sign_check in line["morphs"]:
        if (
            mecab.parse(sign_check).split("\t")[1].split(",")[0] in "補助記号"
        ):  # 記号の除去
            pass
        else:
            text += sign_check.split("\t")[0]
    # 辞書に追加、かかり元を参照する
    text_dic[i] = text
    i += 1
    # 出力
    if line["srcs"] == []:
        pass
    else:
        pnum = line["srcs"]
        for j in pnum:
            kakari_prelist.append(text_dic[int(j)] + "\t" + text)
    if line["dst"] == -1:
        if kakari_prelist:
            kakari_list.append(kakari_prelist)
        kakari_prelist = []
        text_dic = {}
        i = 0

print(kakari_list)
# 出力
# [['AI\tエーアイとは',
#   '計算\tという',
#   'コンピュータ\tという',
#   'という\t道具を',
#   '概念と\t道具を',
#   'という\t道具を',
#   '道具を\t用いて',
#   '用いて\t研究する',
#   '知能を\t研究する',
#   '研究する\t計算機科学',
#   '計算機科学\tの',
#   'の\t一分野を',
#   '一分野を\t指す',
#   '人工知能\t語',
#   'じんこうちのう\t語',
#   'エーアイとは\t語',
#   '指す\t語'],……
