from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует список операций по указанному значению ключа state."""

    # Args:
    #     data (List[Dict[str, Any]]): Список операций в виде словарей.
    #     state (str): Значение ключа state для фильтрации. По умолчанию 'EXECUTED'.
    #
    # Returns:
    #     List[Dict[str, Any]]: Список операций, соответствующих заданному состоянию.

    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список операций по ключу date, с обработкой некорректных дат."""

    # Args:
    #     data (List[Dict[str, Any]]): Список операций в виде словарей.
    #     reverse (bool): Порядок сортировки. True — по убыванию, False — по возрастанию. По умолчанию True.
    #
    # Returns:
    #     List[Dict[str, Any]]: Отсортированный список операций.

    def parse_date(date_str: str) -> datetime:
        """Попытка распарсить строку в объект datetime. Возвращает None, если не удалось."""
        try:
            # Пробуем распарсить дату, включая возможный формат без секунд
            return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            try:
                # Если не получилось с миллисекундами, пробуем без них
                return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
            except ValueError:
                # Если не удается распарсить, возвращаем None
                return None


    def get_date(item: Dict[str, Any]) -> datetime:
        """Получает дату для сортировки, заменяет некорректную дату на None."""
        date_str = item.get("date")
        if date_str:
            return parse_date(date_str)
        return None

    # Сортировка с учетом корректности даты
    return sorted(data, key=lambda x: (
        get_date(x) is not None,  # Помещаем записи с некорректной датой в конец
        get_date(x) or datetime.min,  # Для корректных дат — сами даты
        x.get("id", 0)  # Для одинаковых дат сортируем по id
    ), reverse=reverse)
