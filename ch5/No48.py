from No40 import PATH

with open(PATH, "r", encoding="utf-8") as f:

    lines = f.readlines()

    text_dic = {}
    dic_list = []
    text = ""
    Flag_N = 0
    Flag_lastline = 0
    index_num = 0
    # 辞書のkey

    for line in lines:
        # print(line)
        if line == "EOS\n":
            # 文章の終わったら
            if Flag_lastline == 1:
                # もし　最後の行目
                if Flag_N == 1:
                    # nodeの記号するべきなら
                    text = "N:" + text
                    # nodeの記号する
                    Flag_N = 0

                text_dic[index_num] = [text, num]
                # 辞書に入れる
                dic_list.append(text_dic)
                # 辞書のlistに入れる
                text_dic = {}
                # 辞書を空になる
                Flag_lastline = 0
                # 最後の行目ではない
            continue

        if line[0] == "*":
            # 例え、* 0 -1D 1/1 0.000000

            if Flag_N == 1:
                # nodeの記号するべきなら
                text = "N:" + text
                Flag_N = 0
                # nodeの記号する

            num = int(line.split(" ")[2][:-1])
            # かかり先

            index_num = int(line.split(" ")[1])
            # かかり元

            text_dic[index_num] = [text, num]
            # 辞書に入れる

            text = ""
            if num == -1:
                # 係り先がないとき
                Flag_lastline = 1
                # 最後の行目になった
            continue

        if line.split("\t")[1][0:2] == "記号":
            # 記号を削除する
            continue
        text += line.split("\t")[0]
        if line.split("\t")[1].split(",")[0] == "名詞":
            # もし　名詞なら、nodeの記号するべきだ
            Flag_N = 1


def MakeTree(dic_list):
    # かかりむすびの木を作る
    result = []
    for text in dic_list.items():
        # 辞書listから一つずつを読み込む
        if text[1][0].split(":")[0] == "N":
            # nodeの記号があれば
            temp = ""
            num = int(text[0])

            while True:
                # print(dic_list)
                word = dic_list[num][0]
                # print("this is word")
                # print(word)
                num = int(dic_list[num][1])
                if num == -1:
                    # 木の最後になったら
                    temp += word
                    temp = temp.replace("N:", "")
                    # print("this is temp")
                    # print(temp)
                    # nodeの記号を削除する
                    break
                else:
                    temp += word + "->"
                    # じゃないと、木の記号する

            result.append(temp)
    return result


result_list = []

for index_dic in dic_list:
    index = MakeTree(index_dic)
    if len(index) == 0:
        continue
    result_list.extend(index)

# for i in range(10):
#     print(result_list[i])

# 出力
# 人工知能->指す->実現に関する->される
# 人工知能->指す->実現に関する->される
# じんこうちのう->AI->指す->実現に関する->される
# AI->指す->実現に関する->される
# エーアイとは->計算->という->道具を->知能を->研究する->計算機科学->の->一分野を->指す->実現に関する->される
# 計算->という->道具を->知能を->研究する->計算機科学->の->一分野を->指す->実現に関する->される
# 概念と->コンピュータ->という->道具を->知能を->研究する->計算機科学->の->一分野を->指す->実現に関する->される
# コンピュータ->という->道具を->知能を->研究する->計算機科学->の->一分野を->指す->実現に関する->される
# 道具を->知能を->研究する->計算機科学->の->一分野を->指す->実現に関する->される
