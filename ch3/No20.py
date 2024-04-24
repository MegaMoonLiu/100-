import json


with open("ch3\enwiki-country.json", "r", encoding="utf-8") as enwiki_country:

    # open()でフィールを開き
    # UnicodeDecodeErrorが発生した
    # encoding="utf-8"

    lines = enwiki_country.readlines()
    # readlines()関数でファイルの行を読み取り
    # print(lines)

    text_list = list()

    for line in lines:

        text = json.loads(line)
        # print(text)
        # print(type(text))
        # textの型はdict

        text_list.append(text)
        # print(text_list)
        # print(type(text_list))

    # print(text_list[0])
    # print(text_list[0]["title"])

    # print(len(text_list))
    for index in range(len(text_list)):

        if text_list[index]["title"] == "United Kingdom":
            UK_text = open("\ch3\UK_text.txt", "w", encoding="utf-8")
            UK_text.write(str(text_list[index]))
            # write() argument must be str, not dict
            # print(UK_text)
