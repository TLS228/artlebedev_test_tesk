# artlebedev_test_tesk
## Описание проекта
artlebedev_test_tesk - это тестовое задание на вакансию Python разработчика в команию Артемия Лебедева

## Автор проекта:
*  [Никита Малумашвили](https://github.com/TLS228)

## Технологии
* Python 3.9
* Django
* Django Rest Framework
* Docker
* PostgreSQL
* Swagger

## Запуск проекта
1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:TLS228/artlebedev_test_tesk.git
```

```
cd artlebedev_test_tesk
```

2. Создать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
python3 -m pip install --upgrade pip
```

3. Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

4. В корне проекта необходимо создать файл .env со следующими данными:
```
POSTGRES_USER      #имя пользователя БД 
POSTGRES_PASSWORD  #пароль пользователя БД 
POSTGRES_DB        #название БД
DB_HOST            #имя контейнера, где запущен сервер БД
DB_PORT            #порт, по которому Django будет обращаться к БД 
DEBUG              #статус режима отладки (default=False)
ALLOWED_HOSTS      #список доступных хостов
```