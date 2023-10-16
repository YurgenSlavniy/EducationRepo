# Урок 10

- хранимые процедуры
- пользовательские функции
- транзакции
- представления
- триггеры

# разбор ДЗ к прошлым вебинарам

/* пусть задан некоторый пользователь. Из всех пользователей соц. сети найдите человека, который больше всех общался с выбранным пользователем */

решение с объединением таблиц (JOIN)
```
mysql> SELECT
	from_user_id,
	CONCAT(u.firstname, ' ', u.lastname) AS name,
	COUNT(*) AS 'messages count'
	FROM messages AS m
	JOIN users AS u ON u.id = m.from_user_id
	WHERE to_user_id = 1
	GROUP BY from_user_id
	ORDER BY COUNT(*) DESC
	LIMIT 1;
```
`WHERE to_user_id = 1`  для простоты взяли наш `id = 1` фильтрация по `to_user_id = 1` обозначение целевого пользователя, для которого всё высчитывали. Если убрать `LIMIT 1` получим список всех, кто писал нам сообщеня упорядоченных по количеству, по убыванию после группировки пользуемся агригирующей функцией `COUNT(*)` упорядочиваем по `COUNT(*)` по убыванию `ORDER BY COUNT(*) DESC` мы присоединяли таблицу `users` 
```
JOIN users AS u ON u.id = m.from_user_id
```
Для того чтобы получить фамилию и имя
```
CONCAT(u.firstname, ' ', u.lastname) AS name
```
если закоментируем `CONCAT(u.firstname, ' ', u.lastname) AS name`, и `JOIN users AS u ON u.id = m.from_user_id` мы не получим имени пользователя

решение с вложенными запросами
```
mysql> SELECT
	from_user_id,
	CONCAT((SELECT firstname FROM users WHERE id = m.from_user_id),
	' ',
	(SELECT lastname FROM users WHERE id = m.from_user_id))
	AS name,
	COUNT(*) AS 'messages count'
	FROM messages AS m
	WHERE to_user_id = 1
	GROUP BY from_user_id
	ORDER BY COUNT(*) DESC
	LIMIT 1;
```
во вложенном запросе от СУБД потребуется больше действий

-- подсчитать общее количество лайков, которые получили пользователи младше 18 лет.
```
-- решение с вложенными запросами
mysql> SELECT count(*) -- количество лайков
	FROM likes
	WHERE media_id IN ( -- все медиа записи таких пользователей
	SELECT id
	FROM media
	WHERE user_id IN ( -- все пользователи младше 10 лет
	SELECT
	user_id
	, birthday
	FROM profiles AS p
	WHERE YEAR(CURDATE()) - YEAR(birthday) < 10)
	;
```
В этом самом самом вложенном запросе мы получаем айдишники пользователей указанного возраста
```
SELECT
user_id
birthday
FROM profiles AS p
WHERE YEAR(CURDATE()) - YEAR(birthday) < 10)
```
Фильтруем по дате  `WHERE YEAR(CURDATE()) - YEAR(birthday) < 10)`

Список полученных айдишников в самаом самом вложенном запросе передаётся в фильтрацию `WHERE user_id IN` ( -- все пользователи младше 10 лет)
```
SELECT id
FROM media
WHERE user_id IN ( -- все пользователи младше 10 лет
SELECT
user_id
-- , birthday
FROM profiles AS p
WHERE YEAR(CURDATE()) - YEAR(birthday) < 10)
);
```
Запрос который обращался к таблице media искал медиазаписи этих пользователей айдишники мы отфильтровали в предыдущем вложенном запросе этот набор айдишников передаём в фильтрацию `WHERE media_id IN (` в запросе который обращается к таблице `FROM likes` и считаем просто `COUNT(*)`
```
-- решение с объединением таблиц
mysql> SELECT COUNT(*) -- количество лайков
	FROM likes AS l
	JOIN media AS m ON media_id = m.id
	JOIN profiles AS p ON p.user_id = m.user_id
	WHERE YEAR(CURDATE()) - YEAR(birthday) < 10;
```
Обращаемся к лайкам, присоединяем media, присоединяем profiles фильтруем по дате и вычисляем `COUNT(*)`

-- Определить кто больше поставил лайков (всего) - мужчины или женщины?
```
-- вложенные запросы
mysql> SELECT
	gender,
	COUNT(*)
	FROM (
		SELECT
		user_id AS USER,
		(
			SELECT gender
			FROM vk.profiles
			WHERE user_id = user
			) AS gender
		FROM likes
		) AS dummy
	GROUP BY gender;
```
Cамый самый вложенный запрос получает пол пользователя `SELECT gender FROM vk.profiles` этот пол мы добавляем как колоночку, где айдишники пользователя. Получается айдишник пользователя который поставил лайк и его пол
```
SELECT
user_id AS USER,
(
SELECT gender
FROM vk.profiles
WHERE user_id = user
) AS gender
FROM likes
```
В этой выборке группируем всё по полу `GROUP BY gender;` и для каждой группы f и m их получится 2, подсчитываем `COUNT(*)`
```
-- решение с объединением таблиц JOIN
mysql> SELECT gender, COUNT(*)
	FROM likes
	JOIN profiles ON likes.user_id = profiles.user_id
	GROUP BY gender;
```
Обращаемся к лайкам, присоединяем профили группируем по полу, вычисляем `COUNT(*)`, выводим поля.

