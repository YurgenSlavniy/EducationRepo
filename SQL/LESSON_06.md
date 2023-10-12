# УРОК 6

# SELECT ЗАПРСЫ
Сервисы по генерации данных. _http://filldb.info/_ нажимаем красную кнопку `START HERE` вводим в открывшееся поле DDL команды попробывать в режиме инкогнито. Cайт работает очень нестабильно.В сервисе надо данные генерировать по порядку, т.к таблицы взаимодействуют начинать надо с таблицы у которой нет зависимостей от других, но от которой зависимы другие таблицы после генерации, делаем экспорт и исполняем скрипт `в DBeaver`

# Разбор домашнего задания к 4 ому уроку:
```
------------------ Задача 1.
-- Заполнить все таблицы БД vk данными (по 10-100 записей в каждой таблице).
mysql> use vk;

-- запросы во все таблицы, вида:
INSERT INTO `users` (`id`, `firstname`, `lastname`, `email`, `phone`) VALUES ('1', 'Reuben', 'Nienow', 'arlo50@example.org', '9374071116');
INSERT INTO `users` (`id`, `firstname`, `lastname`, `email`, `phone`) VALUES ('2', 'Frederik', 'Upton', 'terrence.cartwright@example.org', '9127498182');
INSERT INTO `users` (`id`, `firstname`, `lastname`, `email`, `phone`) VALUES ('3', 'Unique', 'Windler', 'rupert55@example.org', '9921090703');
INSERT INTO `users` (`id`, `firstname`, `lastname`, `email`, `phone`) VALUES ('4', 'Norene', 'West', 'rebekah29@example.net', '9592139196');
INSERT INTO `users` (`id`, `firstname`, `lastname`, `email`, `phone`) VALUES ('5', 'Frederick', 'Effertz', 'von.bridget@example.net', '9909791725');
INSERT INTO `users` (`id`, `firstname`, `lastname`, `email`, `phone`) VALUES ('6', 'Victoria', 'Medhurst', 'sstehr@example.net', '9456642385');

-- а лучше использовать пакетную вставку:
INSERT INTO `likes` VALUES
('1','1','1','1988-10-14 18:47:39'),
('2','2','1','1988-09-04 16:08:30'),
('3','3','1','1994-07-10 22:07:03'),
('4','4','1','1991-05-12 20:32:08'),
('5','5','2','1978-09-10 14:36:01'),
('6','6','2','1992-04-15 01:27:31'),
('7','7','2','2003-02-03 04:56:27'),
('8','8','8','2017-04-24 09:30:19'),
('9','9','9','1974-02-07 20:53:55'),
('10','10','10','1973-05-11 03:21:40'),
('11','11','11','2008-12-17 13:03:56'),
('12','12','12','1995-07-17 21:22:38'),
('13','13','13','1985-09-07 23:34:21'),
('14','14','14','1973-01-27 23:11:53')
;

-- можно было воспользоваться сервисом генерации данных
https://filldb.info

------------------ Задача 2.
--  список имен (только firstname) пользователей без повторений в алфавитном порядке

mysql> select distinct firstname from users order by firstname;

-- вариант 2

mysql> select firstname from users
	group by firstname
	order by firstname;

------------------ Задача 3.
/*
Написать скрипт, отмечающий несовершеннолетних пользователей как неактивных (поле is_active = false).
При необходимости предварительно добавить такое поле в таблицу profiles со значением по умолчанию = true (или 1)
*/
-- добавим флаг is_active

mysql> ALTER TABLE vk.profiles ADD COLUMN is_active BIT DEFAULT 1;

-- сделать невовершеннолетних неактивными

mysql> UPDATE profiles
	SET is_active = 0
	WHERE (birthday + INTERVAL 18 YEAR) > NOW();

-- проверим не активных

mysql> select * from profiles
	where is_active = 0
	order by birthday;

-- проверим активных

mysql> select * from profiles
	where is_active = 1
	order by birthday;

------------------ Задача 4.
/* Написать скрипт, удаляющий сообщения «из будущего» (дата позже сегодняшней) */

-- добавим флаг is_deleted

mysql> ALTER TABLE messages ADD COLUMN is_deleted BIT DEFAULT 0;

-- отметим пару сообщений неправильной датой

mysql> update messages set created_at = now() + interval 1 year limit 2;

-- отметим, как удаленные, сообщения "из будущего"

mysql> update messages
	set is_deleted = 1
	where created_at > NOW();

/* -- физически удалим сообщения "из будущего" */ 

mysql> delete from messages where created_at > NOW()

-- проверим
mysql> select * from messages order by created_at desc;
```
# ЗАДАНИЕ 1. Заполнить БД данными. Таблицу usres можно заполнять командой INSERT:
```
mysql> INSERT IGNORE INTO `users` (`id`, `firstname`, `lastname`, `email`, `phone`) VALUES
('1', 'Mike', 'Taison', 'gern@ya.com', '89100987762');
mysql> INSERT IGNORE INTO `users` (`id`, `firstname`, `lastname`, `email`, `phone`) VALUES
('2', 'Gena', 'Svoy', 'notyvf@ya.com', '89090087762');
mysql> INSERT IGNORE INTO `users` (`id`, `firstname`, `lastname`, `email`, `phone`) VALUES
('3', 'Sveta', 'Svoy', 'grtyu@ya.com', '89090987932');...
```
таблица users - пакетная вставка
```
mysql> INSERT IGNORE INTO `users` VALUES
('12', 'Eva', 'Monsim', 'grtyb@ya.com', NULL, '89011667762'),
('13', 'Avin', 'Klein', 'gim@ya.com', NULL, '89011667162'),
('14', 'Yuri', 'Klein', 'buda@ya.com', NULL, '86711667762'),
('15', 'Elisa', 'King', 'rtyb@ya.com', NULL, '89011623462'),
('16', 'Anton', 'Popov', 'pop@ya.com', NULL, '89231667762'),
('17', 'Anton', 'Monsim', 'yban@ya.com',NULL, '89021667762');
```
# ЗАДАНИЕ 2. Вывести список имён (только firstname) пользователей без повторений в алфавитном порядке
```
SELECT DISTINCT firstname
	FROM users
	ORDER BY firstname;
```
- `DISTINCT` - чтобы без повторений. убирает дубликаты.
- `ORDER BY` - сортировка в алфавитном порядке

