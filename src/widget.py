import re  # Регулярные выражения
from datetime import datetime  # Импорт для преобразования функции get_date

from src.masks import (  # Импорт для входных данных аргумента (преобразование в маску) из функции из masks.py
    get_mask_account,
    get_mask_card_number,
)


def mask_account_card(input_data: str) -> str:
    if not input_data or len(input_data.split()) < 2:
        return "Неверный формат"
    if input_data.startswith("Visa") or input_data.startswith("MasterCard"):
        try:
            return f"{input_data.split()[0]} {get_mask_card_number(input_data.split()[1])}"
        except ValueError:
            return "Неверный формат карты"
    if input_data.startswith("Счет"):
        try:
            return f"Счет {get_mask_account(input_data.split()[1])}"
        except ValueError:
            return "Неверный формат"
    return "Неверный формат"


def get_date(date_str: str) -> str:
    """
    Преобразует строку даты из формата ISO в формат ДД.ММ.ГГГГ.
    Возвращает ошибку, если дата некорректна.
    """
    if not date_str:
        return "Дата отсутствует"

    try:
        date = datetime.fromisoformat(date_str)
        return date.strftime("%d.%m.%Y")
    except ValueError:
        return "Неверный формат даты"
