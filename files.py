import re
import requests


url = "https://rozetka.com.ua/ua/sport-i-uvlecheniya/"
respond_text = ''
section_tag = 'class="tile-cats__heading ng-star-inserted'
respond = requests.get(url)
sections_dict = {}
section_pattern = re.compile('>\s?(.+?)\s?</a>')
subsection_pattern = re.compile('a _ngcontent-sc.+?href="(.+?)".+?class="">\s?(.+?)\s?</a>')

with open('rozetka.html', encoding='utf-8') as f:
    for section_text in f.read().split('class="tile-cats__heading ng-star-inserted"'):
        section_found = section_pattern.search(section_text)
        if section_found:
            section_data = []
            for subsection in subsection_pattern.finditer(section_text):
                if subsection:
                    section_data.append(subsection.groups())
            if section_data:
                sections_dict.setdefault(section_found.groups()[0], tuple(section_data))
            section_data.clear()
v = 0

with open('files.txt', 'w') as f:
    for k, v in sections_dict.items():
        f.writelines('\n')
        f.writelines(k.center(120, '-'))
        f.writelines('\n')
        for i in v:
            f.writelines(i[1].ljust(50, '.'))
            f.writelines(i[0].rjust(50))
            f.writelines('\n')


