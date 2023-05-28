**_Places Remember Application_**
 
 
**Цель:**

Создать веб-приложение, с помощью которого люди смогут хранить свои впечатления о посещаемых местах.
 
**Описание задачи:**

Пользователь заходит на сайт и видит страницу с кратким описанием сервиса. Также, он замечает кнопки “Войти с помощью Google” (или VK, на Ваше усмотрение), нажимая на которую Google/VK предлагает ему разрешить доступ к его базовой информации.

Он разрешает доступ, после чего должна открыться страница. В ее шапке будет имя и фотография (информация взята из профиля Google/VK), по центру страницы надпись “У вас нет ни одного воспоминания”, кнопка “Добавить воспоминание” (ее расположение на ваше усмотрение), при нажатии на которую должна открываться форма с возможностью указания места на карте, а также поле для ввода названия и поле для ввода комментария об этом месте.

Далее пользователь может нажать на кнопку “Сохранить”, после чего он снова попадает на домашнюю страницу со списком из этого элемента и возможностью добавлять новые места. Весь добавленный список мест будет отображаться на домашней странице.

На домашней странице пользователя также есть кнопка, позволяющая ему выйти из своего аккаунта. После выхода он должен попасть на приветственную страницу сервиса без возможности видеть список посещаемых мест. При повторной авторизации через Google/VK пользователь снова видит все свои добавленные места.


**Для запуска сервиса:**

1) создать ВК-приложение (stand-alone или веб-сайт). Базовые домены 127.0.0.0 и 0.0.0.0, доверенный redirect URI - пустой.
2) создать в корне проекта .env файл с ключами от ВК-приложения (VK_CLIENT_ID, VK_SECRET, VK_KEY)
3) docker compose build, docker compose up 
4) docker exec -it django_container /bin/bash, python manage.py test (для запуска тестов внутри контейнера)

**Не удалось выполнить :(**
1) Запуск тестов при новых коммитах реализован с использованием github actions.
2) В README проекта есть бейдж с текущим покрытием тестами
3) Приложение запускается на одном из облачных сервисов