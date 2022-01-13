import pytest

from Homework_19_pytest.human import Human
from Homework_19_pytest.race import Race


@pytest.fixture
def asian() -> Race:
    yield Race("asian")


@pytest.fixture
def afroamerican() -> Race:
    yield Race("afroamerican")


@pytest.fixture
def european() -> Race:
    yield Race("european")


@pytest.fixture
def human_asian(asian) -> Human:
    human = Human("George", 18, "male", asian)
    yield human


@pytest.fixture
def human_afroamerican(afroamerican) -> Human:
    human = Human("John", 23, "male", afroamerican)
    yield human


@pytest.fixture
def human_european(european) -> Human:
    human = Human("Elizabeth", 40, "female", european)
    yield human
