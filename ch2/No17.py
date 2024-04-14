with open("popular-names.txt" , "r") as popular_name:
#   withステートメントを使用してファイルを開き
    lines = popular_name.readlines()
    count = len(lines)
    #   readlines()関数でファイルの行を読み取り、行数を取得しています

    unique_strings = set()
    # 空集合を作成する

    for i in range(count):
        line = lines[i]
        columns = line.split('\t')[0]  
        unique_strings.add(columns)
        #　第i個目の第一列をsetに書き込む
        
    print(unique_strings)


