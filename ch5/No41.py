from No40 import PATH


class Chunk(object):
    def __init__(self, bun, num, chunk_list):
        self.morphs = bun
        self.dst = num
        self.srcs = chunk_list


with open(PATH, "r", encoding="utf-8") as f:

    lines = f.readlines()
    # print(lines)
    all_sentense = []
    sentense = []
    Flag = 0

    chunk_dic = {}
    # その文係り先辞書
    pnum = -2
    # 初期値がない場合で一週目の処理ができないので
    bnum = -2
    # 初期値がない場合で一週目の処理ができないので

    for text in lines:
        if text[0] == "*":
            chunk_dic.setdefault(pnum, []).append(bnum)
            # 係り先辞書がないなら　空いておく

            if bnum not in chunk_dic:
                # 自分が係り先になっていない場合は、辞書が用意されていないので自分がkeyの空listを作る
                chunk_dic[bnum] = []

            if sentense:
                # 今の文全てがあれば、追加します
                all_sentense.append(Chunk(sentense, pnum, chunk_dic[bnum]).__dict__)

            sentense = []
            pnum = int(text.split(" ")[2][:-1])
            # print("係り先")
            # print(pnum)
            # 係り先
            bnum = int(text.split(" ")[1])
            # print("係り元")
            # print(bnum)
            # 係り元

            if Flag == 1:
                # 前の文はEOSなら新しい文ので係り辞書を空にする
                chunk_dic = {}
                Flag = 0
            continue

        if text[0:3] == "EOS":
            # 文末
            Flag = 1

        else:
            word = text.split("\t")
            # print(word)
            sentense.append(word[0])

# print(all_sentense[:10])

# 出力
# [
#     {"morphs": ["人工", "知能"], "dst": -1, "srcs": []},
#     {"morphs": ["人工", "知能"], "dst": 17, "srcs": []},
#     {"morphs": ["（", "じん", "こうち", "のう", "、", "、"], "dst": 17, "srcs": []},
#     {"morphs": ["AI"], "dst": 3, "srcs": []},
#     {
#         "morphs": ["〈", "エーアイ", "〉", "）", "と", "は", "、"],
#         "dst": 17,
#         "srcs": [2],
#     },
#     {"morphs": ["「", "『", "計算"], "dst": 5, "srcs": []},
#     {"morphs": ["（", "）", "』", "という"], "dst": 9, "srcs": [4]},
#     {"morphs": ["概念", "と"], "dst": 9, "srcs": []},
#     {"morphs": ["『", "コンピュータ"], "dst": 8, "srcs": []},
#     {"morphs": ["（", "）", "』", "という"], "dst": 9, "srcs": [7]},
# ]
