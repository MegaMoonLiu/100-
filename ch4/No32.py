from No30 import pos_tags

tags = set(
    [
        "VB",  # verb, baseform    take   动词
    ]
)
result = []
for word, pos in pos_tags:
    if pos in tags:
        result.append(word)
print(result[0:50])
