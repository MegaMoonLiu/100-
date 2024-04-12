import re


def cipher(text):
    text_pattern = re.compile("[a-z]")
    # py中的正则表达，生成一个规则
    # 需要match，search等使用该规则
    list = ""
    for char in text:
        if re.match(text_pattern,char):
            # 正则匹配
            char = chr(219-ord(char))
            # ord将字符转换为ASCII码
            # chr将ASCII码转换为字符
        list += char
    return list

text = "the quick brown fox jumps over the lazy dog"

encode = cipher(text)
print(encode)
decode = cipher(encode)
print(decode)