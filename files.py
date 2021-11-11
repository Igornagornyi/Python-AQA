import re
import requests

# url = "https://rozetka.com.ua/ua/sport-i-uvlecheniya/"

# def get_response(url):
    # respond_text = ''
    # section_tag = 'class="tile-cats__heading ng-star-inserted'
    # respond = requests.get(url)
    # sections_dict = {}

    #Шаблон для нахождения разделов розетка
def get_section_pattern():
    section_pattern = re.compile('>\s?(.+?)\s?</a>')
    return section_pattern

    #Шаблон для нахождения подразделов и url розетка
def get_subsection_pattern():
    subsection_pattern = re.compile('a _ngcontent-sc.+?href="(.+?)".+?class="">\s?(.+?)\s?</a>')
    return subsection_pattern

    #Нахождение разделов розетка
def get_section_found():
    with open('rozetka.html', encoding='utf-8') as f:
        for section_text in f.read().split('class="tile-cats__heading ng-star-inserted"'):
            section_found = get_section_pattern().search(section_text)
        return section_found

er = get_section_found()
print(er)

    #Создание списка
def get_section_data():
    if get_section_found():
        section_data = []
        return section_data

eo = get_section_data()
print(eo)

    #Получение названий подразделов и url для словаря
def get_subsection_titles_href():
    with open('rozetka.html', encoding='utf-8') as f:
        for section_text in f.read().split('class="tile-cats__heading ng-star-inserted"'):
            for subsection in get_subsection_pattern().finditer(section_text):
                if subsection:
                    get_section_data().append(subsection.groups())
            return get_section_data()

nm = get_subsection_titles_href()
print(nm)

def write_file():
    with open('rozetka.html', encoding='utf-8') as f:
        sections_dict = {}
        if get_subsection_titles_href():
            sections_dict.setdefault(get_section_found().groups()[0], tuple(get_section_data()))
            get_section_data().clear()
            with open('files.txt', 'w') as f:
                for k, v in sections_dict.items():
                    f.writelines('\n')
                    f.writelines(k.center(120, '-'))
                    f.writelines('\n')
                    for i in v:
                        f.writelines('\n')
                        f.writelines(i[1].ljust(50, '.'))
                        f.writelines(i[0].rjust(50))
                        f.writelines('\n')


if __name__ == '__main__':
    write_file()

write_file()
