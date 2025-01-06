# Теперь импортируем функции из masks.py
from src.masks import get_mask_account, get_mask_card_number

# Используем функции
if __name__ == "__main__":
    # Пример вызова функций
    card_number = 7000792289606361
    account_number = 73654108430135874305

    print(get_mask_card_number(str(card_number)))
    print(get_mask_account(str(account_number)))
