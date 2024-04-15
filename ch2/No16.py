import numpy as np

with open("popular-names.txt", "r") as popular_name:
    #   withステートメントを使用してファイルを開き
    count = int(input())
    # input()でキーボードから入力を受け取る
    text = popular_name.readlines()
    # readlines()関数でファイルの行を読み取り

    # print(len(text))
    text_count = len(text)

    div_list = np.array_split(text, count)
    # numpy.split(): 等分割、または、任意の位置で分割
    # numpy.array_split(): できるだけ等分割で分割
    # print(div_list)

    for index, div in enumerate(div_list):
        # enumerate()関数でインデックス番号, 要素の順に取得して
        file_name = "div_" + str(index) + ".text"
        new_file = open(file_name, "w")
        for j in div:
            # forでデータを書き込む
            new_file.write(j)
        new_file.close()
        # 最後にファイルを閉じる

# Unix
# $split -n 5 -d popular-names.txt
