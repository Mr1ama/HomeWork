# Клуб будущего

Учебный сайт с панелью мероприятий и API на FastAPI.

## Запуск

Установите зависимости:

```bash
python -m pip install -r requirements.txt
```

Запустите сервер из папки `future_club`:

```bash
python -m uvicorn main:app --reload
```

## Маршруты

| Метод | Путь | Описание |
|---|---|---|
| GET | `/` | Страница со всеми мероприятиями |
| GET | `/api/events` | Все мероприятия в JSON |
| GET | `/api/events/open` | Мероприятия с открытой регистрацией |
| GET | `/docs` | Swagger-документация |
