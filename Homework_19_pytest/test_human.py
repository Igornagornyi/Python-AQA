import pytest


def test_check_return_value_for_name_property(human_asian):
    assert human_asian.name == "George"


def test_check_return_value_for_age_property(human_afroamerican):
    assert human_afroamerican.age == 23


def test_check_return_value_for_gender_property(human_european):
    assert human_european.gender == "female"


def test_check_value_for_grow_method(human_european):
    assert human_european.grow() == 41


def test_check_value_for_change_name_method(human_asian):
    assert human_asian.change_name("Lee") == "Lee"


def test_check_value_for_change_gender_method(human_afroamerican):
    assert human_afroamerican.change_gender("female") == "female"


def test_check_for_validate_gender_raise_exception(human_afroamerican):
    with pytest.raises(Exception):
        assert human_afroamerican.change_gender("something wrong")


def test_check_for_change_name_raise_exception(human_european):
    with pytest.raises(Exception):
        assert human_european.change_name("Elizabeth")