- хранимые процедуры
- пользовательские функции
- транзакции
- представления
- триггеры

Процедуры и функции похожи в субд. Хранимые процедуры например в соц. сети вы можете быть знакомы и список пользователей это наводит на мысль, что пользователи туда подбираются псевдослучайным образом по каим то конкретным параметрам.
### задача подбора потенциальных друзей по определённым критериям
напишем процедуру, которая будет предлагать пользователям новых друзей.

Критерии выбора пользователей:
- из одного города,
- состоят в одной группе
- друзья друзей

Из выборки будем показывать 5 человек в случайной комбинации. Напишем с чистого листа, как будто нет `DBreaver` и мощных `IDE`. Нам нужно создать хронимую процедуру.
```
mysql> CREATE PROCEDURE sp_friendship_offers()
	BEGIN
	END
```
Если процедура принимает какие то параметры то пишем их в скобках
```
mysql> CREATE PROCEDURE sp_friendship_offers(for_user_id BIGINT UNSIGNED)
	BEGIN
	END;
```
В нашем случае `for_user_id` - процедура принимает айдишник пользователя `for_user_id` - имя переменной, `BIGINT UNSIGNED` - её тип, наша процедура принимает айдишник пользователя, а возвращает 5 айдишников потенциальных друзей

Внутри процедуры пишем её тело, какие то запросы
```
mysql> CREATE PROCEDURE sp_friendship_offers(for_user_id BIGINT UNSIGNED)
	BEGIN
	SELECT 1111;
	SELECT 2222;
	END;
```
Но возникает проблема с символом `;`. Символ окончания команды `;` ,т.к mysql не понимает ";" означает окончание локальной команды (1111;) внутри тела процедуры или окончание команды `CREATE PROCEDURE ... END;`. В mysql эта проблема решается заменой этого разделителя с помощью команды `DELIMITER //`
```
mysql> DELIMITER //
mysql> CREATE PROCEDURE sp_friendship_offers(for_user_id BIGINT UNSIGNED)
	BEGIN
	SELECT 1111;
	SELECT 2222;
	END;
```
Внутри тела оставляем разделитель ";", а полсе `END` используем новый объявленный разделитель `//`
```
mysql> DELIMITER //
mysql> CREATE PROCEDURE sp_friendship_offers(for_user_id BIGINT UNSIGNED)
	BEGIN
	SELECT 1111;
	SELECT 2222;
	END//
```
После команды END правилом хорошего тона вернуть разделитель обратно
```
mysql> DELIMITER //
mysql> CREATE PROCEDURE sp_friendship_offers(for_user_id BIGINT UNSIGNED)
	BEGIN
	SELECT 1111;
	SELECT 2222;
	END//
mysql> DELIMITER ;
```
`DBreaver` в ЛП есть папка `Procedures` там появилось имя нашей процедуры `sp_friendship_offers`, если мы меняем нашу процедуру, вносим изменения то будет ошибка, что процедура с таким именем уже существует поэтому сперва удаляем существующую процедуру.
```
mysql> DROP PROCEDURE IF EXISTS sp_friendship_offers;
mysql> DELIMITER //
mysql> CREATE PROCEDURE sp_friendship_offers(for_user_id BIGINT UNSIGNED)
	BEGIN
	SELECT 16;
	SELECT 200;
	END//
mysql> DELIMITER ;
```
`DBreaver` сам может сгенерировать код процедуры,нам останется только добавить тело процедуры
 
# -- напишем процедуру, которая будет предлагать пользователям новых друзей.
Критерии выбора пользователей:
- из одного города,
- состоят в одной группе
- друзья друзей

Из выборки будем показывать 5 человек в случайной комбинации.
```
mysql> DROP PROCEDURE IF EXISTS sp_friendship_offers;
mysql> DELIMITER //
mysql> CREATE PROCEDURE sp_friendship_offers(for_user_id BIGINT UNSIGNED)
	BEGIN
- из одного города,
- состоят в одной группе
- друзья друзей
	END//
mysql> DELIMITER ;
```
Существует 2 подхода:
- процедурный подход (императивный) мы выполняем код команда за командой по порядку
- декларативный подход мы пишем одно, может даже громозское утверждение если оно корректное с точки зрения синтаксиса то оно сразу исполняется. за один шаг вся задача решается

mysql декларативный язык позволяет писать код, чтобы в один шаг решить задачу, но логика решения подразумивает разбить на небольшие части, а потом соединить всё в едино.

Начнём с поиска потенциальных друзей из того же города, что и сам пользователь. Возвращать наша процедура будет айдишники, а города из таблицы `profiles` столбец `hometown`

