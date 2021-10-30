
#1
names_str = "john marta james Morgan Adam Maria huang"
title_names_str = names_str.title()
print(title_names_str)

#2
friends_list = ["John", "Marta", "James", "Amanda", "Marianna"]
print("Name".center(20, '*'))
for name in friends_list:
    print(name.rjust(10))

#3
query_str = "name=Amanda=sssss&age=32&&salary=1500&currency=quro"
new_query_str = query_str.split('&&')
format_1 = ''.join(new_query_str[0]).split('&')
format_11 = ''.join(format_1[0]).split('=', 1)
format_12 = ''.join(format_1[1]).split('=')
format_2 = ''.join(new_query_str[1]).split('&')
format_3 = ''.join(format_2[0]).split('=')
format_4 = ''.join(format_2[1]).split('=')
my_dict = {}
my_dict['name'] = format_11[1]
my_dict['age'] = format_12[1]
my_dict['salary'] = int(format_3[1])
my_dict['currency'] = format_4[1]
print(my_dict)

#4
camel_case = ["FirstItem", "FriendsList", "MyTuple"]
my_str1 = ''.join(camel_case[0])
my_str2 = ''.join(camel_case[1])
my_str3 = ''.join(camel_case[2])
my_list1 = []
my_list2 = []
my_list3 = []
my_list4 = []
for i in my_str1:
    if i.isupper():
        i = '_' + i
    my_list1.append(i)
    my_list11 = list(''.join(my_list1))
my_list11.remove('_')
for i in my_str2:
    if i.isupper():
        i = '_' + i
    my_list2.append(i)
    my_list21 = list(''.join(my_list2))
my_list21.remove('_')
for i in my_str3:
    if i.isupper():
        i = '_' + i
    my_list3.append(i)
    my_list31 = list(''.join(my_list3))
my_list31.remove('_')
my_list4.append(''.join(my_list11).lower())
my_list4.append(''.join(my_list21).lower())
my_list4.append(''.join(my_list31).lower())
print(my_list4)

#5
my_list = []
with open('my_text.txt', encoding='utf-8') as file_object:
    for line in file_object:
        my_list.append(line.strip())
print(my_list)


