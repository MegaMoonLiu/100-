str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
words = str.split(' ')

characters = [words[0][0],
              words[4][0],
              words[5][0],
              words[6][0],
              words[7][0],
              words[8][0],
              words[14][0],
              words[15][0],
              words[18][0],
            ]
for i in range(len(words)):
    if i not in [0,4,5,6,7,8,14,15,18]:
        # not in 
        characters.append(words[i][:2])

print(characters)

char_map = {}
for idx,char in enumerate(characters):
    # enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
    # idx 下标
    # char 元素
    char_map[char] = idx + 1

print(char_map)