из одного города
```
mysql> SELECT user_id FROM profiles
```
Объединим таблицу профилей с самой собой,
Для того чтобы вытащить `user_id`
```
mysql> SELECT user_id
	FROM profiles AS p1
	JOIN profiles AS p2 ON p1.hometown = p2.hometown
	WHERE
```
Условия объединения таблиц `ON p1.hometown = p2.hometown` одинаковые города. Дальше фильтрация `WHERE p1.user_id = for_user_id`,
где юзер-айди равен параметру пришедшему из процедуры
```
mysql> CREATE PROCEDURE sp_friendship_offers(for_user_id BIGINT UNSIGNED)
mysql> SELECT user_id
	FROM profiles AS p1
	JOIN profiles AS p2 ON p1.hometown = p2.hometown
	WHERE p1.user_id = for_user_id
```
а из выборки `p2` мы его исключаем
```
mysql> SELECT user_id
	FROM profiles AS p1
	JOIN profiles AS p2 ON p1.hometown = p2.hometown
	WHERE p1.user_id = for_user_id
	AND p2.user_id != for_user_id;
```
У нас будет ошибка т.к в самом начале запроса мы не указали из какой выборки `p1` `p2` нам надо вернуть `user_id`
```
mysql> SELECT p2.user_id
	FROM profiles AS p1
	JOIN profiles AS p2 ON p1.hometown = p2.hometown
	WHERE p1.user_id = for_user_id
	AND p2.user_id != for_user_id;
```
Потому что у нас фильтрация `WHERE p1.user_id = for_user_id AND p2.user_id != for_user_id;` и если вернём `p1.user_id`, то мы вернём тот же айдишник, который пришёл в параметре. А `р2` это все остальные кто с ним в одном городе кроме него самого.  `p2.user_id != for_user_id;`

чтобы исполнить процедуру, её надо вызвать
```
#   mysql> CALL sp_friendship_offers(1);
```
в скобках указываем параметр (id нашего пользователя = 1)

# -- потенциальные друзья с нами в одной группе

Логика наших рассуждений будет такой же, но обращаться будем к другой таблице, кто с нами в одной группе состоит мы можем узнать в табличке `users_communites` и вернуть нужно `user_id` поэтому пишем
```
#   mysql> SELECT user_id FROM users_community;
```
дальше поступаем как в примере выше с городами
```
mysql> SELECT uc2.user_id
	FROM users_community AS uc1
	JOIN users_community AS uc2 ON uc1.community_id = uc2.community_id
	WHERE uc1.user_id = for_user_id
	AND uc2.user_id != for_user_id;
```
# -- потенциальные друзья среди друзей
Логика следующая: есть выборка `х1`  мы её объедтиняем с выборкой `х2`, в `х1` у нас `for_user_id` - то что нам приходит в `х2` то что мы возвращаем наружу, когда мы будем искать друзей друзей нам надо будет добавить третью выборку `х3`, присоединить её к общему запросу.
- в `х1` у нас `for_user_id`
- в `х2` будут его друзья `(user_id его друзей)`
- в `х3` будет целевая аудитория друзья друзей, которых мы и будем возвращать

