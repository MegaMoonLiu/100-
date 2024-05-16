import itertools
import MeCab
from No48 import dic_list, MakeTree


mecab = MeCab.Tagger("")
result_list49 = []


def XYEncoder(text, X_Y):
    # 名詞をXYに置き換える
    mtext = mecab.parse(text)
    # print(mtext)

    result = ""
    Flag = 0
    mtext = mtext.split("\n")
    # print(mtext)

    for m in mtext:
        if m.split("\t")[0] == "EOS" or len(m) == 0:
            # EOS,spaceを削除する
            continue

        pos = m.split("\t")[1].split(",")[0]
        # print(pos)

        if pos != "名詞" and pos != "形状詞" and pos != "代名詞":
            # 名詞句じゃないと、そのままresultに入れる
            result += m.split("\t")[0]
        elif Flag == 1:
            continue
        else:
            # 名詞句なら、XとYに置換する
            result += X_Y
            Flag = 1
    return result


def Clener(text):
    # 文字のIDを消し去る
    for i in range(len(text)):
        # print(text)
        text[i] = text[i].split(":")[0]
    return text


def Remakedict(predic):
    # 単語ごとにIDを渡す
    # print(predic)
    numembid = 0
    for n, text in predic.items():
        # print(n)
        # print(text)
        temp = [text[0] + ":{}".format(str(numembid)), text[1]]
        # print(temp)
        predic[n] = temp
        # print(predic)
        numembid += 1
    # print(predic)
    return predic


def Pairmaker(predic, sent_list):
    # 名詞の組み合わせと名詞のみの係結び木を抽出する
    n_list = []
    kakari_dic = {}
    i = 0
    for n, text in predic.items():

        if text[0].split(":")[0] == "N":
            # Nがあれば名詞である
            n_list.append(n)
            kakari_dic[n] = sent_list[i]
            i += 1
            # 名詞の組み合わせとかかりむすび木を記録する

        # print(n_list)
        # print(kakari_dic)
    return n_list, kakari_dic


for predic in dic_list:
    # 各文ごとに読み込む
    result_list = []
    predic = Remakedict(predic)
    # 単語ごとにIDを渡す
    sent_list = MakeTree(predic)
    # かかりむすびの木を作る
    n_list, kakari_dic = Pairmaker(predic, sent_list)
    # 名詞の組み合わせと名詞のみの係結び木を抽出する
    conb_list = list(itertools.combinations(n_list, 2))
    # print(conb_list)
    # 単語を二つずつ組み合わせで
    for conb in conb_list:
        # 単語グループを回す
        sent1 = kakari_dic[conb[0]].split("->")
        # print("this is sent1")
        # print(sent1)
        sent2 = kakari_dic[conb[1]].split("->")
        # print("this is sent2")
        # print(sent2)

        for sen2 in reversed(sent2):  # メインの処理
            for sen1 in reversed(sent1):

                last_word = sen2

                sent1[0] = XYEncoder(sent1[0], "X")
                sent2[0] = XYEncoder(sent2[0], "Y")
                sent1 = Clener(sent1)
                sent2 = Clener(sent2)
                last_word = last_word.split(":")[0]
                result49 = "->".join(sent1) + "|" + "->".join(sent2) + "|" + last_word

        if "X" not in result49 or "Y" not in result49:
            pass
        else:
            result_list.append(result49)  # 結果を追加
    if len(result_list) == 0:  # 空のリストがきたらスキップ
        continue
    result_list49.append(result_list)  # 最終結果、本文の一文ごとに区切って追加

print(result_list49)
# 出力
# [
#     "X->好奇心を->探索を->行う->AIを->いう|Yし->ノーゲームスコア->ノーゴール->探索を->行う->AIを->いう|Yし",
#     "X->好奇心を->探索を->行う->AIを->いう|Y->ノーゴール->探索を->行う->AIを->いう|Y",
#     "X->好奇心を->探索を->行う->AIを->いう|ノーY->探索を->行う->AIを->いう|ノーY",
#     "X->好奇心を->探索を->行う->AIを->いう|無Yで->目的->なき->探索を->行う->AIを->いう|無Yで",
#     "X->好奇心を->探索を->行う->AIを->いう|Y->なき->探索を->行う->AIを->いう|Y",
#     "X->好奇心を->探索を->行う->AIを->いう|Yを->行う->AIを->いう|Yを",
#     "X->好奇心を->探索を->行う->AIを->いう|Yを->いう|Yを",
#     "X->好奇心を->探索を->行う->AIを->いう|Y->これまでの->最も->いう|Y",
#     "X->好奇心を->探索を->行う->AIを->いう|Yまでの->最も->いう|Yまでの",
#     "X->好奇心を->探索を->行う->AIを->いう|Yで->最も->いう|Yで",
#     "Xが->好奇心を->探索を->行う->AIを->いう|Yを->探索を->行う->AIを->いう|Yを",
#     "Xが->好奇心を->探索を->行う->AIを->いう|Yし->ノーゲームスコア->ノーゴール->探索を->行う->AIを->いう|Yし",
# ]
