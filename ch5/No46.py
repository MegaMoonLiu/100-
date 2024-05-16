import MeCab
import re
from No44 import kakari_list

mecab = MeCab.Tagger("")
text_list = []

for lines in kakari_list:

    joshi_dic = {}

    for text in lines:
        # 各文章を処理する
        word = text.split("\t")
        # 係り受けを分ける

        second_word = mecab.parse(word[1].split(" ")[1]).split("\n")
        # 後半の部分を解析
        # print(second_word)
        for item_1 in second_word:

            verb = re.split("[\t,]", item_1)
            # print("this is verb")
            # print(verb)
            # listを整理する

            if verb[0] == "EOS" or len(verb) == 1:
                # EOS,spaceを削除する
                continue
            if verb[1] == "動詞":
                # 後半に動詞があるか判定する
                frist_word = mecab.parse(word[0].split(" ")[1]).split("\n")
                # 今　前半は助詞があるか判定する
                # print("this is frist_word")
                # print(frist_word)

                for item_2 in frist_word:
                    joshi = re.split("[\t,]", item_2)
                    # print("this is joshi")
                    # print(joshi)
                    # listを整理する
                    if joshi[0] == "EOS" or len(joshi) == 1:
                        # EOS,spaceを削除する
                        continue
                    if joshi[1] == "助詞":
                        # 助詞があれば
                        # print("this is word")
                        # print(word)
                        key_verb = word[1].split(" ")[0] + ":" + verb[7]
                        # print("this is key_verb")
                        # print(key_verb)
                        # print("this is word")
                        # print(word[0])
                        # print(word[0].split(" ")[1])
                        joshi_dic.setdefault(key_verb, []).append(
                            [joshi[0], word[0].split(" ")[1]]
                        )
                        # joshi_dicのvalueを助詞と分節の二次元listにする
                        # print("this is joshi_dic")
                        # print(joshi_dic)

    for key, value in joshi_dic.items():
        # print(key)
        # print(value)
        key = key.split(":")[1]
        value_text1 = []
        value_text2 = []
        for v in value:
            # print(v[0])
            # print(v[1])
            value_text1.append(v[0])
            value_text2.append(v[1])
        text = str(key) + "\t" + " ".join(value_text1) + "\t" + " ".join(value_text2)
        text_list.append(text)

for i in range(len(text_list)):
    print(text_list[i])
# 出力
# 推論をする
# 記述をする      と      主体と
# 注目を集める    が      サポートベクターマシンが
# 経験を行う      に を   元に 学習を
# 学習を行う      に を   経験を 元に
# 流行を超える
# 学習を繰り返す
# 推論をする      て で は を に を通して なされている ACT-Rでは ACT-Rでは 統計的学習を 元に 生成規則を通して
# 統計をする      て で は を に を通して なされている ACT-Rでは ACT-Rでは 推論ルールを 元に 生成規則を通して
