# Тестовое задание веб-программист (Python)

### Реализован эндпоинт, принимающий POST-запрос с параметрами:
* data = Текстовое содержимое файла
* name = Название файла

Результат сохраняется в Google drive

Пример запроса:

```POST server_url/api/v1/touch/
Content-Type: application/json

{

  "data": "content",

  "name": "filename"

}
```
Эндпоинт возвращает ответ:

```
{"id": created_file_id}
```
