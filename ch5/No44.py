import MeCab
from graphviz import Digraph
from No41 import all_sentense
from No40 import PATH

mecab = MeCab.Tagger("")
text_dic = {}
i = 0
kakari_prelist = []
kakari_list = []
for line in all_sentense:
    text = ""
    # print(line)
    for sign_check in line["morphs"]:

        if (
            mecab.parse(sign_check).split("\t")[1].split(",")[0] in "補助記号"
        ):  # 記号を削除
            pass
        else:
            text += sign_check.split("\t")[0]

    # 辞書に追加、かかり元を参照する
    text = str(i) + " " + text
    # 番号を付ける
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

# print(kakari_list)
# 出力
# [['2 AI\t3 エーアイとは',
#   '4 計算\t5 という',
#   '7 コンピュータ\t8 という',
#   '5 という\t9 道具を',
#   '6 概念と\t9 道具を',
#   '8 という\t9 道具を',
#   '9 道具を\t10 用いて',
#   '10 用いて\t12 研究する',
#   '11 知能を\t12 研究する',
#   '12 研究する\t13 計算機科学',
#   '13 計算機科学\t14 の',
#   '14 の\t15 一分野を',
#   '15 一分野を\t16 指す',
#   '0 人工知能\t17 語',
#   '1 じんこうちのう\t17 語',
#   '3 エーアイとは\t17 語',
#   '16 指す\t17 語'],……

# Graphvizで係り受け木を作る
i = 0
for lines in kakari_list:
    graph = Digraph(format="png")
    for line in lines:
        text = line.split("\t")
        graph.node(text[0])
        graph.node(text[1])
        graph.edge(text[0], text[1])
        # グラフを描く

    graph.save("100--main/ch5/output{}".format(str(i).zfill(3)) + ".gv")
    i += 1
# 描いたグラフを保存する
