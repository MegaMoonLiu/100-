with open("popular-names.txt","r") as popular_name, open("col1.txt", "w") as col_1, open ("col2.txt", "w") as col_2:
#   withステートメントを使用してファイルを開き
    text = popular_name.readlines()
    # readlines()関数でファイルの行を読み取り
    # print(text)

    # count = len(text)
    # print(count)

    for i,lines in enumerate(text):
        # enumerate()関数でインデックス番号, 要素の順に取得して
        # print(i,lines)
        name, sex, number, year = lines.split("\t")
        # split()関数で文字列を分割(ぶんかつ)して
        # print(name , sex)
        col_1.write(name + "\n")
        col_2.write(sex + "\n")
        # write()関数でファイルに書き込む

# Unix
# $cut -f 1 -d " " popular-names.txt
#          ctrl + v + tab
# $cut -f 2 -d " " popular-name.txt