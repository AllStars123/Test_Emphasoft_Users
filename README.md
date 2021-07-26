<h1>TestEmphasoft</h1>

Тестовое задание.
<br>CRUD для юзеров с токен аутентификацией.

<h2>CRUD для USERS</h2>

<ul>
<li>'api-token-auth/' : получение токена аутентификации. Который для остальных запросов нужно включать в headers запроса в поле Authorization, в формате "Bearer &lt;токен&gt" </li>
<li>'api/v1/users/': метод GET - получение списка всех пользователей, метод POST (доступен только для superuser) - создание нового пользователя.</li>
<li>'api/v1/users/{user_id}/': метод GET получение информации о конкретном пользователе, метод PATCH (доступен только для superuser и самого пользователя) - изменение данных пользователя, метод DELETE(доступен только для superuser) - удаление пользователя.</li>
</ul>

<h2>Tests</h2>

В приложении доступны тесты:

`python3 manage.py test`

<h2>Автор</h2>

<li>Пурнов Никита Олегович</li>


<h2>Запуск проекта</h2>

<ul>
<li>python3 -m venv venv</li>
<li>source venv/Scripts/activate</li>
<li>pip install -r requirements.txt</li>
<li>python3 manage.py test</li>
<li>python3 manage.py runserver</li>
</ul>


