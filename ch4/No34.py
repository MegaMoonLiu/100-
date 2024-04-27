from No30 import pos_tags

tags = set(
    [
        "NN",  # noun, singular 'desk' 名词单数形式
        "NNS",  # nounplural  'desks'  名词复数形式
        "NNP",  # propernoun, singular     'Harrison' 专有名词
        "NNPS",  # proper noun, plural 'Americans'  专有名词复数形式
    ]
)
longest_count = 0
count = 0
sent = []
result = []

for i in range(len(pos_tags)):

    if pos_tags[i][1] in tags:
        # 今の単語は名詞のとき
        sent.append(pos_tags[i][0])
        count = len(sent)
        # 今の最長の名詞の連接を見つける
    else:
        # 今の単語は名詞じゃないのとき
        if count >= longest_count:
            # もし　今のは一番長い
            result = sent
            longest_count = len(result)
            # 今の長さを記録する
        sent = []
        count = 0
        # 記録を更新する

print("結果: " + str(result))
print("長さ: " + str(longest_count))
