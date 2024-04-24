import collections
import re


with open(R"ch3\UK_text.txt", "r", encoding="utf-8") as UK_text:

    UK_text = UK_text.readlines()
    # print(UK_text)
    # print(type(UK_text))

    result = re.findall("(={2,4}.*?={2,4})", str(UK_text))
    # re.findall(pattern, string, flags=0)
    # 正規表現を使って、stringからpatternとマッチした部分を取得します

    # sectionの書き方
    # ==History== section_1
    # ===Background=== section_2

    section_list = {}

    for text in result:
        section_ = collections.Counter(text)
        # print(section_)
        section_number = int(section_["="] / 2) - 1
        # print(section_number)

        # print(text)
        text = text.replace("=", "")
        # print(text)

        section_list[text] = section_number

    print(section_list)
