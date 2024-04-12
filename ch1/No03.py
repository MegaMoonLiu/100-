str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

# 初步处理数据
str = str.replace(","," ")
# 去除,
str = str.replace("."," ")
# 去除.
str_list = str.split()

# print(str_list) 

for i in range(len(str_list)):
    print(len(str_list[i]),end=',')
