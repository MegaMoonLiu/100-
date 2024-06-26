import re


with open(R"ch3\UK_text.txt", "r", encoding="utf-8") as UK_text:

    UK_text = UK_text.readlines()
    # print(UK_text)
    # print(type(UK_text))

    result = re.findall("\[\[Category:.*?\]\]", str(UK_text))
    # re.findall(pattern, string, flags=0)
    # 正規表現を使って、stringからpatternとマッチした部分を取得します
    # regex101.com

    # d?        d出现0/1次
    # a＊       a可以出现0/多次
    # a+        a出现一次以上
    # a{6}      a出现6次
    # a{2,}     a出现2次以上
    # a{2,6}    a出现2-6次

    # 匹配多个字符：
    # (ab)+ ab出现一次以上

    # 或运算：
    # a (cat|dog) 匹配 a cat or a dog
    # a cat|dog 匹配 a cat or dog

    # 字符类：
    # 匹配由abc构成的数据[abc]+ abc出现一次以上 abc aabbcc
    # [a-zA-Z0-9] ABCabc123
    # ^ 排除 [^0-9] 匹配0-9之外的数据(包括换行符)

    # 元字符
    # \d 数字字符 \d+ 匹配一个以上的数字
    # \D 非数字字符
    # \w 单词字符 单词 数字 下划线即英文字符
    # \W 非单词字符
    # \s 空白符 包含空格和换行符
    # \S 非空白字符
    # \b 单词的边界 单词的开头或结尾 单词与符号之前的边界
    # \B 非单词的边界 符号与符号 单词与单词的边界
    # . 任意字符不包含换行符
    # \. 表示. 通过\进行了转意
    # ^ 匹配行首 $ 匹配行尾
    # *+{} 贪婪匹配
    #     <.+> 会匹配整串 因为是贪婪匹配
    # <.+?> 只匹配两个标签代码，+? 设置为懒惰匹配

    print(result)
