import collections

with open("popular-names.txt", "r") as popular_name:
    #   withステートメントを使用してファイルを開き
    lines = popular_name.readlines()
    #   readlines()関数でファイルの行を読み取り
    lines = map(lambda x: x.replace("\n", ""), lines)
    lines = list(map(lambda x: x.split("\t"), lines))
    #   map()に書き込んで　データを整理して

    count = collections.Counter(map(lambda x: x[0], lines))
    #   collections.Counter()で一列目の文字列の出現頻度を求める

    print(count.most_common)
    # 　most_commonで高い順に並べる

    # Unix
    # $ cut -f 1 -d " " popular-names.txt|sort|uniq -c|sort -n -r
