from datetime import datetime # Импорт для преобразования функции get_date
from masks import get_mask_account, get_mask_card_number # Импорт для входных данных аргумента (преобразование в маску) из функции из masks.py
import re # Регулярные выражения

def mask_account_card(account: str) -> str:
    """Функция маскирует номер карты или счета в зависимости от типа"""
    if "Счет" in account:
        # # Маскировка для счета, скрываем все, кроме последних 4 цифр
        return f"Счет {get_mask_account(account)}"
    else:
        # Маскировка для карт, сохраняем первые 4, последние 4, остальные заменяем на *
        numbers = get_mask_card_number(''.join(re.findall(r'\d', account)))
        return ''.join(item for item in account if item.isalpha()) + " " + numbers

def get_date(date_str: str) -> str:
    """
    Преобразует строку даты из формата ISO в формат ДД.ММ.ГГГГ.

    :param date_str: Дата в формате "ГГГГ-ММ-ДДTЧЧ:ММ:СС"
    :return: Строка с датой в формате ДД.ММ.ГГГГ
    Ввод: "2024-03-11T02:26:18.671407"
    """
    date = datetime.fromisoformat(date_str)
    return date.strftime("%d.%m.%Y")

# Используем функции
if __name__ == "__main__":

    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(get_date("2024-03-11T02:26:18.671407"))

# Примеры входных данных для проверки функции
# Maestro 1596837868705199
# Счет 64686473678894779589
# MasterCard 7158300734726758
# Счет 35383033474447895560
# Visa Classic 6831982476737658
# Visa Platinum 8990922113665229
# Visa Gold 5999414228426353
# Счет 73654108430135874305
