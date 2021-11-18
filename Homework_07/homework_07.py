import re

# Шаблон для названий разделов
section_pattern = re.compile('>\s?(.+?)\s?</a>')

# Шаблон для назв. подразделов и url
subsection_pattern = re.compile('a _ngcontent-sc.+?href="(.+?)".+?class="">\s?(.+?)\s?</a>')


# Сбор данных для словаря
def complete_dict():
    with open('rozetka.html', encoding='utf8') as f:
        sections_dict = {}
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
        return sections_dict

    # Запись данных розетки в файл


def write_file():
    with open('files.txt', 'w') as f:
        for k, v in complete_dict().items():
            f.write('\n')
            f.write(k.center(120, '-'))
            f.write('\n')
            for i in v:
                f.write('\n')
                f.write(i[1].ljust(50, '.'))
                f.write(i[0].rjust(50))
                f.write('\n')


if __name__ == '__main__':
    write_file()