Информация о тех кто с кем дружит в таблице `friend_requests` колонка `target_id`
```
mysql> SELECT target_user_id FROM friend_requests AS fr;
```
далее объединяем снова с самой собой
```
mysql> SELECT target_user_id FROM friend_requests AS fr1
	JOIN friend_requests AS fr2;
```
условие объединения
```
mysql> SELECT target_user_id FROM friend_requests AS fr1
	JOIN friend_requests AS fr2
	ON (fr1.target_user_id = fr2.initiator_user_id
	OR fr.initiator_user_id = fr2.target_user_id);
```
присоединяем снова эту же таблицу
```
mysql> SELECT target_user_id FROM friend_requests AS fr1
	JOIN friend_requests AS fr2
	ON (fr1.target_user_id = fr2.initiator_user_id
	OR fr1.initiator_user_id = fr2.target_user_id)
	JOIN friend_requests AS fr3
	ON (fr3.target_user_id = fr2.initiator_user_id
	OR fr3.initiator_user_id = fr2.target_user_id);
```
дальше фильтруем
```
mysql> SELECT target_user_id FROM friend_requests AS fr1
	JOIN friend_requests AS fr2
	ON (fr1.target_user_id = fr2.initiator_user_id
	OR fr1.initiator_user_id = fr2.target_user_id)
	JOIN friend_requests AS fr3
	ON (fr3.target_user_id = fr2.initiator_user_id
	OR fr3.initiator_user_id = fr2.target_user_id)
	WHERE (fr1.target_user_id = for_user_id
	OR fr1.initiator_user_id = for_user_id);
```
нам нужно чтобы друзья были с подтверждёным статусом
```
mysql> SELECT target_user_id FROM friend_requests AS fr1
	JOIN friend_requests AS fr2
	ON (fr1.target_user_id = fr2.initiator_user_id
	OR fr1.initiator_user_id = fr2.target_user_id)
	JOIN friend_requests AS fr3
	ON (fr3.target_user_id = fr2.initiator_user_id
	OR fr3.initiator_user_id = fr2.target_user_id)
	WHERE (fr1.target_user_id = for_user_id
	OR fr1.initiator_user_id = for_user_id)
	AND fr2.status = 'approved'
	AND fr3.status = 'approved';
```
возвращать мы будем `target_user_id` из `fr3`
```
mysql> SELECT fr3.target_user_id FROM friend_requests AS fr1
	JOIN friend_requests AS fr2
	ON (fr1.target_user_id = fr2.initiator_user_id
	OR fr1.initiator_user_id = fr2.target_user_id)
	JOIN friend_requests AS fr3
	ON (fr3.target_user_id = fr2.initiator_user_id
	OR fr3.initiator_user_id = fr2.target_user_id)
	WHERE (fr1.target_user_id = for_user_id
	OR fr1.initiator_user_id = for_user_id)
	AND fr2.status = 'approved'
	AND fr3.status = 'approved';
```
и нам нужно сказать что он не равен for_user_id
```
mysql> SELECT fr3.target_user_id FROM friend_requests AS fr1
	JOIN friend_requests AS fr2
	ON (fr1.target_user_id = fr2.initiator_user_id
	OR fr1.initiator_user_id = fr2.target_user_id)
	JOIN friend_requests AS fr3
	ON (fr3.target_user_id = fr2.initiator_user_id
	OR fr3.initiator_user_id = fr2.target_user_id)
	WHERE (fr1.target_user_id = for_user_id
	OR fr1.initiator_user_id = for_user_id)
	AND fr2.status = 'approved'
	AND fr3.status = 'approved'
	AND fr3.target_user_id != for_user_id;
```
# ИТОГО: у нас есть 3 отдельных SELECT запроса
```
mysql> DROP PROCEDURE IF EXISTS sp_friendship_offers;
mysql> DELIMITER //
mysql> CREATE PROCEDURE sp_friendship_offers(for_user_id BIGINT UNSIGNED)
	BEGIN
-- из одного города
mysql> SELECT p2.user_id
	FROM profiles AS p1
	JOIN profiles AS p2 ON p1.hometown = p2.hometown
	WHERE p1.user_id = for_user_id
	AND p2.user_id != for_user_id;
-- состоят в одной группе
mysql> SELECT uc2.user_id
	FROM users_community AS uc1
	JOIN users_community AS uc2 ON uc1.community_id = uc2.community_id
	WHERE uc1.user_id = for_user_id
	AND uc2.user_id != for_user_id;
-- друзья друзей
mysql> SELECT fr3.target_user_id FROM friend_requests AS fr1
	JOIN friend_requests AS fr2
	ON (fr1.target_user_id = fr2.initiator_user_id
	OR fr1.initiator_user_id = fr2.target_user_id)
	JOIN friend_requests AS fr3
	ON (fr3.target_user_id = fr2.initiator_user_id
	OR fr3.initiator_user_id = fr2.target_user_id)
	WHERE (fr1.target_user_id = for_user_id
	OR fr1.initiator_user_id = for_user_id)
	AND fr2.status = 'approved'
	AND fr3.status = 'approved'
	AND fr3.target_user_id != for_user_id;
	END//
mysql> DELIMITER
mysql> CALL sp_friendship_offers(1);
```
объединяем эти запросы с помощью UNION
```
mysql> DROP PROCEDURE IF EXISTS sp_friendship_offers;
mysql> DELIMITER //
mysql> CREATE PROCEDURE sp_friendship_offers(for_user_id BIGINT UNSIGNED)
	BEGIN
-- из одного города
mysql> SELECT p2.user_id
	FROM profiles AS p1
	JOIN profiles AS p2 ON p1.hometown = p2.hometown
	WHERE p1.user_id = for_user_id
	AND p2.user_id != for_user_id
	UNION
-- состоят в одной группе
mysql> SELECT uc2.user_id
	FROM users_community AS uc1
	JOIN users_community AS uc2 ON uc1.community_id = uc2.community_id
	WHERE uc1.user_id = for_user_id
	AND uc2.user_id != for_user_id
	UNION
-- друзья друзей
mysql> SELECT fr3.target_user_id FROM friend_requests AS fr1
	JOIN friend_requests AS fr2
	ON (fr1.target_user_id = fr2.initiator_user_id
	OR fr1.initiator_user_id = fr2.target_user_id)
	JOIN friend_requests AS fr3
	ON (fr3.target_user_id = fr2.initiator_user_id
	OR fr3.initiator_user_id = fr2.target_user_id)
	WHERE (fr1.target_user_id = for_user_id
	OR fr1.initiator_user_id = for_user_id)
	AND fr2.status = 'approved'
	AND fr3.status = 'approved'
	AND fr3.target_user_id != for_user_id;
	END//
mysql> DELIMITER
mysql> CALL sp_friendship_offers(1);
```
в условии задачи из выборки будем показывать 5 человек в случайной комбинации.
```
mysql> LIMIT 5;
```
Но тогда из первого запроса выбираются 5  пользователей и всё и только если недоберётся 5 записей в первом запросе, мы пойдём добирать 5 записей из 2 ого запроса, потом только если не доберём дойдём до 3 запроса, случайности вывода записей не будет упорядочиваем с помощью `ORDER BY RAND()`

```
mysql> DROP PROCEDURE IF EXISTS sp_friendship_offers;
mysql> DELIMITER //
mysql> CREATE PROCEDURE sp_friendship_offers(for_user_id BIGINT UNSIGNED)
	BEGIN
-- из одного города
mysql> SELECT p2.user_id
	FROM profiles AS p1
	OIN profiles AS p2 ON p1.hometown = p2.hometown
	WHERE p1.user_id = for_user_id
	AND p2.user_id != for_user_id
	UNION
-- состоят в одной группе
mysql> SELECT uc2.user_id
	FROM users_community AS uc1
	JOIN users_community AS uc2 ON uc1.community_id = uc2.community_id
	WHERE uc1.user_id = for_user_id
	AND uc2.user_id != for_user_id
	UNION
-- друзья друзей
mysql> SELECT fr3.target_user_id FROM friend_requests AS fr1
	JOIN friend_requests AS fr2
	ON (fr1.target_user_id = fr2.initiator_user_id
	OR fr1.initiator_user_id = fr2.target_user_id)
	JOIN friend_requests AS fr3
	ON (fr3.target_user_id = fr2.initiator_user_id
	OR fr3.initiator_user_id = fr2.target_user_id)
	WHERE (fr1.target_user_id = for_user_id
	OR fr1.initiator_user_id = for_user_id)
	AND fr2.status = 'approved'
	AND fr3.status = 'approved'
	AND fr3.target_user_id != for_user_id
	ORDER BY RAND()
	LIMIT 5;
	END//
mysql> DELIMITER
mysql> CALL sp_friendship_offers(1);
```
При каждом вызове процедура возвращает 5 случайных пользователей, которые вошли в нашу выборку для решения задачи мы написали процедуру, она принимает айдишник пользователя и выдаёт 5 других айдишников, которые могут являться потенциальными друзьями

