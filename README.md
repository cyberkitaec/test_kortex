<h1> Задание </h1>

Реализовать следующие сущности БД:
<ul> <h2> <strong> Исполнитель </strong> </h2>
  <li>Наименование исполнителя</li>
</ul>

<ul><h2> <strong> Альбом</strong></h2>
  <li>Наименование альбом</li>
  <li>Год выпуска</li>
  <li>Исполнитель(FK)</li>
</ul>

<ul>
  <h2><strgong>  Песня </strgong></h2>
  <li> Наименование песни</li>
  <li> Порядковый номер в альбоме</li>
  <li> Альбом(FK)</li>
</ul>

Реализовать RESTful API. В качестве базы данных должна использоваться MySQL.

<h1> Стэк технологий</h1>
<ul>
 <li> Python 3.9.13</li>
  <li> Django 4.2</li>
  <li> DRF </li>
</ul>

<h1> Установка и запуск </h1>
<p>Создайте виртуальную среду</p>
<code> python -m venv env </code>
<p>Активируйте виртуальную среду</p>
<code> .\env\Scripts\activate </code>
<p> Клонируйте репозиторий </p>
<code> git clone https://github.com/cyberkitaec/test_kortex.git</code>
<p> Установка зависимостей</p>
<code>pip install -r requirements.txt</code>
<p> Запуск проекта</p>
<code>cd cortex</code>
<code>python manage.py runserver</code>
