from xml.etree import ElementTree


def xml_parse():
    my_movies = []
    tree = ElementTree.parse("movies.xml")
    root = tree.getroot()
    genres = root.findall("genre")
    for genre in genres:
        my_movies.append(genre.attrib["category"])
        for decade in genre.findall("decade"):
            my_movies.append(decade.attrib["years"])
            for movie in decade.findall("movie"):
                my_movies.append(movie.attrib["title"])
                for format in movie.findall("format"):
                    my_movies.append(format.text)
                    for year in movie.findall("year"):
                        my_movies.append(int(year.text))
                        for rating in movie.findall("rating"):
                            my_movies.append(rating.text)
                            for description in movie.findall("description"):
                                my_movies.append([description.text.strip()])
        return my_movies