# ФУНКЦИИ

Когда пользователей будет много в соц. сети, то нам нужна будет информация об их популярности, чтобы в поиске например как то сортировать выборку. Например придумать коэфицент популярности пользователя. Можем взять количество запросов в друзья к этому пользователю разделить на количество запросов в друзья от него чем больше этот коэфицент, тем популярнее пользователь

Будем пользоваться инструментами кодогенерации которые предлагает `DBreaver` `ЛП -> Procedures (процедуры) -> ПКМ -> Создать объект процедура` даём имя (название:) процедуры, во всплывающем списке выбираем -> функция `(FUNCTION)`, открылась вкладка в рабочем окне. `Свойства функции` жмём на вкладку определение `(Source)` открывается сгенерированный код
```
mysql> CREATE FUNCTION vk.most_popular()
	RETURNS INT
	BEGIN
	END
```
где между `BEGIN` и `END` будем писать свой код. После написания всего жмём `CTRL + S` открывается окошко с исходным кодом. Можно копировать готовый скрипит

Задачу мы будем решать в процедурном стиле. Решается задача по шагам постепенно объявим переменные , присвоим переменным результаты посчитаем что нам нужно вернуть и вернём результат

обьявление переменной `DECLARE имя_переменнтой ТИП`
```
mysql> CREATE FUNCTION vk.most_popular()
       RETURNS INT
       BEGIN
           DECLARE requests_to_user INT; # запросы к пользователю
           DECLARE requests_from_user INT; # запросы от пользователей
       END
```
Присвоим переменным результат `SET requests_to_user = ();` значение мы будем вычислять и выглядит это как вложенный запрос
```
mysql> CREATE FUNCTION vk.most_popular()
       RETURNS INT
       BEGIN
           DECLARE requests_to_user INT; # запросы к пользователю
           DECLARE requests_from_user INT; # запросы от пользователей
           SET requests_to_user = ();
       END
```
Количество запросов в друзья к пользователю , это количество записей `SELECT count(*)` в таблице `friend_requests  FROM vk.friend_requests`. Записи в которых цель `(target_user_id)` для этого введём переменную `FUNCTION vk.most_popular(check_user_id BIGINT UNSIGNED)`, где наш пользователь был целью `WHERE target_user_id = check_user_id` количество строк где наш пользователь был целью, где  к нему стучались в друзья
```
mysql> CREATE FUNCTION vk.most_popular(check_user_id BIGINT UNSIGNED)
       RETURNS INT
       BEGIN
           DECLARE requests_to_user INT; # запросы к пользователю
           DECLARE requests_from_user INT; # запросы от пользователей
           SET requests_to_user = (
               SELECT count(*)
               FROM vk.friend_requests
               WHERE target_user_id = check_user_id
               );
       END
```
Во вторую переменную `requests_from_user` мы можем присвоить значение по похожему образу вместо таргета, будет инициатор
```
mysql> CREATE FUNCTION vk.most_popular(check_user_id BIGINT UNSIGNED)
       RETURNS INT
       BEGIN
           DECLARE requests_to_user INT; # запросы к пользователю
           DECLARE requests_from_user INT; # запросы от пользователей
           SET requests_to_user = (
               SELECT count(*)
               FROM vk.friend_requests
               WHERE target_user_id = check_user_id
               );
           SET requests_to_user = (
               SELECT count(*)
               FROM vk.friend_requests
               WHERE initiator_user_id = check_user_id
               );
       END
```
Альтернативный вариант решения в более SQL стиле
```
mysql> CREATE FUNCTION vk.most_popular(check_user_id BIGINT UNSIGNED)
       RETURNS INT
       BEGIN
           DECLARE requests_to_user INT; # запросы к пользователю
           DECLARE requests_from_user INT; # запросы от пользователей
           SET requests_to_user = (
               SELECT count(*)
               FROM vk.friend_requests
               WHERE target_user_id = check_user_id
               );
           SELECT count(*)
           INTO requests_from_user
           FROM vk.friend_requests
           WHERE initiator_user_id = check_user_id
       END
```
Подвели результаты, теперь нам нужно что то вернуть. Функция всегда должна нам что то возвращать `RETURN requests_to_user / requests_from_user`
```
mysql> CREATE FUNCTION vk.most_popular(check_user_id BIGINT UNSIGNED)
       RETURNS INT
       BEGIN
           DECLARE requests_to_user INT; # запросы к пользователю
           DECLARE requests_from_user INT; # запросы от пользователей
           SET requests_to_user = (
               SELECT count(*)
               FROM vk.friend_requests
               WHERE target_user_id = check_user_id
               );

           SELECT count(*)
           INTO requests_from_user
           FROM vk.friend_requests
           WHERE initiator_user_id = check_user_id;

           RETURN requests_to_user / requests_from_user
       END
```
Но по умолчанию у нас стоит `RETURNS INT,`, а результатом деления будет вещественное число . Дробное. меняем `INT` на `FLOAT`
```
mysql> CREATE FUNCTION vk.most_popular(check_user_id BIGINT UNSIGNED)
       RETURNS FLOAT
       BEGIN
           DECLARE requests_to_user INT; # запросы к пользователю
           DECLARE requests_from_user INT; # запросы от пользователей
           SET requests_to_user = (
               SELECT count(*)
               FROM vk.friend_requests
               WHERE target_user_id = check_user_id
               );

           SELECT count(*)
           INTO requests_from_user
           FROM vk.friend_requests
           WHERE initiator_user_id = check_user_id;

           RETURN requests_to_user / requests_from_user
       END
```
при запуске мы получили ошибку
```
You have an error in your SQL syntax;
check the manual that corresponds to your MySQL
server version for the right syntax to use near
'END' at line 18
```
После `ETURNS FLOAT` мы должны написать что то из
```
RETURNS FLOAT DETERMINISTIC
   RETURNS FLOAT NO SQL
   RETURNS FLOAT READS SQL DATA
```
Это подсказака для СУБД какого типа и рода наша функция - `DETERMINISTIC` - наша функция всгда будет возвращать один и тот же результат для одинакового набора параметров. Может использоваться как инструкция для СУБД, что результат можно захэшировать. Один раз посчитать и потом брать его из хэша - `NO SQL` можно было бы использовать если в теле функции не было бы никаких запросов чистая математика, вычисления - `READS SQL DATA`  мы в теле нашего запроса читаем sql данные
```
mysql> CREATE FUNCTION vk.most_popular(check_user_id BIGINT UNSIGNED)
       RETURNS FLOAT READS SQL DATA
       BEGIN
           DECLARE requests_to_user INT; # запросы к пользователю
           DECLARE requests_from_user INT; # запросы от пользователей
           SET requests_to_user = (
               SELECT count(*)
               FROM vk.friend_requests
               WHERE target_user_id = check_user_id
               );

           SELECT count(*)
           INTO requests_from_user
           FROM vk.friend_requests
           WHERE initiator_user_id = check_user_id;

           RETURN requests_to_user / requests_from_user;
       END
```
`CTRL + S`  ошибки не образовалось, функция сохранилась

