# Привет, это мое решение на тестовое задание на должность Python-developer в "Фабрика решений". 
На вашем компьютере должен быть установлен Python и Redis.
## Для запуска, необходимо: 
1. Склонировать репозиторий:
```
https://github.com/podverta/api_test.git
```
2. Перейти в директорию и создать виртуальное окружение:
```
python -m venv venv
```
3. Активировать окружение:
```
source\venv\bin\activate
```
4. В корневом каталоге в файле .env добавить ваш токен TOKEN_API='<токен>'
5. Установить зависимости:
```
pip install -r .\requirements.txt 
```
6. Подготовить миграцию: 
```
python manage.py makemigrations  
```
7. Произвести миграцию: 
```sh
python manage.py migrate 
```
8. Запустить сервер Django:
```sh
python manage.py runserver 
```
9. Запустить Celery:
```
celery -A main_app worker --loglevel=INFO
```
10. Запустить Flower:
```
celery -A  main_app flower --port=5555
```


