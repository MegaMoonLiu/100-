with open("popular-names.txt" , "r") as popular_name:
#   withステートメントを使用してファイルを開き
    line_count = len(popular_name.readlines())
#   readlines()関数でファイルの行を読み取り、行数を取得しています


print(line_count)
#   出力結果
#   2780

#   UNIX
#   wc -l "popular-names.txt"
#   出力結果
#   2780