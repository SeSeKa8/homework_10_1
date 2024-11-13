# Bank Operations Processing

## Цель проекта
Данный проект предоставляет функции для обработки банковских операций, включая фильтрацию по состоянию и сортировку по дате.

## Установка
1. Склонируйте репозиторий:
   ```
   git clone https://github.com/SeSeKa8/hw_10.1-Git.git
   ```
## Примеры использования
1. Сортировка по дате
```commandline
data = [
    {"id": 1, "state": "EXECUTED", "date": "2023-01-01"},
    {"id": 2, "state": "CANCELED", "date": "2023-01-02"}
]

sorted_data = sort_by_date(data, reverse=False)
print(sorted_data)
>>> [{'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'}, {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02'}]
```
2. Фильтрация по состоянию
```commandline
data = [
    {"id": 1, "state": "EXECUTED", "date": "2023-01-01"},
    {"id": 2, "state": "CANCELED", "date": "2023-01-02"}
]

filtered = filter_by_state(data, "EXECUTED")
print(filtered)
>>> [{'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'}]
```
