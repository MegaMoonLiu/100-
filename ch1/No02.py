str_1 = 'shoe'
str_2 = 'cold'
str_list = ''

for i in range(len(str_1)):
    print(''.join(str_1[i]+str_2[i]),end='')
# .join()用于字符串拼接