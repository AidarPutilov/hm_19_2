## Домашняя работа 20.1
- Работа продолжена в проекте домашней работы 19.2
- Создана БД les_20_1 в ручном режиме, внесены настройки подключения.
- Созданы модели Product и Category, описаны начальные настройки.
- Для каждой модели описаны поля.
- Перенесено отображение моделей в базу данных с помощью инструмента миграций.
- Настроена административная панель для отображения моделей категории и продукта.
- Через инструмент shell заполнен список категорий, сделаны выборки с произвольными фильтрами. Решение в скриншотах.
- Сформированы фикстуры для заполнения БД.
- Написана кастомная команда fill, которая заполняет БД, предварительно очистив её.

### Применённые пакеты
- django
- ipython
- pillow
- psycopg2-binary

### Инструкция для развертывания проекта

#### Клонирование проекта:
```
git clone https://github.com/AidarPutilov/hm_19_2.git
cd hm_19_2
```
#### Первоначальные настройки:
- Ввести настройки сервера PostgreSQL в файле config.py.
- Создать базу данных les_20_1.
- Создать миграции, применить миграции.
- Заполнить БД командой
```
Windows: python manage.py fill
Linux, MacOS: python3 manage.py fill
```
- Задать логин и пароль администратора
```
Windows: python manage.py createsuperuser
Linux, MacOS: python3 manage.py createsuperuser
```
#### Запуск сервера:
```
Windows: python manage.py runserver
Linux, MacOS: python3 manage.py runserver
```
#### Запуск страницы:
```
http://127.0.0.1:8000/
```
#### Административная страница:
```
http://127.0.0.1:8000/admin/
```
### Автор
Айдар Путилов