Альтернативный вариант решения: но как правило  `GROUP BY` идёт с агригирующими функциями
```
mysql> SELECT firstname
	FROM users
	GROUP BY firstname
	ORDER BY firstname;
```
# ЗАДАНИЕ 3. 
Написать скрипт отмечающий несовершеннолетних пользователей, как неактивных (поле is_active = false) предварительно добавить такое поле в таблицу profiles со значением по умолчанию = true (или 1)

Добавляем поле в таблицу
```
mysql> ALTER TABLE socialnet.profiles ADD COLUMN is_active BIT DEFAULT 1;
```

Делаем несовершеннолетних неактивными
```
mysql> UPDATE profiles
	SET is_active = 0
	WHERE (birthday + INTERVAL 18 YEAR) > NOW();
```
Пишем update запрос.
```
WHERE (birthday + INTERVAL 18 YEAR) > NOW()
```
Берём дату рождения прибавляем интервал 18 лет и если она окажется больше настоящей даты, то пользователь несовершеннолетний:

- INTERVAL - системная встроенная функция
- INTERVAL 18 YEAR . 18 - число. YEAR - единицы измерения

Проверим неактивных пользователей простым select запросом
```
SELECT * FROM profiles
	WHERE is_active = 0
	ORDER BY birthday;
```
Проверяем активных пользователей
```
SELECT * FROM profiles
	WHERE is_active = 1
	ORDER BY birthday;
```
# Использование типа данных `BIT`
Посмотрим варианты добавления столбца с разными типами данных
```
ALTER TABLE socialnet.profiles 
ADD COLUMN is_active_bool BOOL DEFAULT 1;

ALTER TABLE socialnet.profiles
ADD COLUMN is_active_boolian BOOLEAN DEFAULT 1;

ALTER TABLE socialnet.profiles
ADD COLUMN is_active_tinyint TINYINT(1) DEFAULT 1;

ALTER TABLE socialnet.profiles
ADD COLUMN is_active_char CHAR(1) DEFAULT 1;

ALTER TABLE socialnet.profiles
ADD COLUMN is_active_enum ENUM('true', 'false') DEFAULT 'true';

ALTER TABLE socialnet.profiles
ADD COLUMN is_active_enum2 ENUM('0', '1') DEFAULT 1;
```
`mysql` считает тип данных `bool` число в интервале от -128 до 128 `boolian` считается псевдонимом для `tinyint`, если мы добавим в эти поля значения отличные от 0 и 1, то они сохронятся и тогда будет ошибка данных. В поле с типом данных `BIT` мы не сможем сохранить иные значения кроме 0 и 1 `ENUM('true', 'false')` - строковые константы они занимают больше места чем биты 0 и 1 `ENUM('0', '1')` - также строка

