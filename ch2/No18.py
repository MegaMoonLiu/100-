with open("popular-names.txt", "r") as popular_name:
    #   withステートメントを使用してファイルを開き
    lines = popular_name.readlines()
    #   readlines()関数でファイルの行を読み取り

    lines = map(lambda x: x.replace("\n", ""), lines)
    lines = map(lambda x: x.split("\t"), lines)
    #   map()に書き込んで　データを整理して

    lines = list(lines)

    lines = sorted(lines, key=lambda x: x[2], reverse=True)
    #           要排序的数据, 排序的标准, 是否翻转
    # sorted()で各行を3コラム目の数値の逆順で整列する

    print(lines)

# Unix
# $sort -n -r -k 3 popular-names.txt
# -n 整数順に並べる　-r 降順に並べる　-k 3　第三列目で
