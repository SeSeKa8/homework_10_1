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
    """Сортирует список операций по ключу date."""

    # Args:
    #     data (List[Dict[str, Any]]): Список операций в виде словарей.
    #     reverse (bool): Порядок сортировки. True — по убыванию, False — по возрастанию. По умолчанию True.
    #
    # Returns:
    #     List[Dict[str, Any]]: Отсортированный список операций.

    return sorted(data, key=lambda x: x.get("date") or "", reverse=reverse)


# ПроверкаЖ
if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            state="EXECUTED",
        )
    )
    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            reverse=False,
        )
    )