# ЗАДАНИЕ 4.
Написать скрипт, удаляющий сообщения «из будущего» (дата позже сегодняшней)

физически удалим сообщения
```
DELETE FROM messages
WHERE created_at > NOW();
```
Альтернативное решение, когда удалённые данные ещё где то хронятся
```
ALTER TABLE messeges
ADD COLUMN is_deleted BIT DEFAULT 0;
```
создаём столбец is_deleted по умолчанию False - 0

Отметим пару сообщений неправильной датой
```
UPDATE messages
SET created_at = now() + interval 1 year
LIMIT 2;
```
Вместо `delete` запроса делаем update запрос и все сообщения из будущего отмечаем как True - 1
```
UPDATE messages
SET is_deleted = 1
WHERE created_at > NOW();
```
проверяем
```
SELECT * FROM messages ORDER BY created_at desc;
```

!!! В `DBreaver` можно вручную в таблице добавлять, менять данные !!!

*********************************************

# SELECT ЗАПРОСЫ
Запустил скрипт и установил Базу данных которую разбирают на уроке

Пользователь зарегестрировался, вошёл на свою страничку и первое что он видит страничка своего профиля т.е информация о себе. Наша БД организована так, что данные о пользователе разбросаны по разным таблицам. Если бы всё было в одной таблице запрос был бы прост
```
mysql> SELECT * FROM users WHERE id = 1;
```
Предположим нам надо собрать имя, фамилию, город и фото
```
mysql> SELECT
	firstname,
	lastname,
	'city',
	'main_photo'
	FROM users
	WHERE id = 88;
```
В таблице users есть только `firstname` и `lastname`, а информация `'city'`, `'main_photo'` в этой таблице нет `'city'` у нас находится в таблице `profiles` в колонке `hometown` мы заранее позаботились о связях между таблицами связь между `users и profiles` с помощью внешнего ключа поле `user_id` в `profiles` ссылается на `id` в таблице `users` по этой связи перейдём в `profiles` и спустимся в `hometown`
```
mysql> SELECT hometown FROM profiles WHERE user_id = 88;
```
это отдельный запрос, встроем его в общий запрос
```
mysql> SELECT
	firstname,
	lastname,
	(SELECT hometown FROM profiles WHERE user_id = 88) AS 'city',
	'main_photo'
	FROM users
	WHERE id = 88;
```
 Разбираемся с фото. в  `DBreaver` смотрим `ERD` диаграмму связи табличек фото находится в поле `filename` в таблице `media`. Мы же обращаемся к табличке `users`  из неё можем перейти по связи к табличке `profiles`, А потом из `profiles` в `media` по существующей связи
`profiles (photo_id)` связь с `media(id)`

Кликаем по связи в ERD диаграмме чтобы увидить связь photo_id ссылается на id в в таблице media
```
mysql> SELECT filename FROM media WHERE id = (
	SELECT photo_id FROM profiles WHERE user_id =1);
```
в `WHERE` приравниваем первичный ключ к внешнему сначала исполнится вложенный запрос `(SELECT photo_id FROM profiles WHERE user_id =1)`
внедряем в основной запрос :
```
mysql> SELECT
	firstname,
	lastname,
	(SELECT hometown FROM profiles WHERE user_id = 88) AS 'city',
	(SELECT filename FROM media WHERE id = (
	SELECT photo_id FROM profiles WHERE user_id = 88)) AS 'main_photo'
	FROM users
	WHERE id = 88;
```
мы сейчас решили задачу с помощью вложенных запросов.

 Можно заменить 88 на прямое обращение к таблице users к колонке `id : users.id` во вложенных запросах мы делаем ссылку на внешнюю таблицу весь запрос стал скалерированным. Внешняя таблица - users
