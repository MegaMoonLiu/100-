def N_gram(n,text):
    text = text.replace(",", " ")
    text = text.replace(".", " ")
    # 数据处理
    words = text.split(" ")
    # 分割单词
    characters = text.replace(" ","")

    char_list = []
    words_list = []


    for char in range(len(characters)):
        char_list.append(characters[char:n+char])
        # char 起始 
        # n+char 窗口大小


    for word in range(len(words)):
        words_list.append(words[word:n+word])
        # words 起始
        # n+word 窗口大小

    return char_list , words_list


C_1, W_1 = N_gram(2,"paraparaparadise")
C_2, W_2 = N_gram(2,"paragraph")


X = set(C_1)
Y = set(C_2)
# 定义集合

union_set = X.union(Y)
# 并集运算
intersection_set = X.intersection(Y)
# 交集运算
difference_set = X.difference(Y)
# 差集运算

isInX = "se" in X
isInY = "se" in Y
# 包含检查
# issubset() 子集检查
print("se is in X? ",isInX)
print("se is in Y?",isInY)

