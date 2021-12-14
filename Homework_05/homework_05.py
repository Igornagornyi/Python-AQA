from typing import List


#1
names_str = "john marta james Morgan Adam Maria huang"

def capital_names(value: str) -> str:
    """Print names in str with capital letter"""
    capital_names_str = value.title()
    return capital_names_str

#2
friends_list = ["John", "Marta", "James", "Amanda", "Marianna"]

def print_friends(value: List[str]) -> str:
    """Print names in list in column"""
    first_line = "Name".center(20, '*')
    print(first_line)
    for name in friends_list:
        print(name.rjust(10))

#3
query_str = "name=Amanda=sssss&age=32&&salary=1500&currency=quro"

def create_dict(value: str) -> dict:
    """Create dict from str"""
    my_dict = {}
    new_query_str = query_str.split('&&')
    format_1 = ''.join(new_query_str[0]).split('&')
    format_11 = ''.join(format_1[0]).split('=', 1)
    format_12 = ''.join(format_1[1]).split('=')
    format_2 = ''.join(new_query_str[1]).split('&')
    format_3 = ''.join(format_2[0]).split('=')
    format_4 = ''.join(format_2[1]).split('=')
    my_dict['name'] = format_11[1]
    my_dict['age'] = format_12[1]
    my_dict['salary'] = int(format_3[1])
    my_dict['currency'] = format_4[1]
    return my_dict


#4
camel_case = ["FirstItem", "FriendsList", "MyTuple"]

def create_str(value: List[str]) -> List[str]:
    my_str1 = ''.join(value[0])
    my_str2 = ''.join(value[1])
    my_str3 = ''.join(value[2])
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
    return my_list4

#5
# my_list = []
# with open('my_text.txt', encoding='utf-8') as file_object:
#     for line in file_object:
#         my_list.append(line.strip())


if __name__ == '__main__':

    print(capital_names(value=names_str))
    print_friends(value=friends_list)
    print(create_dict(value=query_str))
    print(create_str(value=camel_case))

