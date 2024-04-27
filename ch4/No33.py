from No30 import pos_tags


result = []
# print(pos_tags[0][0])
tags = set(
    [
        "NN",  # noun, singular 'desk' 名词单数形式
        "NNS",  # nounplural  'desks'  名词复数形式
        "NNP",  # propernoun, singular     'Harrison' 专有名词
        "NNPS",  # proper noun, plural 'Americans'  专有名词复数形式
    ]
)
for i in range(1, len(pos_tags) - 1):

    if (
        pos_tags[i - 1][1] in tags
        and pos_tags[i][0] == "'of"
        and pos_tags[i + 1][1] in tags
    ):
        result.append(pos_tags[i - 1][0] + " of " + pos_tags[i + 1][0])

print(result)
