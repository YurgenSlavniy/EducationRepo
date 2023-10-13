# УРОК 8

# Решения задач с помощью объединения таблиц
Это можно делать с помощью `JOIN` круги элера (пересекающиеся круги) с их помощью часто объясняют объединения таблиц

Мы будем рассматривать на примере таблиц  `users` и `messeges`.  Эти таблицы связаны соотношением один ко многим. Один пользователь мог написать много сообщений при этом каждое сообщение имеет одного отправителя и одного получателя
- в таблице users есть колонка `id` - `id` - это первичный ключ
- в таблице messages  `user_id` - `user_id` - внешний ключ

Какие то пользователи написали несколько сообщений какие то пользоатели написали 1 сообщение, а какие то пользователи совсем не писали сообщений, а ещё будет ситуация, что в таблице `messeges` в колонке `user_id` будут NULL значения, вернее отсутствие значений это плохо, это неправильно, это ошибка в данных, но тем не менее ситуация такая сложилась такую ситуацию надо учитывать и мы её смоделируем
```
USERS         MESSAGES
| id |   |      | user_id|   |
|    |   |      |        |   |
|    |   |      |        |   |
|    |   |      |   NULL |   |
|    |   |      |        |   |
```
Порисуем сейчас разные варианты объединения таблиц

Cамый маленький способ объединения таблиц (по объему данных) `[INNER] JOIN` - внутреннее объединение, выводим те записи из левой таблицы, которым нашлось соответствие в правой и те записи из правой, которым нашлось соответствие в левой из `users` мы берём только те `id` которые псиали сообщения и только те сообщения у которых есть отправитель если взять 2 пересекающихся кружочка это зона пересечения кружков

Если мы захотим к этой выборке добавить пользователей которые не писали сообщений `LEFT [OUTER] JOIN` всё что входит в таблицу `users` целиком, а из правой таблицы только соответствия (всё что попадало в `INNER JOIN`)

Аналогичный `RIGHT [OUTER] JOIN` вторая таблица целиком и первая таблица область пересечения

Выборка которая включает обе таблицы целиком `FULL [OUTER] JOIN` способ объединения которого нет на кругах Эллера

`CROSS JOIN` (декартово произведение таблиц) каждая запись из левой таблицы выводится с каждой записью правой все возможные варианты

# !!ДЛЯ mysql FULL [OUTER] JOIN не реализован!!

На парктике. в `DBreaver`.
# CROSS JOIN
```
mysql> SELECT * FROM users, messages;
```
Мы получили таблицу в 10 000 строк:
- users - 100 строк
- messages - 100 строк

100 * 100 = 10 000 строк

- левые прля - все поля users,
- правые поля - все поля messages
```
mysql> SELECT COUNT(*) FROM users, messages;
```
получаем 10 000. 100 пользователей перемножили на 100 сообщений
```
mysql> SELECT * FROM users JOIN messages;
```
### альтернативная запись CROSS JOIN
```
mysql> SELECT *
	FROM users
	JOIN messages
	WHERE users.id = messages.from_user_id;
```
Добавляем фильттрацию `WHERE` от выборки остаются пользователи и их сообщения нам возвращают 100 строк, но это все ещё `CROSS JOIN`

чтобы этот запрос стал `INNER JOIN` `WHERE` меняется на `ON`
```
mysql> SELECT *
	FROM users
	JOIN messages
	ON users.id = messages.from_user_id;
```
- `CROSS JOIN` работает медленно
- `INNER JOIN` работает быстро
- `CROSS JOIN` сначала отрабатывает все записи потом фильтрует.
- `INNER` фильтрует записи в процессе отбора

Сценарии использования `CROSS JOIN` например нагрузочное тестирование через запятую перечисляем несколько таблиц, смотрят сколько времени он исполняется, как ведет себя сервер, как быстро он упадёт

Cценарии в котором нам нужны сами данные, если взять числа от 1 до 31, а в другой таблице числа от 1 до 12 => получится календарь