ВЫЗВАТЬ ФУНКЦИЮ:
```
mysql> SELECT most_popular(1);
```
Можем округлить значение с помощью функции `round(param1 - что округляем, param2 - сколько знаков после запятой)`
```
mysql> SELECT round(most_popular(1), 2);
```
итого:
```
mysql> SELECT round(most_popular(1), 2) AS 'user popularity';
```
# РАЗНИЦА МЕЖДУ ПРОЦЕДУРАМИ И ФУНКЦИЯМИ
1) способ вызова. 
- для функции: `SELECT имя_функции(параметр);`
- для процедуры: `CALL имя_процедуры(параметр);`
2) возвращение результата
- функция должна что то возвращать `RETURN`
- процедура ничего не возвращает, просто делает расчёт и выводит результат
3) использование
- функцию можно использовать внутри функции ка кпараметр, например `SELECT round(most_popular(1), 2) AS 'user popularity';`
- с процедурами так нельзя
4) использование динамичных sql
- в функциях нельзя
- только в хранимых процедурах можно использовать динамический sql конструкция `(PREPARE-EXECUTE)`
5) отличие в применении
-  функции часто используются для вычислений, константы, математика, фибоначи и т.д.
- процедуры используются для реализации бизнес логики.

Иногда архитектор ПО в базу данных помещает только данные, и никакой бизнес логики, никаких вычислений, функций, процедур, тригерров. У нас есть сервер наша машина где всё будет вычисляться и крутиться, а к базе обращаемся только за данными. Полученные с базы данные уже на серере обсчитываем. Если вся бизнес логика только на сервере где используются серверные языки `(JAVA, C#)` делается чтобы ускорить разработку,` т.к программист проще пишет на своём языке, чем на sql, также этим архитектурным решением можно разделить данные в БД и бизнес логику в самом приложении.

Но мы можем использовать логику в самой SQL, когда критически важной становится скорость на больших данных это становится заметным. Когда нужно данные получать, высчитывать,обратно получать и т.д и это сказыввается на тарфике

# ТРАНЗАКЦИИ
Некоторый механизм позволяющий выполнить набор команд и точно их завершить. Есть БД. состояние 1 до выполнения команд, состояние 2 - после выполнения команд. Если начав в состоянии 1 мы наткнёмся на ошибку в наборе команд, мы снова вернёмся в исходное первое состояние либо все команды выпооняем целиком, либо не выполняем ни одну из них.

### на примере нашей соцсети:
Регестрация пользователя. Пользователь при регистрации заполняет некотоые поля формы которая у нас есть, а мы уже под капотом раскладываем данные по табличкам и так получается, что данные пользователя разбросаны по разным табличкам, как минимум какие то данные при регистрации пользователя надо положить в таблицу `users`
```
mysql> INSERT INTO users (firstname, lastname, email, phone)
	VALUES ('New', 'User', 'new@mail.com', 456789876);
```
а какие то в таблицу `profiles`
```
mysql> INSERT INTO profiles (user_id, gender, birthday, hometown)
	VALUES (@last_user_id, 'M', '1990-10-10', 'Moscow');
