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
                my_movies.append(movie[0].text)
                my_movies.append(movie[1].text)
                my_movies.append(movie[2].text)
                my_movies.append(movie[3].text.strip())

    return my_movies
