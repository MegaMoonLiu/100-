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
    characters.append(words[i][:2])

print(characters)

char_map = {}
for idx,char in enumerate(characters):
    char_map[char] = idx + 1

print(char_map)

