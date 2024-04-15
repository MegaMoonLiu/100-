with open("popular-names.txt", "r") as popular_name:
    #   withステートメントを使用してファイルを開き
    count = int(input())
    # input()でキーボードから入力を受け取る
    text = popular_name.readlines()
    # readlines()関数でファイルの行を読み取り

    for n in reversed(range(count)):
        # reversed()でリストの要素を逆順に並べ替える
        print(text[count - n])

# Unix
# $tail -n 5 popular-names.txt
