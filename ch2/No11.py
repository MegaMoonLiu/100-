with open("popular-names.txt", "r") as popular_name:
    #   withステートメントを使用してファイルを開き
    for lines in popular_name:
        print(lines.replace("\t", " "))

        # forでタブ1文字につきスペース1文字に置換します

# UNIX指令
#   $ cat popular-names.txt | sed "s/\t/ /"
#       catでファイルの中身を確認し　sed "s"で置換します
#   $ cat popular-names.txt | tr "\t" " "
#       catでファイルの中身を確認し　trで置換します
#   $ cat popular-names.txt | expand -t 1
#       catでファイルの中身を確認し　expandで各列のデータを1文字に揃えて表示する
