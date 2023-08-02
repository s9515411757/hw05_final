### Сообщество

```shell
Цель проекта: создать сервис с сообществом, где можно создавать посты и комментрировать их и подписываться на авторов 
```

==========================================================================

## Установка
1) Самый простой способ:
```shell
git clone https://github.com/s9515411757/hw05_final.git
```

2) Или через PyCharm:
- нажмите на кнопку **Get from VCS**:
![alt text]([https://raw.githubusercontent.com/WISEPLAT/imgs_for_repos/master/get_from_vcs.jpg ](https://github.com/s9515411757/hw05_final.git))

Вот ссылка на этот проект:
```shell
https://github.com/s9515411757/hw05_final.git
```
3) В PyCharm по умолчанию создается виртуальное окружение, если оно у вас не создалось, то следует воспользоваться командой для Windows:
```shell
python3 -m venv venv
или
python -m venv venv 
```
Если вы хотите использовать в работе определённую версию Python, добавьте к команде создания виртуального окружения номер этой версии. Пример:
```shell
python3.8 -m venv venv
```
4) Запускаем виртуальное окружение. Если venv вашего проекта деактивировано, активируйте его, введите команду:
```shell
# Для Windows:
source venv/Scripts/activate
или
venv/Scripts/activate

# Для Linux и macOS:
source venv/bin/activate 
```

5) Устанавливаем библиотеки, перед установкой следует обновить PIP:
```shell
python.exe -m pip install --upgrade pip

pip install -r requirements.txt
```
==========================================================================

## Python версия 3.7-3.9
Библиотеки:
```shell
Django==2.2.16
mixer==7.1.2
Pillow==8.3.1
pytest==6.2.4
pytest-django==4.4.0
pytest-pythonpath==0.7.3
requests==2.26.0
six==1.16.0
sorl-thumbnail==12.7.0
Faker==12.0.1
```
==========================================================================

## Лицо сайта
![alt text](https://github.com/s9515411757/hw05_final/blob/master/1.png)

## Форма регистрации
![alt text](https://github.com/s9515411757/hw05_final/blob/master/2.png)

## После авторизации создаем свой тестовый пост
![alt text](https://github.com/s9515411757/hw05_final/blob/master/3.png)

## Как отображается пост с добавлением картинки
![alt text](https://github.com/s9515411757/hw05_final/blob/master/4.png)

## Отображение комментария
![alt text](https://github.com/s9515411757/hw05_final/blob/master/5.png)
