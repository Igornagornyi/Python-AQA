from __future__ import annotations

from typing import List


class Movie:

    def __init__(
            self,
            category: str,
            decade: str,
            title: str,
            formt: str,
            year: int,
            rating: str,
            description: str
    ) -> None:
        self.__category = category
        self.__decade = decade
        self.__title = title
        self.__format = formt
        self.__year = year
        self.__rating = rating
        self.__description = description

    @classmethod
    def from_root(cls, line: List):
        return cls(*line)

    def __str__(self):
        start = "{"
        content = ""
        end = "}"
        for key, value in self.__dict__.items():
            content += f"\t{key.replace(f'_{self.__class__.__name__}__', '')}: {value}\n"
        return f"{start}{content}{end}"
