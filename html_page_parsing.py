from bs4 import BeautifulSoup
import requests
import re

url = 'https://rozetka.com.ua/ua/sport-i-uvlecheniya'
#1
response_list = []
response = requests.get(url)
page_content = BeautifulSoup(response.content, "html.parser")
titles = page_content.find_all(class_="tile-cats__heading ng-star-inserted")
for i in titles:
    response_list.append(i['title'])
print(response_list)

#2
response_list_title = []
response_list_url = []
new_url_list = []
page_content = BeautifulSoup(response.content, "html.parser")
titles = page_content.find_all(class_="tile-cats__heading ng-star-inserted")
for i in titles:
    response_list_title.append(i['title'])
    response_list_url.append(i['href'])
for i in response_list_url:
    new_url_list.append(i.split())
    response_dict = dict(zip(response_list_title, new_url_list))
print(response_dict)

#3
response_list_text = []
response_list_text_result = []
page_content = BeautifulSoup(response.content, "lxml")
titles = page_content.find_all(class_="portal-grid__cell ng-star-inserted")
for i in titles:
    response_list_text.append(i.text)
for i in response_list_text:
    val = re.findall(r'[А-Я]+[^А-Я]+', i)
    response_list_text_result.append(val[1:len(val)+1])
resp_list_prefull = list(zip(response_list_url, response_list_text_result))
resonse_dict_full = dict(zip(response_list_title, resp_list_prefull))
