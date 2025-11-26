import pytest
from src.processing import filter_by_state
from src.processing import sort_by_date

@pytest.fixture
def unsorted():
    return [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

@pytest.mark.parametrize("sorted", [
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
])
def test_filter_by_state(unsorted: list[dict], sorted: list[dict]) -> list[dict]:
    assert filter_by_state(unsorted) == sorted


@pytest.fixture
def state():
    return ["CANCELED"]


@pytest.mark.parametrize("sorted_state", [
    [{'date': '2018-10-14T08:21:33.419441', 'id': 615064591, 'state': 'CANCELED'},
     {'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'}]
])
def test_filter_by_state(unsorted_list: list[dict], state: str, sorted_state: list[dict]) -> list[dict]:
    assert sort_by_date(unsorted_list, state) == sorted_state


@pytest.fixture
def without_state():
    return [
        {'id': 41428829, 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'date': '2018-10-14T08:21:33.419441'}
]


@pytest.mark.parametrize("expected", [
    [{'date': '2019-07-03T18:35:29.512364', 'id': 41428829},
     {'date': '2018-10-14T08:21:33.419441', 'id': 615064591},
     {'date': '2018-09-12T21:27:25.241689', 'id': 594226727},
     {'date': '2018-06-30T02:08:58.425572', 'id': 939719570}]
])
def test_filter_by_state(without_state: list[dict], expected: list[dict]) -> list[dict]:
    assert sort_by_date(without_state) == expected


@pytest.fixture
def unsorted_list():
    return [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


@pytest.mark.parametrize("sorted_list", [
    [{'date': '2019-07-03T18:35:29.512364', 'id': 41428829, 'state': 'EXECUTED'},
     {'date': '2018-10-14T08:21:33.419441', 'id': 615064591, 'state': 'CANCELED'},
     {'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
     {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}]
])
def test_sort_by_date(unsorted_list: list[dict], sorted_list: list[dict]) -> list[dict]:
    assert sort_by_date(unsorted_list) == sorted_list


@pytest.fixture
def reverse():
    return False


@pytest.mark.parametrize("sorted_reverse", [
    [{'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'},
     {'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
     {'date': '2018-10-14T08:21:33.419441', 'id': 615064591, 'state': 'CANCELED'},
     {'date': '2019-07-03T18:35:29.512364', 'id': 41428829, 'state': 'EXECUTED'}]
])
def test_sort_by_date(unsorted_list: list[dict], reverse: bool, sorted_reverse: list[dict]) -> list[dict]:
    assert sort_by_date(unsorted_list, reverse) == sorted_reverse