import MeCab
import re
import copy
from No46 import text_list

mecab = MeCab.Tagger("")
result = []

for line in text_list:
    # print(line)
    base_verb = line.split("\t")[0]
    # 動詞
    joshi_list = line.split("\t")[1].split(" ")
    # 助詞
    verbs_list = line.split("\t")[2].split(" ")
    # 残りの部分
    # print(base_verb)
    # print(joshi_list)
    # print(verbs_list)
    for joshi, verbs in zip(joshi_list, verbs_list):
        joshi_list_temp = copy.copy(joshi_list)
        verbs_list_temp = copy.copy(verbs_list)

        # print(verbs)
        verbs_MeCab = mecab.parse(verbs)
        # print(verbs_MeCab)

        verbs_MeCab = re.split("[\t,]", verbs_MeCab)
        # print(verbs_MeCab)

        if verbs_MeCab[0] == "EOS" or len(verbs_MeCab) == 1:
            continue

        # print(verbs_MeCab[2])
        # print(joshi)
        if verbs_MeCab[2] == "サ変接続":
            if joshi == "を":
                verb_result = verbs_MeCab[0] + joshi + base_verb
                # print(verb_result)
                joshi_list_temp.remove("を")
                # 述語になったので除去する
                verbs_list_temp.remove(verbs)
                # 述語になったので除去する
                result.append(
                    verb_result
                    + "\t"
                    + " ".join(joshi_list_temp)
                    + "\t"
                    + " ".join(verbs_list_temp)
                )

# for i in range(len(result)):
#     print(result[i])

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
