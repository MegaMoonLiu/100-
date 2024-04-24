import re


with open(R"ch3\UK_text.txt", "r", encoding="utf-8") as UK_text:

    UK_text = UK_text.readlines()
    # print(UK_text)
    # print(type(UK_text))

    result = re.findall("\[\[Category:(.*?)\]\]", str(UK_text))
    # re.findall(pattern, string, flags=0)
    # 正規表現を使って、stringからpatternとマッチした部分を取得します

    print(result)