# СЦЕНАРИИ РАБОТЫ ПО УМОЛЧАНИЮ
для `SELECT` по умолчанию `ALL` (не `DISTINCT`) для `UNION` по умолчанию `DISTINCT` (не `ALL`) для `JOIN` по умолчанию `INNER` (не `OUTER`, не `CROSS`)

```
LEFT JOIN
mysql> SELECT *
	FROM users
	LEFT JOIN messages
	ON users.id = messages.from_user_id;
```
Совсем другой запрос, получим другую выборку в результате 116 строк получаем из них 100 которые были в INNER JOIN, 16 новых строк чтобы наглядно продемонстрировать сделаем сортировку
```
mysql> SELECT *
	FROM users
	LEFT JOIN messages
	ON users.id = messages.from_user_id
	ORDER BY messages.id;
```
Первые 16 строк это те строки которые добавились в `LEFT JOIN` это пользователи напротив которых в полях таблицы `messages` везде `NULL`, а следующие 100 строк те самые которые были в `INNER JOIN` с логической точки зрения  внашем запросе верхние 16 пользователей, те пользователи, которые не писали сообщений

Как оставить только эти 16 пользователей. Точнее только тех пользователей, которые не писали сообщений
```
mysql> SELECT *
	FROM users
	LEFT JOIN messages
	ON users.id = messages.from_user_id
	ORDER BY messages.id
	LIMIT 16;
```
Результат получим, но это не совсем корректное решение т.к цифру 16 мы заранее не знаем
```
mysql> SELECT users.*
	FROM users
	LEFT JOIN messages
	ON users.id = messages.from_user_id
	WHERE messages.id IS NULL
	ORDER BY messages.id
```
Этот запрос является частным случаем `LEFT JOIN`

# SQL JOINS

### LEFT JOIN в общем виде:
```
mysql> SELECT <select_list>
	FROM tableA A
	LEFT JOIN tableB B
	ON A.Key = B.Key;
```
### LEFT JOIN частный случай оставили только те записи, которым НЕ нашли соответствие в правой
```
mysql> SELECT <select_list>
	FROM tableA A
	LEFT JOIN tableB B
	ON A.Key = B.Key
	WHERE B.Key IS NULL;
```
### RIGHT JOIN в общем виде:
```
mysql> SELECT <select_list>
	FROM tableA A
	RIGHT JOIN tableB B
	ON A.Key = B.Key;
```
### RIGHT JOIN частный случай
```
mysql> SELECT <select_list>
	FROM tableA A
	RIGHT JOIN tableB B
	ON A.Key = B.Key
	WHERE A.Key IS NULL;

mysql> SELECT <select_list>
	FROM tableA A
	INNER JOIN tableB B
	ON A.Key = B.Key

mysql> SELECT <select_list>
	FROM tableA A
	FULL OUTER JOIN tableB B
	ON A.Key = B.Key

mysql> SELECT <select_list>
	FROM tableA A
	FULL OUTER JOIN tableB B
	ON A.Key = B.Key
	WHERE A.Key IS NULL OR B.Key IS NULL;
```
получим 2 одинаковых результата с помощью `LEFT` и `RIGHT JOIN`
```
-- LEFT JOIN
mysql> SELECT users.* , messages.*
	FROM users
	LEFT JOIN messages ON users.id = messages.from_user_id
	ORDER BY messages.id
-- RIGHT JOIN
mysql> SELECT users.* , messages.*
	FROM messages
	RIGHT JOIN users ON users.id = messages.from_user_id
	ORDER BY messages.id
```
Левая таблица та которая слева от `JOIN`, правая - спарва
- FROM messages LEFT JOIN users ON users.id = messages.from_user_id
- FROM users LEFT JOIN messages ON users.id = messages.from_user_id

`LEFT JOIN` и `RIGHT JOIN` - взаимозаменяемы

