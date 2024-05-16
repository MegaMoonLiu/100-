PATH = "100--main\ch5\\ai.ja.txt.parsed"


class Morph(object):
    def __init__(self, pos):
        self.surface = pos[0]
        self.base = pos[7]
        self.pos = pos[1]
        self.pos1 = pos[2]


with open(PATH, "r", encoding="utf-8") as f:

    lines = f.readlines()
    ai_list = []
    morph_list = []

    for text in lines:

        if text[0:3] == "EOS":

            if ai_list:
                morph_list.append(ai_list)
                ai_list = []

            continue

        if text[0] == "*":
            continue

        pos = text.split("\t")
        temp = pos[1].split(",")
        pos.pop()
        pos.extend(temp)
        ai_list.append(Morph(pos).__dict__)


# print(morph_list)

# 出力
# [[{'surface': '人工', 'base': '人工', 'pos': '名詞', 'pos1': '一般'},
#   {'surface': '知能', 'base': '知能', 'pos': '名詞', 'pos1': '一般'}],
#  [{'surface': '人工', 'base': '人工', 'pos': '名詞', 'pos1': '一般'},
#   {'surface': '知能', 'base': '知能', 'pos': '名詞', 'pos1': '一般'},
#   {'surface': '（', 'base': '（', 'pos': '記号', 'pos1': '括弧開'},
#   {'surface': 'じん', 'base': 'じん', 'pos': '名詞', 'pos1': '一般'},
#   {'surface': 'こうち', 'base': 'こうち', 'pos': '名詞', 'pos1': '一般'},
#   {'surface': 'のう', 'base': 'のう', 'pos': '助詞', 'pos1': '終助詞'},……
