import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_number, expected", [("1234567812345678", "1234 56** **** 5678"),
                                                   ("1111222233334444", "1111 22** **** 4444"),
                                                   ("0000111122223333", "0000 11** **** 3333"),])

# Положительный тест на стандартную работоспособность
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

def test__get_mask_card_number_empty():
    with pytest.raises(AssertionError, match="Наберите номер банковской карты"):
        get_mask_card_number("")

def test_get_mask_card_number_incorrect_number():
    with pytest.raises(ValueError):
        get_mask_card_number("11112222333344445")
        get_mask_card_number("111122223333440")
        get_mask_card_number("")

def test_get_mask_card_number_if_letters():
    with pytest.raises(ValueError):
        get_mask_card_number("111f2222F3334A4L")

@pytest.mark.parametrize("account_number, expected", [("12345678901234567890", "**7890"),
                                                      ("98765432109876543210", "**3210"),
                                                      ("00000000000000000001", "**0001"),])
# Положительный тест на стандартную работоспособность
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected

# Обработка исключений: длина больше/меньше, доп. символы, буквы
def test_get_mask_account_incorrect_number_and_invalid():
    with pytest.raises(ValueError):
        get_mask_account("1111122222333334444")
        get_mask_account("111112222233333444445")
        get_mask_account("12a34")
        get_mask_account("12a!./34")
