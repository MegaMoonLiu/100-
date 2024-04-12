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


char, words = N_gram(2,"I am an NLPer")
print(char)
print(words)