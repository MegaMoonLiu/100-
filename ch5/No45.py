import MeCab
import re
from No44 import kakari_list

mecab = MeCab.Tagger("")
f = open("100--main/ch5/verb_pattern.txt", "w", encoding="utf-8")

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
                        key_verb = word[1].split(" ")[0] + ":" + verb[7]
                        # print("this is key_verb")
                        # print(key_verb)
                        joshi_dic.setdefault(key_verb, []).append(joshi[0])

    for key, value in joshi_dic.items():
        # print(key)
        # print(value)
        key = key.split(":")[1]
        text = str(key) + "\t" + " ".join(value) + "\n"
        f.write(text)

f.close

# cat /verb_pattern.txt | sort | uniq -c | sort -nr
# 出力
# 50 する	を
# 18 する	が
# 14 する	と
# 13 する	に
# 12 する	は を
# 10 れる	と

# cat /verb_pattern.txt | grep "行う" | sort | uniq -c | sort -nr
#   5 行う	を
#   1 行う	を に を
#   1 行う	まで を に
#   1 行う	に は で が

# 　cat verb_pattern.txt | grep "なる" | sort | uniq -c | sort -nr
#   3 なる	が と
#   2 なる	は に
#   2 なる	に
#   2 なる	と
#   1 異なる	も
#   1 異なる	で が

# cat verb_pattern.txt | grep "与える" | sort | uniq -c | sort -nr
#   1 与える	は に を
#   1 与える	が に
#   1 与える	が など に
