import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def sample_data():
    return [
        {'date': '2019-07-03T18:35:29.512364', 'id': 1, 'state': 'EXECUTED'},
        {'date': '2018-06-30T02:08:58.425572', 'id': 2, 'state': 'CANCELED'},
        {'date': '2018-09-12T21:27:25.241689', 'id': 3, 'state': 'EXECUTED'},
        {'date': '2020-01-01T12:00:00.000000', 'id': 4, 'state': 'EXECUTED'},
    ]

# Положительный тест на стандартную работоспособность
def test_filter_by_state(sample_data):
    filtered = filter_by_state(sample_data, state="EXECUTED")
    assert len(filtered) == 3
    assert all(item["state"] == "EXECUTED" for item in filtered)

# Пустой
def test_filter_by_state_empty():
    assert filter_by_state([]) == []

# Отсутствующие данные
def test_filter_by_state_no_matches(sample_data):
    filtered = filter_by_state(sample_data, state="NON_EXISTENT")
    assert filtered == []

# Положительный тест на стандартную работоспособность
def test_sort_by_date(sample_data):
    sorted_data = sort_by_date(sample_data)
    assert sorted_data[0]["date"] == "2020-01-01T12:00:00.000000"
    assert sorted_data[-1]["date"] == "2018-06-30T02:08:58.425572"
    # Проверяем сортировку по id для одинаковых дат
    assert sorted_data[-2]["id"] > sorted_data[-3]["id"]

# Пустой
def test_sort_by_date_empty():
    assert sort_by_date([]) == []

# Отсутствует дата
def test_sort_by_date_missing_date(sample_data):
    sample_data.append({"id": 5, "state": "EXECUTED"})  # Без даты
    sorted_data = sort_by_date(sample_data)
    assert sorted_data[-1]["id"] == 5  # Запись без даты — последняя

# Тест на некорректный формат даты
def test_sort_by_date_invalid_format():
    sample_data = [
        {"id": 1, "state": "EXECUTED", "date": "2020-13-01T12:00:00.000000"},  # Некорректный месяц
        {"id": 2, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    sorted_data = sort_by_date(sample_data)
    # Проверяем, что некорректная дата окажется в конце списка
    assert sorted_data[0]["date"] == "2019-07-03T18:35:29.512364"
    assert sorted_data[-1]["date"] == "2020-13-01T12:00:00.000000"

# Тест на строку вместо даты
def test_sort_by_date_non_date_string():
    sample_data = [
        {"id": 1, "state": "EXECUTED", "date": "not a date"},  # Строка вместо даты
        {"id": 2, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    sorted_data = sort_by_date(sample_data)
    # Строка "not a date" должна быть в конце списка
    assert sorted_data[0]["date"] == "2019-07-03T18:35:29.512364"
    assert sorted_data[-1]["date"] == "not a date"

# Тест на формат даты с часами и минутами
def test_sort_by_date_partial_date():
    sample_data = [
        {"id": 1, "state": "EXECUTED", "date": "2020-01-01T12:00"},
        {"id": 2, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    sorted_data = sort_by_date(sample_data)
    # Проверяем, что данные с полной датой должны быть выше в списке
    assert sorted_data[0]["date"] == "2019-07-03T18:35:29.512364"
    assert sorted_data[1]["date"] == "2020-01-01T12:00"
