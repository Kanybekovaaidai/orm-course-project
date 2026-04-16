# ORM Online Courses Project

## Описание
Проект представляет собой backend систему управления онлайн-курсами с использованием SQLAlchemy ORM и SQLite.

## Модели
- User
- Profile
- Course
- Student

## Связи
- One-to-One: User — Profile
- One-to-Many: User — Course
- Many-to-Many: Student — Course (через enrollments)

## Функциональность
- CRUD операции
- Поиск по email
- Получение связанных данных (courses пользователя, courses студента)

## Запуск
pip install sqlalchemy
python main.py

## Пример работы

После запуска:
- создаются таблицы
- добавляются пользователи, курсы и студенты
- выполняются запросы и CRUD операции
