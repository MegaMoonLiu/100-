with open("popular-names.txt" , "r") as popular_name:
#   withステートメントを使用してファイルを開き
    count = int(input())
    # input()でキーボードから入力を受け取る
    text = popular_name.readlines()
    # readlines()関数でファイルの行を読み取り
    for n in range(count):
        print(text[n])

# Unix
# $head -n 5 popular-names.txt