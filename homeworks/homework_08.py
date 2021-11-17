from bs4 import BeautifulSoup
import requests
import re

url = 'https://rozetka.com.ua/ua/sport-i-uvlecheniya'

def get_section_titles_href_from_rozetka(url):
    response = requests.get(url)
    page_content = BeautifulSoup(response.content, "html.parser")
    html_text = page_content.find_all(class_="tile-cats__list ng-star-inserted")
    return html_text
x = get_section_titles_href_from_rozetka(url)

def get_titles_list(url):
    response_list = []
    html_titles = get_section_titles_href_from_rozetka(url)
    for i in html_titles:
        response_list.append(i.a['title'])
    return response_list

r = get_titles_list(url=url)

def get_href_list(url):
    response_list_url = []
    html_href = get_section_titles_href_from_rozetka(url)
    for i in html_href:
        response_list_url.append(i.a['href'])
    return response_list_url

z = get_href_list(url)

def get_subtitle_href(url):
    response_list_url = []
    response = requests.get(url)
    page_content = BeautifulSoup(response.content, "html.parser")
    html_text = page_content.find_all(class_="tile-cats__item ng-star-inserted")
    for i in html_text:
        response_list_url.append(i.a['href'])
    return response_list_url

uu = get_subtitle_href(url)

def get_titles_and_href_dict(url):
    new_url_list = []
    val_href = get_href_list(url)
    val_titles = get_titles_list(url)
    for i in val_href:
        new_url_list.append(i.split())
        response_dict = dict(zip(val_titles, new_url_list))
    return response_dict

v = get_titles_and_href_dict(url)

def get_full_dict(url):
    response_list_text = []
    response_list_text_result = []
    titles = get_section_titles_href_from_rozetka(url)
    for i in titles:
        response_list_text.append(i.text)
    for i in response_list_text:
        val = re.findall(r'[А-Я]+[^А-Я]+', i)
        response_list_text_result.append(val[1:len(val)+1])
    resp_list_full = list(zip(get_href_list(url), response_list_text_result))
    resonse_dict_full = dict(zip(get_titles_list(url), resp_list_full))
    return resonse_dict_full

b = get_full_dict(url)
