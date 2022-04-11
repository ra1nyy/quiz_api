# QUIZ api
 
<h2>Схема базы данных</h2>
<img width="729" alt="image" src="https://user-images.githubusercontent.com/69690237/162806727-13a33d3b-eb08-4c28-bb27-da35064ada44.png">

<h2>Роутинг</h2>

- POST .../api/v1/account/token
Роут для получения токена. В проекте используется JWT-токен
Пример тела запроса:
```json
{
    "username": "ra1ny_test",
    "password": "5252"
}
```
- POST .../api/v1/account/register
Роут для регистрации пользователя.
Пример тела запроса:
```json
{
    "username": "ra1ny_test",
    "password": "5252",
    "first_name": "Руслан"
}
```

- POST .../api/v1/lecture/start_studying и .../api/v1/lecture/finish_studying
Роут для начала начала/завершения изучения лекции
Пример тела запроса:
```json
{
    "lecture": "4662dc58-b8e9-11ec-b909-0242ac120002",
    "user": "1"
}
```

- GET .../api/v1/lecture/<pk>
Роут для получения текста лекции. Возвращает текст лекции только в случае, если пользователь изучает именно эту лекцию
 
- GET .../api/v1/study_program/
Роут для получения программы обучения (всех этапов)
 
- GET .../api/v1/quiz/<pk>
Роут для получения теста с вопросами
Пример ответа:
```json
{
    "id": "6f602a4c-b9a8-11ec-8422-0242ac120002",
    "questions": [
        {
            "id": "e20efa82-b9a8-11ec-8422-0242ac120002",
            "question": "Что такое денди ?",
            "type": "text",
            "answer_options": null
        },
        {
            "id": "e47d1ee8-b9a8-11ec-8422-0242ac120002",
            "question": "Что такое пудж ?",
            "type": "one_answer",
            "answer_options": {
                "1": "Герой доты",
                "2": "Игра"
            }
        },
    ]
}
```
 
- POST .../api/v1/quiz/<pk>
Роут для отправки результата теста
Пример тела запроса:
```json
{
     "answers_dict" : 
     {
         "e20efa82-b9a8-11ec-8422-0242ac120002": "Яблоко",
         "e47d1ee8-b9a8-11ec-8422-0242ac120002": [1, 2, 3]
     }  
}
```