```
mysql> SELECT
	firstname,
	lastname,
	(SELECT hometown FROM profiles WHERE user_id = users.id) AS 'city',
	(SELECT filename FROM media WHERE id = (
	SELECT photo_id FROM profiles WHERE user_id = users.id)) AS 'main_photo'
	FROM users
	WHERE id = 88;
```
Скалерированные запрос работают медленно

Выберем фотографии пользовтаеля
```
mysql> SELECT * FROM media;
```
Этим запросом выбрали все данные конкретизируем запрос
```
mysql> SELECT *
	FROM media
	WHERE user_id = 88;
```
теперь мы получили записи только пользователя 88, но не все из них фото мы заранее позаботились о поле `media_type_id`, который указывает на тип записи (поста) нам нужны только фото. зайдём в таблику media_type, фотографиям соответствует первый медиатип. с id = 1 фильтруем запрос ещё раз
```
mysql> SELECT *
	FROM media
	WHERE user_id = 88
	AND media_type_id = 1;
```
Если бы захотели получить видеозаписи мы позоботились о медиатипе заранее и для видео `media_type_id = 3`
```
mysql> SELECT *
	FROM media
	WHERE user_id = 88
	AND media_type_id = 3;
```
Если бы мы ранее не позаботились о `media_type_id` тогда бы мы могли ориентироваться на расширение поля filename файл должен заканчиваться .mp4 или .avi
```
mysql> SELECT *
	FROM media
	WHERE user_id = 88
	AND (filename LIKE '%.mp4'
	OR filename LIKE '%.avi');
```
В скобках указываем потому что иначе `OR` будет цеплять другие id у которых найдёт .avi не только 88 user_id

Посчитаем количество фотографий у нашего пользователя
```
mysql> SELECT COUNT(*)
	FROM media
	WHERE user_id = 88
	AND media_type_id = 1;
	COUNT(*) - аггригирующая функция
```
# Аггригирующие функции:

- `AVG` - среднее
- `MAX` - максимальное
- `MIN` - минимальное
- `COUNT` - количество, счётчик
- `SUM` - сумма

В общем случае аггригирующие функции используются вместе с группировкой

Рассмотрим пример где есть аггригирующие функции и группировка узнаем количество новостей каждого типа
```
mysql> SELECT * FROM media;
```
Мы видим разные медиатипы группируем всё по типу медиаданных
```
mysql> SELECT
	COUNT(*),
	media_type_id
	FROM media
	GROUP BY media_type_id;
```
Можем добавить информативности запросу
```
mysql> SELECT
	COUNT(*),
	media_type_id,
	(SELECT name FROM media_types WHERE id = media_type_id) AS 'type'
	FROM media
	GROUP BY media_type_id;
```
Cколько новостей у каждого пользователя.
```
mysql> SELECT
	COUNT(*),
	user_id
	FROM media
	GROUP BY user_id;
```
Группируем по пользователям `GROUP BY user_id`

Усложним запрос. Нам нужны только те пользователи, у которых более 1 медиазаписи

если пробуем следующим образом, то будет !!ошибка!!
```
mysql> SELECT
	COUNT(*),
	user_id
	FROM media
	WHERE COUNT(*) > 1
	GROUP BY user_id;

mysql> SELECT
	COUNT(*) AS cnt,
	user_id
	FROM media
	WHERE cnt > 1
	GROUP BY user_id;
```
Такой запрос также приводит к ошибке даже если придумаем псевдоним

`AS cnt` - результат работы аггрегирующей функции аггригирующая функция вычисляется после группировки

запрос который работает:
```
mysql> SELECT
	COUNT(*) AS cnt,
	user_id
	FROM media
	GROUP BY user_id
	HAVING cnt > 1;
```
`HAVING` умеет учитывать результаты группировки

### порядок выполнения запроса:
- `FROM media` - сначала мы обращаемся к таблице
- `WHERE cnt` > 1 - фильтруем данные
- `GROUP BY user_id` - группируем данные

получаем ошибку

- `FROM media` - сначала мы обращаемся к таблице
- `GROUP BY user_id` - группируем данные
- `HAVING cnt > 1;` - фильтруем данные после группировки