```
А ещё появляется сложность, что `user_id` из  `profiles` мы заранее не знаем, когда нет процедуры и функции мы вводим переменную `(@last_user_id)`
```
mysql> INSERT INTO users (firstname, lastname, email, phone)
	VALUES ('New', 'User', 'new@mail.com', 456789876);
	SET @last_user_id = 111;
	INSERT INTO profiles (user_id, gender, birthday, hometown)
	VALUES (@last_user_id, 'M', '1990-10-10', 'Moscow');
```
Если нет функции процедур к переменной мы обращаемся через собачку нам надо вычислить айдишник пользователя, которого только что вставии для этого есть специальная функция `LAST_INSERT_ID()` возвращает `id` после последний команды `INSERT` в текущей сессии

```
mysql> INSERT INTO users (firstname, lastname, email, phone)
	VALUES ('New', 'User', 'new@mail.com', 456789876);
	SET @last_user_id = LAST_INSERT_ID();
	INSERT INTO profiles (user_id, gender, birthday, hometown)
	VALUES (@last_user_id, 'M', '1990-10-10', 'Moscow');
```
У нас есть несколько команд их надо выполнить все или не выполнить ни одной поэтому обращаем этот код в транзакцию

```
mysql> START TRANSACTION;
mysql> INSERT INTO users (firstname, lastname, email, phone)
	VALUES ('New', 'User', 'new@mail.com', 456789876);
	SET @last_user_id = LAST_INSERT_ID();
	INSERT INTO profiles (user_id, gender, birthday, hometown)
	VALUES (@last_user_id, 'M', '1990-10-10', 'Moscow');
mysql> COMMIT;
```
если не хотим чтобы транзакция прошла, хотим отменить.
```
mysql> ROLLBACK;
```
Если в данных случаются ошибки, нам надо отслеживать исключения и если было исключение делать `rollback`, если не было исключения делать `COMMIT` такого рода вещи в mysql можно отслеживать в процедурах
```
-- обработка ошибки в транзакции
DROPPROCEDUREIFEXISTS`sp_add_user`;

DELIMITER $$

CREATEPROCEDURE`sp_add_user`(firstname varchar(100), lastname varchar(100), email varchar(100), phone varchar(12), hometown varchar(50), photo_id INT,OUT tran_result varchar(200))
BEGIN
DECLARE`_rollback`BOOLDEFAULT0;
 	DECLARE code varchar(100);
 	DECLARE error_string varchar(100);
DECLARE last_user_id int;

DECLARECONTINUE HANDLER FORSQLEXCEPTION
begin
 	SET`_rollback` = 1;
 	GET stacked DIAGNOSTICSCONDITION1
code = RETURNED_SQLSTATE, error_string = MESSAGE_TEXT;
 	set tran_result := concat('Error occured. Code: ', code, '. Text: ', error_string);
end;

STARTTRANSACTION;
 		INSERTINTO users (firstname, lastname, email, phone)
 		VALUES (firstname, lastname, email, phone);

 		INSERTINTO profiles (user_id, hometown, photo_id)
 		VALUES (last_insert_id(), hometown, photo_id);
 	IF`_rollback`THEN
 	ROLLBACK;
 	ELSE
 		set tran_result := 'ok';
 	COMMIT;
 	ENDIF;
END$$

DELIMITER ;

-- вызываемпроцедуру
call sp_add_user('New', 'User', 'new87@mail.com', 454545456, 'Moscow', -1, @tran_result);

-- смотрим результат
select @tran_result;
```
# ПРЕДСТАВЛЕНИЯ
Простой но достаточно мощный функционал в СУБД образно это сохранёный `SELECT` запрос посмотрим тех. документацию
```
13.1.21 CREATE VIEW Statement
CREATE
     [OR REPLACE]
     [ALGORITHM = {UNDEFINED | MERGE | TEMPTABLE}]
     [DEFINER = user]
     [SQL SECURITY { DEFINER | INVOKER }]
     VIEW view_name [(column_list)]
     AS select_statement
     [WITH [CASCADED | LOCAL] CHECK OPTION]
```
- `CREATE` затем необязательные опции
- `VIEW имя_для_view`
- `AS селект_запрос`

Обсудим необязательные опции
- `[OR REPLACE] ` - создать или заменить существующую `VIEW`
- `ALGORITHM = по умолчанию UNDEFINED`
- `MERGE` - мы в теле нашего запроса `select_statement` в самом `select` запросе используем данные из нескольких таблиц из разных БД
- `TEMPTABLE` - результат сохроняем во временную таблицу
- `[DEFINER = user]` - сейчас не актуальна, была актуальна когда sql код не было хранить в системе контроля версий, чтобы было понятно кто писал код.
- `[WITH [CASCADED | LOCAL] CHECK OPTION]` мы не будем сохронять `VIEW` если в `SELECT` запросе есть ошибки

### пример `VIEW`:
Каждый раз когда нам надо получить подтверждёный список друзей нам надо было писать запрос
```
mysql> SELECT *
	FROM users AS u
	JOIN friend_requests fr ON u.id = fr.target_user_id
	WHERE
	fr.status = 'approved'
	UNION
	SELECT *
	FROM users AS un
	JOIN friend_requests AS fr ON u.id = fr.initiator_user_id
	WHERE
	fr.status = 'approved';
