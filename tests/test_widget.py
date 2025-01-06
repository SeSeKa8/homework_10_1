import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("input_data, expected", [
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),
    ("MasterCard 8765432187654321", "MasterCard 8765 43** **** 4321"),
    ("", "Неверный формат"),  # Ожидаемое значение для пустой строки
    ("Счет", "Неверный формат"),  # Ожидаемое значение для неполного ввода
    ("Visa abc123", "Неверный формат карты"),
    ("Счет abc123", "Неверный формат")
])
def test_mask_account_card(input_data, expected):
    assert mask_account_card(input_data) == expected



@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2019-07-03T18:35:29.512364", "03.07.2019"),
    ("", "Дата отсутствует"),
    ("not a date", "Неверный формат даты"),
    ("2024-02-30T12:00:00", "Неверный формат даты")
])

def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
