import pytest
from one_hot_encoder import fit_transform


def test_part():
    expected = [('Moscow', [0, 0, 1]), ('New York', [0, 1, 0]), ('Moscow', [0, 0, 1]), ('London', [1, 0, 0])]
    assert fit_transform(['Moscow', 'New York', 'Moscow', 'London']) == expected


def test_instance():
    actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
    assert isinstance(actual[0], tuple)


def test_ft():
    assert fit_transform('Cheese') == [('Cheese', [1])]


def test_len():
    words = ['Moscow', 'New York', 'Moscow', 'London']
    actual = len(fit_transform(words)[0][1])
    expected = len(set(words))
    assert actual == expected


def test_error():
    with pytest.raises(TypeError):
        fit_transform()
