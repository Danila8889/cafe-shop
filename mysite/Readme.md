Основное приложение находится в директории mysite, там же и Dockerfile для развертывания и деплоя

В mysite содержится два приложения сafe и mysite

 - mysite основное и содержит настройки

 - cafe содержит логику приложения, весь фунцкционал
 

Для запуска переходим в корневую директорию mysite и пишем в bash: python manage.py runserver


Для доступа в админку

  username: admin
  password: 123

В приложении cafe есть папка api_v1 для создания API заказов

URL адреса делятся на три категории:
   pk - первичный ключ модели

 - http://127.0.0.1:8000/cafe/orders/ - заказы

 - http://127.0.0.1:8000/cafe/order/{pk}/detail/ - заказ


 - http://127.0.0.1:8000/cafe/tables/ - столики

 - http://127.0.0.1:8000/cafe/table/1/detail/ - столик


 - http://127.0.0.1:8000/cafe/api/orders/ - API django rest framework для заказов


 Так же в приложении cafe есть фикстуры для тестов, templates, где лежат html-шаблоны, models - модели БД, tests - тесты, mixins - миксины
 forms - формы для POST-запросов





