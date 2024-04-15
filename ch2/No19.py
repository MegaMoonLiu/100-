import collections

with open("popular-names.txt", "r") as popular_name:
    #   withステートメントを使用してファイルを開き
    lines = popular_name.readlines()
    #   readlines()関数でファイルの行を読み取り
    lines = map(lambda x: x.replace("\n", ""), lines)
    lines = list(map(lambda x: x.split("\t"), lines))
    #   map()に書き込んで　データを整理して

    count = collections.Counter(map(lambda x: x[0], lines))

    print(count.most_common)
