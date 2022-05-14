## Сервер для IT школы Samsung

Это - простой одностраничный сервер для тестирования клиента. Он развёрнут 
на heroku. 

Демонстрационная версия: <https://buran-it-sch.herokuapp.com>

Главная страница отображает список задач с указанием автора.

Чтобы добавить свои задачи в общий списко, необходимо отправить POST-запрос вида:

```
d = {
    "user": "test3",
    "tasks": [
        {
            "title": "task1",
            "text": "description 1",
            "solved": True
        },
        {
            "title": "task2",
            "text": "description 2",
            "solved": True
        },
        {
            "title": "task3",
            "text": "description 3",
            "solved": True
        },
    ]
}

res = requests.post("https://buran-it-sch.herokuapp.com/add", json=d)
print(res.content)
```

Все задачи, принадлежащие пользователю, имя которого получено по ключу "user", удаляются, после 
чего добавляются все, указанные в POST-запросе

