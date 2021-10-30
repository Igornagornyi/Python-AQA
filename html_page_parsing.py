from bs4 import BeautifulSoup
import requests

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
response_list_two = []
response_list_url = []
page_content = BeautifulSoup(response.content, "html.parser")
titles = page_content.find_all(class_="tile-cats__heading ng-star-inserted")
for i in titles:
    response_list_two.append(i['title'])
    response_list_url.append(i['href'])
    response_dict = dict(zip(response_list_two, response_list_url))
print(response_dict)

#3
response_list_text = []
page_content = BeautifulSoup(response.content, "lxml")
titles = page_content.find_all(class_="portal-grid__cell ng-star-inserted")
for i in titles:
    response_list_text.append(i.a['title'])
for key, value in zip(response_dict, response_list_text):
    response_dict[key] = response_dict[key] + " " + value

