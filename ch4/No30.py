import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.text import Text
from nltk.tag import pos_tag

with open("ch4/alice.txt", "r") as alice:

    alice_lines = alice.readlines()
    sent = []

    for text in alice_lines:
        sent.append(sent_tokenize(text))
    # print(sent[0:5])
    # 　文章を文になる

    words = []

    for i in sent:
        for j in i:
            words.extend(word_tokenize(j))
    # print(words[0:5])
    # 文を単語になる

    words_lower = []
    for i in words:
        words_lower.append(i.lower())

    # print(words_lower[0:5])
    # 小文字になる

    english_stopwords = stopwords.words("english")
    english_punctuation = [
        ",",
        ".",
        ":",
        ";",
        "?",
        "(",
        ")",
        "[",
        "]",
        "!",
        "@",
        "#",
        "%",
        "$",
        "*",
        "...",
        "'",
    ]
    words_clear = []

    for i in words_lower:
        if i not in english_stopwords:
            if i not in english_punctuation:
                words_clear.append(i)

    # print("/".join(words_clear[0:50]))
    # stop-words と記号を削除する

    st = PorterStemmer()
    words_stem = []
    for word in words_clear:
        words_stem.append(st.stem(word))
    # print(words_stem[0:50])
    # stemming

    pos_tags = pos_tag(words_stem)
    # print(pos_tags)

    alice_words_text = open("ch4/alice_words_tags.txt", "w")
    alice_words_text.write(str(pos_tags))
