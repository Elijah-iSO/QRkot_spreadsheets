<<<<<<< HEAD
# QRkot_spreadseets
=======
# Приложение для Благотворительного фонда поддержки котиков QRKot.

### Краткое описание
 
Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

Проекты
В Фонде QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.
Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.
Пожертвования
Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.
Пользователи
Целевые проекты создаются администраторами сайта. 
Любой пользователь может видеть список всех проектов, включая требуемые и уже внесенные суммы. Это касается всех проектов — и открытых, и закрытых.
Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.

### Запуск
Для установки и запуска приложения выполните последовательно команды ниже (из консоли)

Скачайте приложение:
```
git clone
```

Создание виртуального окружения, команда запускается из корневой директории приложения:
```
python3 -m venv venv
```

Активируйте виртуальное окружение(MacOS):
```
source venv/bin/activate
```

Установка пакетов, необходимых для работы приложения в виртуальное окружение
```
pip install --upgrade pip
```
pip install -r requirements.txt
```

Автоматическое создание миграций
```
alembic revision --autogenerate
```

Выполнение миграций
```
alembic upgrade head
```

Запуск
```
uvicorn app.main:app --reload
```

## Автор
ILYA OLEYNIKOV
GitHub:	https://github.com/Elijah-iSO
E-mail: oleynikovis@yandex.ru
>>>>>>> master
