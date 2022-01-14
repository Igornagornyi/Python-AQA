import pytest

from Homework_19_pytest.human import Human
from Homework_19_pytest.race import Race


@pytest.fixture
def asian() -> Race:
    return Race("asian")


@pytest.fixture
def afroamerican() -> Race:
    return Race("afroamerican")


@pytest.fixture
def european() -> Race:
    return Race("european")


@pytest.fixture
def human_asian(asian) -> Human:
    human = Human("George", 18, "male", asian)
    print("text from fixture setup")
    yield human
    print("here could be additional instructions from fixture teardown")


@pytest.fixture
def human_afroamerican(afroamerican) -> Human:
    human = Human("John", 23, "male", afroamerican)
    return human


@pytest.fixture
def human_european(european) -> Human:
    human = Human("Elizabeth", 40, "female", european)
    return human
