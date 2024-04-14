with open("col1.txt","r") as col_1, open("col2.txt","r") as col_2, open("col1+2.txt","w") as new_text:
#   withステートメントを使用してファイルを開き
    col_1_lines = col_1.readlines()
    col_2_lines = col_2.readlines()
    # readlines()関数でファイルの行を読み取り

    # print(col_1_lines)
    # print(col_2_lines)

    for name, sex in zip(col_1_lines,col_2_lines):
        # zipでリストなどの要素をまとめる
        name = name.replace("\n","")
        # replace()で改行を削除する
        # print(name)
        
        # print(sex)
        new_text.write(name + "\t" + sex)
        # write()でファイルに書き込む
        new_text.close()
        # 最後にファイルを閉じる

# Unix
# $paste col1.txt col2.txt
# pasteでファイルを行単位で連結する
