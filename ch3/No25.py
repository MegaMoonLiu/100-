import re


with open(R"ch3\UK_text.txt", "r", encoding="utf-8") as UK_text:

    UK_text = UK_text.readlines()
    # print(UK_text)
    # print(type(UK_text))

    # Infobox countryの書き方
    # Infobox country\n| common_name               = United Kingdom\n| linking_name              = the United Kingdom
    # <!--Note: "the" required here as this entry used to create wikilinks-->\n| conventional_long_name    = United Kingdom of Great Britain and Northern Ireland\n|
    #  image_flag                = Flag of the United Kingdom.svg\n| alt_flag = A flag featuring both cross and saltire in red, white and blue\n|
    #  other_symbol = [[File:Royal Coat of Arms of the United Kingdom.svg|x100px]][[File:Royal Coat of Arms of the United Kingdom (Scotland).svg|
    # x100px]]\n| other_symbol_type = [[Royal coat of arms of the United Kingdom|Royal coats of arms]]:
    # {{#tag:ref |The coat of arms on the left is used in England, Northern Ireland, and Wales; the version on the right is used in Scotland|group=note}}\n|
    #  national_anthem                = "[[God Save the Queen]]"{{#tag:ref |
    # There is no authorised version of the national anthem as the words are a matter of tradition; only the first verse is usually sung.<ref>

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

    print(result_list_25)