# FULL OUTER JOIN
Если бы мы находились не в mysql а любом другом СУБД (ORACLE, MS) то мы бы получили результат исполнив запрос
```
mysql> SELECT users.*, messages.*
	FROM users
	FULL JOIN messages ON users.id = messages.from_user_id
	ORDER BY messages.id;
```
В mysql мы получим ощибку поэтому нужны некоторые дополнительные манипуляции `FULL JOIN` когда пересекающиеся круги Эллера полностью закрашены в нём точно есть `INNER JOIN` + частные случаи `LEFT JOIN` и `RIGHT JOIN` нам может помочь вертикальное объединение `UNION` в `JOIN` мы добавляем новые колонки в `UNION` добавляются новые строки поэтому если сделать `UNION` для `LEFT JOIN` и `RIGHT JOIN` получим `FULL OUTER JOIN`
```
mysql> SELECT users.*, messages.*
	FROM users
	LEFT JOIN messages ON users.id = messages.from_user_id
	UNION
	SELECT users.*, messages.*
	FROM users
	RIGHT JOIN messages ON users.id = messages.from_user_id
```
Смоделируем ситуацию с `NULL` для поля `from_user_id` в таблице `messages` у нас появятся сообщения без отправителя
`в DBreaver` -> ЛП -> по таблице messages 2 клик ПКМ -> открываем вкладку Свойства (properietes), убираем галочку с колонки not NULL со строки `from_user_id` -> жмём save появляется всплывающее окно в нём запрос
```
ALTER TABLE vk.messages MODIFY COLUMN from_user_id bigint unsigned NULL;
```
жмём сохранить, теперь добавим несколько строк
```
mysql> INSERT INTO vk.messages
	(from_user_id, to_user_id, body, created_at)
	VALUES (NULL, 1, 'some text...', CURRENT_TIMESTAMP);
```
Во вкладке данные появились 2 строки у которых поле from_user_id имеет значение NULL

- INNER JOIN возвращает 100 строк
- LEFT OUTER JOIN возвращает 116 строк
- RIGHT OUTER JOIN возвращает 102 строки
- FULL [OUTER] JOIN возвращает 118 строк

Если в `INNER` 100 строк, а в `LEFT` 116 то из этих 116, 100 строк это из INNER, а 16 добавляются `LEFT JOIN`ом, в `RIGHT` 102 из них 100 `INNER`, + 2 добавленные `RIGHT JOIN`ом. 118 = 100 + 16 + 2

`UNION` действует по умолчанию с `DISTINCT` поэтому у нас уникальные строки и строки из `INNER JOIN` не дублируются теми же строками, содержащимеся в `RIGHT` и `LEFT JOIN`

Рассмотрим запрос с прошлого урока:
```
-- выборка данных по пользователю (со вложенными запросами)
mysql> SELECT
	firstname,
	lastname,
	(SELECT hometown FROM profiles WHERE user_id = users.id) AS 'city',
	(SELECT filename FROM media WHERE id = (
	SELECT photo_id FROM profiles WHERE user_id = users.id)) AS 'main_photo'
	FROM users
	WHERE id = 88;
```
Решение этой же задачи с помощью `JOIN`
```
-- выборка данных по пользователю (JOIN)
mysql> SELECT
	firstname,
	lastname,
	hometown AS 'city',
	media.*,
	FROM users
	JOIN profiles ON profiles.user_id = users.id
	JOIN media ON media.id = profiles.photo_id
	WHERE users.id = 1;
```
Первые 2 колонки firstname, lastname пренадлежат таблице users 'city' пренадлежит SELECT hometown FROM profiles, поэтому присоединяем табличку profiles (JOIN profiles) условие объединения `( ON profiles.user_id = users.id)` явно указываем имя таблицы `profiles.user_id` мы присоединили profiles к общему запросу после этого мы можем пользоваться всеми полями этой таблицы нам нужен только hometown. для получения 'main_photo' мы пользовались запросом в запросе
```
(SELECT filename FROM media WHERE id = (
SELECT photo_id FROM profiles WHERE user_id = users.id)) AS 'main_photo'
```
В filename из таблицы media
```
SELECT filename FROM media
```
Мы присоединим таблицу media к общему запросу `JOIN` media `ON` условие объединения id в таблице media равен `photo_id` в таблице profiles `ON media.id = profiles.photo_id` photo_id это внешний ключ который ссылается на id таблицы media присоединили таблицу media после этого можем пользоваться всеми её полями хоть вот так написать `media.*`, но мы получаем ошибку по последней строчке `> WHERE id = 1` т.к id есть сейчас во всех таблицах, которые мы JOINили поэтому нам надо уточнить о какой таблице идёт речь `> WHERE users.id = 1` в поле `media.* `нам не нужны все поля нам нужно только поле media.filename
```
-- выборка данных по пользователю (JOIN)
mysql> SELECT
	firstname,
	lastname,
	hometown AS 'city',
	media.filename AS 'main_photo'
	FROM users
	JOIN profiles ON profiles.user_id = users.id
	JOIN media ON media.id = profiles.photo_id
	WHERE users.id = 1;
```
Обсудим разницу между:

- выборка данных по пользователю (JOIN)
- выборка данных по пользователю (со вложенными запросами)

Если в JOIN запросе уберём фильтрацию `WHERE users.id = 1` мы получим много строк в результате в первом запросе у нас кореляция `user_id = users.id` это отрицательно влияет на скорость работы, если мы в итоговой выборке захотим добавить дату рождения birthday, в случае `JOIN` мы её просто добавляем в `SELECT`
```
mysql> SELECT
	firstname,
	lastname,
	birthday,
	hometown AS 'city',
	media.filename AS 'main_photo'
```
В случае вложенных запросов, нам надо написать ещё один вложенный запрос
```
(SELECT birthday FROM profiles WHERE user_id = users.id) AS birthday,
```
При этом мы усложняем весь запрос т.к добавили в него ещё один вложенный цикл при этом время исполнения запроса также увеличится поэтому мы как правило пишем JOIN, когда надо собирать данные с разных таблиц таблицы объединяем по внешним ключам внешние ключи индексируются и это получается достаточно эффективно

### примеры:
### -- сообщения к пользователю
```
mysql> SELECT * FROM messages;
```
Для начала выбираем всё из таблицы messages нам нужны только те, которые адресованы конкретному пользователю применяем фильтрацию
```
mysql> SELECT * FROM messages WHERE to_user_id = 1;
```
Мы получили все сообщения, которые адресованы первому пользователю. Если мы к этой выборке захотим добавить информаию из таблицы users. можно использовать псевдонимы не только для столбцов, но и для имён таблиц и если мы придумали псевдоним для таблицы, то его должны указывать, везде где мы обращаемся к этой таблице `FROM messages AS m` в таблице messages есть ссылки на id пользователя из таблицы users
```
mysql> SELECT *
	FROM messages AS m
	JOIN users AS u ON u.id = m.from_user_id
	WHERE to_user_id = 1
```
`from_user_id и to_user_id` являются внешними ключами у нас будут разные запросы
```
mysql> SELECT *
	FROM messages AS m
	JOIN users AS u ON u.id = m.to_user_id
	WHERE to_user_id = 1

mysql> SELECT
	u.email,
	m.*
	FROM messages AS m
	JOIN users AS u ON u.id = m.to_user_id
	WHERE to_user_id = 1
```
`u.email` будет емейл  `m.to_user_id` имейл получателя, чтобы получить имейл отправителя можен снова присоединить JOIN но с другим псевдонимом
```
mysql> SELECT
	u.email AS 'recever email',
	u2.email AS 'sender email',
	m.*
	FROM messages AS m
	JOIN users AS u ON u.id = m.to_user_id
	OIN users AS u2 ON u2.id = m.from_user_id
	WHERE to_user_id = 1
	
```
Одну и туже таблицу можно добавлять несколько раз, но нужно придумать к ней разные псевдонимы и в некоторых случаях без псевдонимов нельзя обойтись

