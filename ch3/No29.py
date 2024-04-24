import urllib
import requests
import re


with open(R"ch3\UK_text.txt", "r", encoding="utf-8") as UK_text:

    UK_text = UK_text.readlines()
    # print(UK_text)
    # print(type(UK_text))

    result = re.findall("Infobox country(.*?\<ref\>)", str(UK_text))
    # re.findall(pattern, string, flags=0)
    # 正規表現を使って、stringからpatternとマッチした部分を取得します
    # print(result[0])
    # result += "\\n"
    result = re.findall("(?<=\\\\n\|)(.*?) *= *(.*?)(?=\\\\n)", result[0])
    # print(result)

    result_list_25 = {}

    for i, j in result:
        # print(i)
        # print(j)

        result_list_25[i] = j

    # print(result_list_25)

    # ----------------------------------
    # 26

    result_list_26 = {}

    for key, text in result_list_25.items():
        # re.sub(pattern, repl, string, count=0, flags=0)

        # pattern：正規表現
        # repl：交換したい文字列
        # string：交換したいデータ

        # count：可选参数，表示要替换的最大次数，而且必须是非负整数，该参数默认为0，即所有的匹配都会替换；
        # flags：可选参数，表示编译时用的匹配模式（如忽略大小写、多行模式等），数字形式，默认为0。

        # print(key)
        # print(text)

        result_list_26[key] = re.sub(".*?\\{2,5}", " ", text)
        # print(new_result_list[key])

    # print(result_list_26)

    # ------------------------------------------------------------------
    # 27

    result_list_27 = {}
    for key, text in result_list_26.items():

        # print("26 " + result_list_26[key])

        pattern = "\[{2}.*?\|.*?px\|(?=.*?\]\])"
        # [[File:Royal Coat of Arms of the United Kingdom (Scotland).svg|x100px]]\
        text = re.sub(pattern, "", text)

        pattern = "\<.*?\>"
        # the United Kingdom<!--Note: "the" required here as this entry used to create wikilinks-->\
        text = re.sub(pattern, "", text)

        pattern = "\[{2}.*?\|"  # [[(除去)|]]の処理
        text = re.sub(pattern, "", text)

        pattern = "(\[{2}|\]{2})"  # 最後に残ったやつを処理
        result_list_27[key] = re.sub(pattern, "", text)

        # print("27 " + result_list_27[key] + "\n")

    # print(result_list_27)

    # ------------------------------------------------------------------
    # 29

    for key, text in result_list_27.items():

        if key == " image_flag":
            titles = "File:" + result_list_27[key]
            break

    titles = str(titles).replace("\\", "")
    print(titles)


# API:Imageinfo
# sample code

S = requests.Session()


URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": titles,
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

for k, v in PAGES.items():
    print(v)
    print(v["title"] + " is uploaded by User:" + v["imageinfo"][0]["user"])