выбираем друзей пользователя
```
mysql> SELECT * FROM friend_requests;
```
нам нужны записи касающиеся конкретного пользователя
```
mysql> SELECT *
	FROM friend_requests
	WHERE initiator_user_id = 1
	OR target_user_id =1;
```
добавим фильтрацию по статусу дружбы
```
mysql> SELECT *
	FROM friend_requests
	WHERE initiator_user_id = 1
	OR target_user_id =1
	AND status = 'approved';
```
нам надо повысить приоритет логического ИЛИ (OR)
```
mysql> SELECT *
	FROM friend_requests
	WHERE (initiator_user_id = 1
	OR target_user_id =1)
	AND status = 'approved';
```
как получить только список друзей, только их id
```
mysql> SELECT  initiator_user_id
	FROM friend_requests
	WHERE target_user_id = 1
	AND status = 'approved';

mysql> SELECT  target_user_id
	FROM friend_requests
	WHERE initiator_user_id = 1
	AND status = 'approved';
```
нам нужно склеить результаты этих запросов
```
mysql> SELECT  initiator_user_id
	FROM friend_requests
	WHERE target_user_id = 1
	AND status = 'approved'
	UNION
	SELECT  target_user_id
	FROM friend_requests
	WHERE initiator_user_id = 1
	AND status = 'approved';
-->
initiator_user_id
4
3
10
```
получили список подтверждёных друзей пользователя

`UNION` - вертикальное объединение запросов нужно чтобы набор полей и количество типов данных совпадали в верхнем и нижнем запросе, объединёных `union`

### Выбираем новости друзей
Лента новостей - записи из таблицы media, которые относятся к друзьям
```
mysql> SELECT * FROM media;
```
Вывести все записи таблицы медиа

мы знаем что мои друзья 3, 4, 10
```
mysql> SELECT *
	FROM media
	WHERE user_id IN (3, 4, 10);
```
Проблема в том, что мы изначально не знаем список друзей, всё что мы знаем - собственный айдишник, а всё остальное нам надо получить динамически в процессе запроса можем использовать предыдущий запрос, внутри этого запроса, чтобы сперва исполнился вложенный запрос, который получит список айдишников подставить его в фильтрацию `WHERE`
```
mysql> SELECT *
	FROM media
	WHERE user_id IN (
	SELECT  initiator_user_id
	FROM friend_requests
	WHERE target_user_id = 1
	AND status = 'approved'
	UNION
	SELECT  target_user_id
	FROM friend_requests
	WHERE initiator_user_id = 1
	AND status = 'approved'
	) ;
```
добавляем туда же собственные новости OR user_id =1
```
mysql> SELECT *
	FROM media
	WHERE user_id IN (
	SELECT  initiator_user_id
	FROM friend_requests
	WHERE target_user_id = 1
	AND status = 'approved'
	UNION
	SELECT  target_user_id
	FROM friend_requests
	WHERE initiator_user_id = 1
	AND status = 'approved'
	) OR user_id =1;
```
Новости отсортируем в хронологическом порядке по убыванию. самые свежие вначале. Старенькие в конце `ORDER BY create_at DESC`;
```
mysql> SELECT *
	FROM media
	WHERE user_id IN (
	SELECT  initiator_user_id
	FROM friend_requests
	WHERE target_user_id = 1
	AND status = 'approved'
	UNION
	SELECT  target_user_id
	FROM friend_requests
	WHERE initiator_user_id = 1
	AND status = 'approved'
	OR user_id =1
	ORDER BY create_at DESC;
```
выбираем сообщения касающиеся отдельного пользователя
```
mysql> SELECT * FROM messeges;
```
показываем всю таблицу сообщений нам нужны только записи касаемые конкретного пользователя там где он был отправителем
```
mysql> SELECT *
	FROM messeges
	WHERE from_user_id = 1;
```
сообщение где он был получателем
```
mysql> SELECT *
	FROM messeges
	WHERE to_user_id = 1;
```
диалог между 2умя пользователями user_id = 1 и user_id = 2
```
mysql> SELECT * FROM messeges;
```
вся таблица сообщений диалог между 1 и 2 это где 1 был отправитель, 2 был получатель и где 2 был отправитель 1 был получатель
```
mysql> SELECT *
	FROM messeges
	WHERE from_user_id = 1 AND to_user_id = 2
	OR from_user_id = 2 AND to_user_id = 1;
```
отсортируем в хронологическом порядке
```
mysql> SELECT *
	FROM messeges
	WHERE from_user_id = 1 AND to_user_id = 2
	OR from_user_id = 2 AND to_user_id = 1
	ORDER BY created_at DESC;
```
Нужно реализовать функционал непрочитанных сообщений, идём в таблицу messeges и смотрим есть ли у нас поле, отвечающее за прочитанность и непрочитанность такого поля нет, надо его добавить можем это сделать через запрос
```
mysql> ALTER TABLE messeges ADD COLUMN read_messeges BIT DEFAULT 0;
```
Можно сделать в `DBreaver` в user interface:
- ЛП -> ПКМ по Колонки -> создать объект 'колонка'
появляется всплывающее окно где даём имя нашей колонке и настройки.

