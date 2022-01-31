from root import xml_parse

from movie import Movie

if __name__ == '__main__':
    movie_1 = xml_parse()[0:7]
    movie_2 = xml_parse()[7:14]
    print(Movie.from_root(movie_1))
    print(Movie.from_root(movie_2))