### -- сколько друзей у каждого пользователя (JOIN)

Всегда получив задачу, мы определяемся с таблицами, которые нам понадобятся пользователи в таблице users друзья в `friend_request` между этими таблицами есть внешние ключи, они отлично объединяются можем посмотреть связь в ER диаграмме `initiator_user_id`, `target_user_id` из таблицы `friend_request` связаны с id в таблице users
```
mysql> SELECT * FROM users AS u;
```
присоединяем `friend_requests`
```
mysql> SELECT *
	FROM users AS u
	JOIN friend_requests AS fr ON
	(u.id = fr.initiattor_user_id
	OR
	u.id = fr.target_user_id);
```
Теперь сгруппируем выборку по полю id таблицы user, чтобы получить количество для каждой группы
```
mysql> SELECT
	COUNT(*),
	u.email
	FROM users AS u
	JOIN friend_requests AS fr ON
	(u.id = fr.initiattor_user_id
	OR
	u.id = fr.target_user_id)
	GROUP BY u.id;
```
Мы не учли статус дружбы. нам нужны подтверждёные друзья, поэтому надо добавить фильтрацию `WHERE`
```
mysql> SELECT
	COUNT(*),
	u.email
	FROM users AS u
	JOIN friend_requests AS fr ON
	(u.id = fr.initiattor_user_id
	OR
	u.id = fr.target_user_id)
	WHERE fr.status = 'approved'
	GROUP BY u.id;
```
Теперь получили выборку сколько у каждого подтверждёных друзей можно упорядочить ка книбудь
```
ORDER BY COUNT(*) DESC
mysql> SELECT
	COUNT(*),
	u.email
	FROM users AS u
	JOIN friend_requests AS fr ON
	(u.id = fr.initiattor_user_id
	OR
	u.id = fr.target_user_id)
	WHERE fr.status = 'approved'
	GROUP BY u.id
	ORDER BY COUNT(*) DESC;
```
Дадим псевдоним для  count(*) AS cnt
```
mysql> SELECT
	COUNT(*) AS cnt,
	u.email
	FROM users AS u
	JOIN friend_requests AS fr ON
	(u.id = fr.initiattor_user_id
	OR
	u.id = fr.target_user_id)
	WHERE fr.status = 'approved'
	GROUP BY u.id
	ORDER BY cnt DESC;
```
### -- выборка новостей друзей пользователя (users.id = 1)
Это записи из таблицы media и users
```
mysql> SELECT * FROM media;
```
Нас интересуют записи, которые относятся только к моим друзьям всё что мы знаем на момент исполнения запроса это наш собственный `id (users.id = 1)`, а получить нам нужно новости моих друзей присоединяем таблицу `friend_request`
```
mysql> SELECT *
	FROM media AS m
	JOIN friend_requests AS fr ON
	m.user_id = fr.target_user-id;
```
Если мы рассматриваем по `fr.target_user-id`, то я `(users.id = 1)` - инициатор
```
mysql> SELECT *
	FROM media AS m
	JOIN friend_requests AS fr ON
	(m.user_id = fr.target_user-id
	AND
	fr.initiator_user_id = 1);
```
`(m.user_id = fr.target_user-id AND fr.initiator_user_id = 1)`
Так мы получаем новости таргетов, где я был инициатором это не все друзья, поэтому добавляем фильтрацию `ИЛИ (OR)`
```
mysql> SELECT *
	FROM media AS m
	JOIN friend_requests AS fr ON
	(m.user_id = fr.target_user-id
	AND
	fr.initiator_user_id = 1
	OR
	m.user_id = fr.initiator_user-id
	AND
	fr.target_user_id = 1);
```
добавляем фильтрацию по статусу
```
mysql> SELECT *
	FROM media AS m
	JOIN friend_requests AS fr ON
	(m.user_id = fr.target_user-id
	AND
	fr.initiator_user_id = 1
	OR
	m.user_id = fr.initiator_user-id
	AND
	fr.target_user_id = 1)
	WHERE fr.status = 'approved';
```
отсортировать в хронологическом порядке
```
mysql> SELECT *
	FROM media AS m
	JOIN friend_requests AS fr ON
	(m.user_id = fr.target_user-id
	AND
	fr.initiator_user_id = 1
	OR
	m.user_id = fr.initiator_user-id
	AND
	fr.target_user_id = 1)
	WHERE fr.status = 'approved'
	ORDER BY created_at DESC;
```
### -- Количество сообществ у пользователей
Понадобятся таблички `users` и `users_communities` к табличке usres мы хотим добавить ещё одну колонку которая будет содержать количество сообществ
```
mysql> SELECT *
FROM users AS u
JOIN users_communities AS uc ON u.id = uc.user_id;
```
Условие объединения `ON u.id = uc.user_id` айдишник пользователя равен у нас есть внешний ключ `user_id` в получившейся выборке всё нужно сгруппировать по `id` пользователя а потом вычислить `COUNT`
```
mysql> SELECT *
	FROM users AS u
	JOIN users_communities AS uc ON u.id = uc.user_id
	GROUP BY u.id;
```
после группировки, вместо `*` пользуемся агригирующими функциями
```
mysql> SELECT
	COUNT(*),
	u.email
	FROM users AS u
	JOIN users_communities AS uc ON u.id = uc.user_id
	GROUP BY u.id;
```
сделаем сортировку по убыванию
```
mysql> SELECT
	COUNT(*),
	u.email
	FROM users AS u
	JOIN users_communities AS uc ON u.id = uc.user_id
	GROUP BY u.id
	ORDER BY COUNT(*) DESC;
```
Мы хотим отфильтровать пользователей например тех которые вступили в более 1 сообщество с помощью   `WHERE` мы получим ошибку
```
mysql> SELECT
	COUNT(*) AS cnt,
	u.email
	FROM users AS u
	JOIN users_communities AS uc ON u.id = uc.user_id
	WHERE cnt > 1
	GROUP BY u.id
	ORDER BY cnt DESC;
```
Получаем ошибку дело в том что функция `COUNT(*) AS cnt`, которая появляется после отработки `GROUP BY`, а фильтрация  `WHERE cnt > 1` выполняется до группировки таким образом можно воспользоваться фильтрацией HAVING
```
mysql> SELECT
	COUNT(*) AS cnt,
	u.email
	FROM users AS u
	JOIN users_communities AS uc ON u.id = uc.user_id
	GROUP BY u.id
	HAVING cnt > 1
	ORDER BY cnt DESC;
```
# HAVING фильтрация после группировки
```
-- количество пользователей в сообществах
mysql> SELECT * FROM communites;
```
Мы хотим узнать сколько пользователей в каждом сообществе здесь надо добавить колоночку, которая нам даст количество информация о пользователях в сообществе в таблице `users_communities`. мы её присоединим
```
mysql> SELECT *
	FROM communities AS cm
	JOIN users_communities AS uc ON cm.id = uc.community_id
```
`users_community` там есть внешний ключ `community_id` получили выборку, её осталось сгруппировать по айдишнику сообщества чтобы внутри каждой группы подсчитать `COUNT`
```
mysql> SELECT *
	FROM communities AS cm
	JOIN users_communities AS uc ON cm.id = uc.community_id
	GROUP BY c.id;
```
после группировки считаем `COUNT`
```
mysql> SELECT
	COUNT(*),
	c.name
	FROM communities AS cm
	JOIN users_communities AS uc ON cm.id = uc.community_id
	GROUP BY c.id;
```
`COUNT(*)` - вместо звёздочки можем подставлять какую нибудь колонку `COUNT(c.id)` если в функции `COUNT(c.id)` пишем какое нибудь поле мы будем учитывать только те записи, где это поле не `NULL` `COUNT(*)` - не важно в каких полях какие значения