-  тип данных - `BIT`
-  `Not Null` - ставим галочку
-  по умолчанию `(DEFAULT)`- ставим 0 (все сообщения не прочитанные)
-  жмём OK

Чтобы это появилось в базе мы должны нажать save `save (правый нижний угол)` открылось окно с запросом
```
mysql> ALTER TABLE vk.messages ADD is_read BIT DEFAULT 0 NOT NULL;
```
жмём сохранить.

Теперь если мы хотим получить только непрочитанные сообщения
```
mysql> SELECT *
	FROM messeges
	WHERE to_user_id = 1
	AND is_read = 0;
```
У нас есть много сообщений от 8 к 1, теперь тобы сообщения стали прочитанные, нужно чтобы 1 зашла в диалог с 8, тогда значение в колонке is_read изменится на 1
```
mysql> UPDATE messeges
	SET is_read =1
	WHERE from_user_id = 8
	AND to_user_id = 1;
```
Выведим информацию о друзьях в определённом виде. Друзья пользователя с преобразованием пола и подсчётом возраста `user id, gender, age`  пол хотим получать понятным рускоязычным словом мужской, женский. А возраст надо преобразовывать, т.к у нас только дата рождения
```
mysql> SELECT
	user_id, gender, age
	FROM profiles;
```
фильтруем только друзей. возраст пока возьмём в ковычки
```
mysql> SELECT
	user_id, gender, 'age'
	FROM profiles
	WHERE user_id IN (
	SELECT  initiator_user_id
	FROM friend_requests
	WHERE target_user_id = 1
	AND status = 'approved'
	UNION
	SELECT  target_user_id
	FROM friend_requests
	WHERE initiator_user_id = 1
	AND status = 'approved'
	);
-->
user_id  gender     age
10	   m	    age
3          m	    age
4	   f	    age
```
Для вывода - мужской и женский можем организовать ветвление внутри select запроса
```
mysql> SELECT
	user_id,
	CASE(gender)
	WHEN 'f' THEN 'женский'
	WHEN 'm' THEN 'мужской'
	END AS gender,
	'age'
	FROM profiles
	WHERE user_id IN (
	SELECT  initiator_user_id
	FROM friend_requests
	WHERE target_user_id = 1
	AND status = 'approved'
	UNION
	SELECT  target_user_id
	FROM friend_requests
	WHERE initiator_user_id = 1
	AND status = 'approved'
	);
-->
user_i     gender	age
3	   мужской	age
4	   женский	age
10	   мужской	age
```
Осталось разобраться с возрастом `birthday` можем использовать встроенные функции `TIMESTAMPDIFF()` которая вычисляет разницу между двумя датами в определённых единицах измерения
```
mysql> SELECT
	user_id,
	CASE(gender)
	WHEN 'f' THEN 'женский'
	WHEN 'm' THEN 'мужской'
	END AS 'gender',
	TIMESTAMPDIFF(YEAR, birthday, NOW()) AS 'age'
	FROM profiles
	WHERE user_id IN (
	SELECT  initiator_user_id
	FROM friend_requests
	WHERE target_user_id = 1
	AND status = 'approved'
	UNION
	SELECT  target_user_id
	FROM friend_requests
	WHERE initiator_user_id = 1
	AND status = 'approved'
	);
-->
user_id       gender	 age
3	      мужской	  27
4	      женский	  41
10	      мужской	  44
```