```
Всё это занимало много строк, а требовалось часто мы можем этот сложный запрос сохранить как `VIEW`

```
mysql> CREATE VIEW v_friends AS
mysql> SELECT *
	FROM users AS u
	JOIN friend_requests fr ON u.id = fr.target_user_id
	WHERE
	fr.status = 'approved'
	UNION
	SELECT *
	FROM users AS un
	JOIN friend_requests AS fr ON u.id = fr.initiator_user_id
	WHERE
	fr.status = 'approved';
```
Теперь мы можем обращаться к `VIEW`
```
mysql> SELECT * FROM v_friends;
```
В одну строчку мы получаем результат исполнения этого запроса `VIEW` под капотом исполняет весь `SELECT` запрос с этой вьюшкой можем работать как с виртуальной таблицей можем дописать какие нибудь фильтрации
```
mysql> SELECT *
	FROM v_friends
	WHERE id = 1;
```
можем выбирать какие нам надо поля
```
   mysql> SELECT id, email, firstname
	FROM v_friends;
```
эти данные нигде не хрониятся, они формируются динамически и выводятся нам сразу после запроса если захотели что то подправить
```
mysql> CREATE OR REPLACE VIEW v_friends AS
```
и вносим изменеия в запрос. Представления так же могут реализовать управление разграничением правами доступа позволяют дать доступ только на чтение

Например есть менеджер, который  просит дотуп к базе а мы боимся давать ему много доступа (вдруг он что то поломает, удалит) мы можем создать специальную для него учётку в SQL и на сервере БД этой учётке дать доступ только к определённым представлениям которые нужны пользователю

# ТРИГЕРЫ
```
13.1.20 CREATE TRIGGER Statement
	CREATE
	[DEFINER = user]
	TRIGGER trigger_name
	trigger_time trigger_event
	ON tbl_name FOR EACH ROW
	[trigger_order]
	rigger_body

trigger_time: { BEFORE | AFTER }

trigger_event: { INSERT | UPDATE | DELETE }

trigger_order: { FOLLOWS | PRECEDES } other_trigger_name
```
Тригер - некоторый механизм который позволяет подписаться на какое то событие в жизни базы и в момент наступления этого события внедряет свой код. Событий три на которые реагирует тригер
- `trigger_event: { INSERT | UPDATE | DELETE }`
 свой код мы можем внедрить либо до. либо после
- `trigger_time: { BEFORE | AFTER }`
Итого 6 мест где можем наш код вставить.

Создаём триггер командой `CREATE`
- `TRIGGER trigger_name` - далее даём тригеру имя
- `trigger_time:`  - момент и trigger_event: - событие
- `ON tbl_name` - обязательно имя таблицы, тригер всегда привязан к таблице
- `FOR EACH ROW` - просто синтаксическая конструкция
- `trigger_body` - тело тригера
- `trigger_order: { FOLLOWS | PRECEDES }` позволяет выставить каскад тригеров

О тригерах на примере нашей соцсети зайдём в таблицу зкщашдуы и посмотрим прситально на колонку `birthday`. Если в это поле мы попытаемся передать некорректные данные например строковые пробуем это сохранить и получаем ошибку, о том, что тип данных не соответствует. Если мы в эту колону попытаемся вставить дату рождения из будущего то всё сохранится. Мы логически понимаем, что это ошибка и некорректные данные. Но субд от этого не защетила, ошибки не выдала, потому что это проверки бизнес логики, а не типов данных такого рода проверки мы можем реализовать на тригерах, что мы сейчас и сделаем

Можно воспользоваться инструментами кодогенерации `в DBeaver`. ПКМ в ЛП по Тригеры -> создать новый тригер даём ему имя и генерируется код во вкладке Source
```
mysql> CREATE TRIGGER check_user_age_before_update
#       -> BEFORE UPDATE
#       -> ON profiles FOR EACH ROW
#       -> BEGIN
#       -> END;
```
между `BEGIN` и `END` пишем нашу бизнес логику
```
mysql> CREATE TRIGGER check_user_age_before_update
	BEFORE UPDATE
	ON profiles FOR EACH ROW
	BEGIN
	IF NEW.birthday >= CURRENT_DATE() THEN
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'дата рождения некорректна';
	END IF;
	END;
```
Если дата рождения больше сегодняшнего числа то выводим исключение и сообщение об ошибке NEW. переменная доступная нам в триггерах представляет нам новую строку, которая  кнам приходит которой мы хотим заменить существующую строку в случае обновления в случае INSERT вставки представляет собой строку которую мы хотим вставить, если тригер на событие `UPDATE` то у нас есть переменная `OLD`. `IF OLD.birthday >= CURRENT_DATE() THEN` она содержит старую существующую строку, которую мы хотим обновить на новую в нашем случае пользуемся `NEW`. после написания `CTRL + S` тригер сохроняется и будет реагировать на события вставки `BEFORE UPDATE`

посмотрим стрку
```
mysql> SELECT * FROM profiles WHERE user_id = 1;
```
попробуем её обновить с некорректными данными
```
mysql> UPDATE profiles SET birthday = '2028.10.10' WHERE user_id = 1;
```
Запрос вызывает ошибку выводится сообщение с кодом который мы написали и текстом об ошибке наш триггер проверил, что дата некорректная увидел ошибку. Сообщил и фактически отменил команду `UPDATE` защитил нас от ошибки передаём корректные данные никаких ошибок не возникает.

Тригеры применяются например для логирования для вызова внешних сервисов например отправляет смс после добавления новой строчки в таблицу тригерр может проверять данные, вычислеия, бизнеслогику
