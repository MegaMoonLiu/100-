import random

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind. "
text = text.replace(".","")
text = text.split(" ")

new_test = ""

for words in text:
    if len(words) < 4:
        pass
    else:
        words = words[0]+"".join(random.sample(words[1:-1],len(words[1:-1])))+words[-1]
    new_test += words + " "


print(new_test)