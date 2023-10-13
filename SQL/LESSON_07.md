# УРОК 7

### СЛОЖНЫЕ ЗАПРОСЫ
- типы многотабличных запросов
- вложенные запросы
- JOIN-объединения таблиц
- внешние ключи и ссылочная целостность
- типы многотабличных запросов
- объединение UNION
- ключевые слова ALL и DISTINCT
- свойства UNION-запросов

### типы многотабличных запросов
- Объединение (UNION)
- вложенные запросы
- соединения (JOIN)

Многотабличные запросы можно формировать из 2 ух и более таблиц

### Операции со множествами
- `UNION` - объединение TABLE1 + TABLE2
- `EXCEPT` - разность TABLE1 - TABLE2
- `INTERSECT` - пересечение TABLE1 ^ TABLE2

В sql мы можем оперировать не отдельными значениями а их наборами в сонове лежит теория множеств

# !!! MYSQL ПОДДЕРЖИВАЕТ ТОЛЬКО UNION !!!
реализация `EXCEPT` и `INTERSECT` не реализованы

# ВЛОЖЕННЫЕ ЗАПРОСЫ
```
mysql> SELECT
	id,
	<SUBQUERY>
	FROM
	<SUBQUERY>
	WHERE
	<SUBQUERY>
	GROUP BY
	id
	HAVING
	 <SUBQUERY>
```
Позволяют использовать результат, который возвращает запрос в другом запросе
- `<SUBQUERY>` - точки в запросе, где мы можем использовать вложенный запрос

# ТИПЫ JOIN СОЕДИНЕНИЙ
-   JOIN (INNERT JOIN)
-   LEFT JOIN
-   RIGHT JOIN
-   OUTER JOIN

очень похожи на UNION запросы, однако вместо объединения однотипных результатов JOIN запросы допускают соединение совершенно разноплановых таблиц задействуя связь - первичный внешний ключ

```
mysql> SELECT * FROM catalogs;
```
возвращает результат в виде таблицы
```
+----+-------------------------------------+
| id | name                                |
+----+-------------------------------------+
|  1 | Процессоры                          |
|  2 | Материнские платы                   |
|  3 | Видеокарты                          |
|  4 | Жесткие диски                       |
|  5 | Оперативная память                  |
+----+-------------------------------------+
5 rows in set (0.00 sec)
```
Если формат результирующей таблицы совпадает возможно объединение выполнения 2ух операторов select в одну результирующую таблицу используем оператор UNION. важное условие - совпадение всех параметров результирующих таблиц количество столбцов, порядок их следования и тип столбцов - всё это должно совпадать
```
mysql> SELECT * FROM rubrics;
-->
+----+----------------------+
| id | name                 |
+----+----------------------+
|  1 | Видеокарты           |
|  2 | Память               |
+----+----------------------+
2 rows in set (0.00 sec)
```
структуры таблиц ribrics и catalogs совпадают объединим 2 результирующих запроса в один
```
mysql> SELECT * FROM rubrics
	UNION
	SELECT * FROM catalogs;
-->
+----+-------------------------------------+
| id | name                                |
+----+-------------------------------------+
|  1 | Процессоры                          |
|  2 | Материнские платы                   |
|  3 | Видеокарты                          |
|  4 | Жесткие диски                       |
|  5 | Оперативная память                  |
|  1 | Видеокарты                          |
|  2 | Память                              |
+----+-------------------------------------+
7 rows in set (0.04 sec)

mysql> SELECT name FROM rubrics
	UNION
	SELECT name FROM catalogs;
-->
+-------------------------------------+
| name                                |
+-------------------------------------+
| Видеокарты                          |
| Память                              |
| Процессоры                          |
| Материнские платы                   |
| Жесткие диски                       |
| Оперативная память                  |
 +-------------------------------------+
6 rows in set (0.15 sec)
```
В результирующий запрос попадают только неповторяющиеся строки, чтобы предотвратить такое поведение `UNION ALL` в этом случае результирующая таблица содержит все данные
```
mysql> SELECT name FROM rubrics
	UNION ALL
	SELECT name FROM catalogs;
-->
+-------------------------------------+
| name                                |
+-------------------------------------+
| Видеокарты                          |
| Память                              |
| Процессоры                          |
| Материнские платы                   |
| Видеокарты                          |
| Жесткие диски                       |
| Оперативная память                  |
+-------------------------------------+
7 rows in set (0.00 sec)
```
Ключевые слова `ALL и DISTINCT` взаимозаменяемы часто SQL команда выбирает поведение по умолчанию например выводить всё включая дубли `ALL` выводить только уникальные значения `DISTINCT` по умолчанию `UNION DISTINCT` - поэтому `DISTINCT` не пишется если не нужно обратное `UNION ALL`

`ORDER BY` для сортировки действует на весь результат запроса, а не на отдельные таблицы
```
mysql> SELECT name FROM catalogs
	UNION ALL
	SELECT name FROM rubrics
	ORDER BY name;
	-->
+-------------------------------------+
| name                                |
+-------------------------------------+
| Видеокарты                          |
| Видеокарты                          |
| Жесткие диски                       |
| Материнские платы                   |
| Оперативная память                  |
| Память                              |
| Процессоры                          |
+-------------------------------------+
7 rows in set (0.01 sec)
```
Для обратной сортировки ключевое слово `DESC`
```
mysql> SELECT name FROM catalogs
	UNION ALL
	SELECT name FROM rubrics
	ORDER BY name DESC;
```
Тоже самое касается ключевого слова `LIMIT` сначала происходит объединение результатов и потом к полученному результату применяется `LIMIT` обойти это ограничение в рамках `UNION` обойти нельзя
```
mysql> SELECT name FROM catalogs
	UNION ALL
	SELECT name FROM rubrics
	ORDER BY name DESC
	LIMIT 2;
-->
+----------------------+
| name                 |
+----------------------+
| Процессоры           |
| Память               |
+----------------------+
2 rows in set (0.01 sec)
```
Во вложенных запросах можем сначала использовать сортировку и ограничения и затем использовать полученные результаты в `UNION` для того чтобы превратить select запросы во вложенные их помещают в круглые скобки
```
mysql> (SELECT name FROM catalogs
	ORDER BY name DESC
	LIMIT 2)
	UNION ALL
	(SELECT name FROM rubrics
	ORDER BY name DESC
	LIMIT 2);
-->
+-------------------------------------+
| name                                |
+-------------------------------------+
| Процессоры                          |
| Оперативная память                  |
| Память                              |
| Видеокарты                          |
+-------------------------------------+
 4 rows in set (0.01 sec
```
`ORDER BY` и `LIMIT` работают в рамках отдельных вложенных запросов

# !!! ЕСЛИ СТРУКТУРА ТАБЛИЦ НЕ СОВПАДАЕТ ОБЪЕДИНИТЬ ИХ В UNION НЕ ПОЛУЧИТСЯ !!!

Но если мы подберём набор столбцов, что их количество и тип будут совпадать мы сможем объединить эти 2 таблицы
```
mysql> SELECT * FROM catalogs UNION SELECT * FROM products;
-->
ERROR 1064 (42000):
You have an error in your SQL syntax;
check the manual that corresponds to your
MySQL server version for the right syntax
to use near '

mysql> SELECT * FROM catalogs UNION SELECT * FROM products' at line 1

mysql> SELECT * FROM catalogs
	UNION
	SELECT id, name FROM products;
```
первый select запрос оперделяет названия столбцов т. к мы объединяем не сами таблицы а результаты запросов мы можем объединять полностью эквивалентный запрос
```
mysql> SELECT * FROM catalogs UNION SELECT * FROM catalogs;
```
можно применять более 2ух `UNION` для объединение 2 ух и более таблиц
```
mysql> SELECT * FROM catalogs
	UNION
	SELECT id, name FROM products
	UNION
	SELECT id, name FROM users;
```
`UNION` запросы выполняются давольно медленно, промежуточные таблицы `UNION` в mysql почти всегда размещаются на жёстком диске все опрерации фильтрации и сортировки также будут осуществляться во временном файле

По возможности после ключевого слова `SELECT` следует указывать только те столбцы которые нужны в результирующей таблице и для составления запроса чем меньше столбцов указано, тем меньше размер промежуточной таблицы и тем быстрее проходят операции с ней

# ВЛОЖЕННЫЕ ЗАПРОСЫ
- ключевые слова IN, ANY, SOME, ALL
- проверка на существование
- коррелированные запросы
- подзапросы в конструкции FROM

Вложенный запрос позволяет использовать результат который возвращается базовым запросом в другом запросе синтаксис основного запроса остаётся неизменным
```
mysql> SELECT
	id,
	<SUBQUERY>
	FROM
	<SUBQUERY>
	WHERE
	<SUBQUERY>
	GROUP BY
	id
	HAVING
	<SUBQUERY>
```
подзапрос можно использовать в местах `<SUBQUERY>` для того чтобы СУБД могла отличать основной запрос от вложенного запроса последний помещают в круглые скобки

Мы хотим вычислить список всех товаров в разделе процессоры посмотрим содержимое разделов каталога
```
mysql> SELECT * FROM catalogs;
-->
+----+-------------------------------------+
| id | name                                |
+----+-------------------------------------+
|  1 | Процессоры                          |
|  2 | Материнские платы                   |
|  3 | Видеокарты                          |
|  4 | Жесткие диски                       |
|  5 | Оперативная память                  |
+----+-------------------------------------+
5 rows in set (0.00 sec)
```
Таблица products с товарами связана с таблицей catalogs при помощи внешнего ключа catalog_id
```
mysql> SELECT id, name, catalog_id FROM products;
```
если мы хотим извлечь все товары, относящиеся к разделу процессоры мы можем воспользоваться следующим условием
```
mysql> SELECT id, name, catalog_id
	FROM products
	WHERE catalog_id =1;
```
при помощи вложенных запросов извлечём первичный ключ каталога процессоры
```
mysql> SELECT id FROM catalogs WHERE name = 'процессоры';
```
а теперь превратим его во вложенный запрос
```
mysql> SELECT id, name, catalog_id
	FROM
	products
	WHERE
	catalog_id = (SELECT id FROM catalogs WHERE name = 'процессоры');
```
	
Подставили запрос на вычисление id в качестве скалярного значение в WHERE условие

давайте найдём в таблице products товар с самой высокой ценой. Для начала найдё самую максимальную цену при помощи функции `MAX()`
```
mysql> SELECT MAX(price) FROM products;
```
теперь можем сформировать вложенный запрос
```
mysql> SELECT
	id, name, catalog_id
	FROM
	products
	WHERE
	price = (mysql> SELECT MAX(price) FROM products);
```
для вложенных запросов можно использовать любой логический оператор. Найдём все товары, чья цена ниже средней
```
mysql> SELECT
	id, name, catalog_id
	FROM
	products
	WHERE
	price < (SELECT AVG(price) FROM products);
```
Использовали аггригатную функцию `AVG(price)` которая возвращает среднее значение, затем последовательно сравниваем цену с этим значением

Вложенные функции можем использовать после ключевого слова `select` для каждого из товаров извлечём названия каталога, для начала просто выведим список товарных позиций
```
mysql> SELECT
	id, name, catalog_id
	FROM
	products;
```
Для замены внешнего ключа названием товарной позиции
```
mysql> SELECT name FROM catalogs WHERE id = 1;
```
Только вместо 1 мы должны поставить ключ catalog_id
```
mysql> SELECT
	id,
	name,
	(SELECT name FROM catalogs WHERE id = catalog_id) AS 'catalog'
	FROM
	products;
```
Обратим внимание что в `WHERE` условии столбец id принадлежит таблице catalogs, а столбец catalog_id принадлежит таблице products в случае конфликтов можем явно использовать квалификационные имена
```
mysql> SELECT
	products.id,
	products.name,
	(SELECT
	catalogs.name
	FROM
	catalogs
	WHERE
	catalogs.id = products.catalog_id) AS 'catalog'
	FROM
	products;
```
Если подзапрос использует столбец из внешнего запроса, то такой запрос называется коррелированным. Главная особенность - СУБД должна вычислять для каждой строки внешнего запроса. Для объёмных таблиц может быть очень накладно.
```
mysql> SELECT
	products.id
	products.name,
	(SELECT MAX(price) FROM products) AS 'max_price'
	FROM
	products;
```
Отработает некорректно. Вложенный запрос не является коррелированным, СУБД выполнит его один раз в начале и в каждую строку будет добавлен результат из ранее выполненного запроса.

Если там, где СУБД ожидает одно значение мы попробуем передать несколько нам вернётся сообщение об ошибке
```
mysql> SELECT
	id, name, catalog_id
	FROM
	products
	WHERE
	catalog_id = (SELECT id FROM catalogs);
-->
ERROR 1242 (21000): Subquery returns more than 1 row
```
Ошибка сообщает о том, что мы возвращаем более одной строки

Для того чтобы воспользоваться вложенными запросами в таких условиях потребуется воспользоваться специальными ключевыми словами например `IN`
```
mysql> SELECT
	id, name, catalog_id
	FROM
	products
	WHERE
	catalog_id IN (1, 2);
```
Содержимое скобок в таком запросе можно заменить на вложенный запрос
```
mysql> SELECT
	id, name, catalog_id
	FROM
	products
	WHERE
	catalog_id IN (SELECT id FROM catalogs);
```
Оператор `IN` применяется в том случае, если необходимо применить оператор равенства в отношении множеств помимо оператора равенства могут использоваться другие логические опрераторы `>, >= , <= , <, !=` для реализации таких сравнений используется ключевое слово `ANY`

Есть ли среди товаров раздела материнские платы товарные позиции которые дешевле любой товарной позиции из раздела процессоры
```
mysql> SELECT
	id, name, catalog_id
	FROM
	products
	WHERE
	catalog_id = 2 AND
	price < ANY (SELECT price FROM products WHERE catalog_id = 1 );
```
выведм все товарные позиции
```
mysql> SELECT id, name, price, catalog_id
	FROM products
	ORDER BY catalog_id, price;
```
Подзапрос возвращает 4 цены из раздела процессоры `price < ANY (SELECT price FROM products WHERE catalog_id = 1 )` и сравнивает каждую цену из раздела материнские платы. Если хотя бы одно условие сробатывает `ANY` выражение считается истиной все выражение ложные - строка отбрасывается

для ключевого слова `ANY` существует синоним `SOME`
```
mysql> SELECT
	id, name, price, catalog_id
	FROM
	products
	WHERE
	catalog_id = 2 AND
	price < SOME (SELECT price FROM products WHERE catalog_id = 1 );
```
В ключевых словах `ANY` и `SOME` срабатывает логика `или`, если сробатывает хотя бы одно сравнение с множеством значений выражение считается истиным

Иногда требуется логика  `И` выражение возвращает истину, когда все условия истины, хотя бы одно ложное - всё выражение ложное в этом случае ключевое слово `ALL`

 Найдём все товары из раздела материнские платы которые дороже любого товара из раздела процессоры
```
mysql> SELECT
	id, name, price, catalog_id
	FROM
	products
	WHERE
	catalog_id = 2 AND
	price > ALL (SELECT price FROM products WHERE catalog_id = 1 );
```
Каждая цена из раздела материнские платы сравнивается с каждой ценой из раздела процессоры, хотя бы одно выражение ложно - такой товар отбрасывается в конечную выборку попадают только те товарные позиции, для которых все сравнения оказались истинные

Результирующие таблицы которые возвращаются вложенным запросом может быть пустой, то есть не содержать ни одной строки `EXISTS` и `NOT EXISTS` для проверки данного факта

Извлечём те разделы каталога для которых имеется хотя бы одна товарная позиция
```
mysql> SELECT * FROM catalogs
	WHERE EXISTS (SELECT * FROM products WHERE catalog_id = catalogs.id);
```
Если вложенный запрос возвращает более одной строки `EXISTS` возвращает истину. `EXISTS` проверяет чисо возвращаемых строк, а не содержимое

Извлечём каталоги для которых нет ни одной товарной позиции
```
mysql> SELECT * FROM catalogs
	WHERE NOT EXISTS (SELECT * FROM products WHERE catalog_id = catalogs.id);
```
# СТРОЧНЫЕ ЗАПРОСЫ
Возвращают более одного столбца возвращение в скобках перед  `IN` - конструктор строки
```
mysql> SELECT id, name, price, catalog_id FROM products
	WHERE (catalog_id, 5060.00) IN (SELECT id, price FROM catalogs);
```
его можно записывать с помощью ключевого слова `ROW`
```
mysql> SELECT id, name, price, catalog_id FROM products
	WHERE ROW(catalog_id, 5060.00) IN (SELECT id, price FROM catalogs);
```
Однако как правило это ключевое слово опускают.

Вложенные запросы возвращают результирующую таблицу, котороая становится предметом дальнейших запросов. Стандарт sql разрешает использование вложенных запросов везде где допускаются ссылки на таблицы. В частности можно использовать в продолжении `FROM`

Давайте сначала получим товарные позиции из раздела процессоры
```
mysql> SELECT id, name, price, catalog_id FROM products WHERE catalog_id =1;
```
этот запроc может стать своеобразной промежуточной таблицей давайте извлечём среднюю цену по этому разделу
```
mysql> SELECT
	AVG(price)
	FROM
	(SELECT * FROM products WHERE catalog_id = 1) AS prod;
```
В ключевом слове `FROM` мы обязаны назначить вложенному осмотру псевдоним при помощи ключевого слова `AS`

Тот же запрос
```
mysql> SELECT AVG(price)
	FROM products
	WHERE catalog_id =1;
```
Нам надо вычислить минимальные цены в разделах и получить среднюю минимальную цену в этом случае сначала можем получить минимальные цены разделов
```
mysql> SELECT catalog_id, MIN(price)
	FROM products
	GROUP BY catalog_id;
```
Группируем товарные позиции по полю каталог айди `GROUP BY catalog_id;` и вычисляем для каждого из разделов минимальную цену при помощи функции `MIN()` потом мы можем использовать полученную результирующую таблицу в качестве вложенного запроса подставляя её в ключевое слово `FROM`
```
mysql> SELECT
	AVG(price)
	FROM
	(SELECT MIN(price) AS price
	FROM products
	GROUP BY catalog_id) AS prod;
```
Получили среднююю минимальную цену, для этого воспользовались аггригирующей функцией `AVG(price)`

# JOIN-объединение таблиц
- декартово произведение таблиц
- Типы соединений
- Ключевые слова ON и USING
- многотабличные обновления
- многотабличные удаления

Декартово произзведение 40 * 60 = 2400 присоединение таблиц получается получается промежуточная таблица в которой каждая строка одной таблицы сопостовляется к каждой строке другой создавая тем самым все возможные комбинации строк обеих таблиц результирующая таблимца содержит количество столбцов равное произведению столбцов в соединяемых таблицах

Создадим 2 таблицы tbl1 и tbl2 которые будут содержать единственный столбец value
```
mysql> CREATE TABLE tbl1 (value VARCHAR(255));
mysql> INSERT INTO tbl1 ('fst1'), ('fst2'), ('fst3');
mysql> CREATE TABLE tbl2 (value VARCHAR(255));
mysql> INSERT INTO tbl2 ('snd1'), ('snd2'), ('snd3');
```
Теперь посмотрим содержимое таблиц
```
mysql> SELECT * FROM tbl1;
-->
+-------+
| value |
+-------+
| fst1  |
| fst2  |
| fst3  |
+-------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM tbl1;
-->
+-------+
| value |
+-------+
| snd1  |
| snd2  |
| snd3  |
+-------+
3 rows in set (0.00 sec)
```
Для того чтобы создать соединение этих 2 ух таблиц их имена следует перечислить после ключевого слова `FROM` через запятую
```
mysql> SELECT * FROM tbl1, tbl2;
-->
+-------+-------+
| value | value |
+-------+-------+
| fst1  | snd1  |
| fst2  | snd1  |
| fst3  | snd1  |
| fst1  | snd2  |
| fst2  | snd2  |
| fst3  | snd2  |
| fst1  | snd3  |
| fst2  | snd3  |
| fst3  | snd3  |
+-------+-------+
9 rows in set (0.06 sec)
```
Вместо запятой можно использовать ключевое слово `JOIN`
```
mysql> SELECT * FROM tbl1 JOIN tbl2;
```
К каждой строке первой таблицы сопоставляются все строки второй таблицы, если явно запросить поле value получим сообщение об ошибке
```
mysql> SELECT value FROM tbl1, tbl2;
-->
ERROR 1052 (23000): Column 'value' in field list is ambiguous
```
СУБД не может определить столбец какой таблицы tbl1 имеется в виду. Для того чтобы исключить неоднозначность можно использовать квалификационные имена
```
mysql> SELECT tbl1.value, tbl2.value FROM tbl1, tbl2;
```
При явном указании указании имён таблиц всё отрабатывает без ошибок для символа `*` также можно использовать квалификационное имя
```
mysql> SELECT tbl1.*, tbl2.* FROM tbl1, tbl2;
```
если мы используем символ `*` будут выводиться столбцы всех соединяемых таблиц

Таблицам можно назначать псевдоимы с помощью ключевого слова `AS` такой подход позволяет использовать более короткие имена для таблиц

Содержимое промежуточной таблицы можно фильтровать например при помощи `WHERE` условий

Соединим таблицы products и catalogs
```
mysql> SELECT
	p.name, p.price, c.name
	FROM
	catalogs AS с
	JOIN
	products AS p;
```
Редко требуется выводить все возможные комбинации, чаще количество строк ограничивается при помощи условия
```
mysql> SELECT
	p.name
	p.price
	c.name
	FROM
	catalogs AS с
	JOIN
	products AS p
	WHERE
	c.id = p.catalog_id;
```
Вместо `WHERE` можно использовать `ON` условие. `ON` условие работает в момент соединения т.е промежуточная таблица сразу получается небольшой `WHERE` условие действует после объединения т.е сперва получается промежуточная таблица с декартовым произведением таблиц лишь затем осуществляется фильтрация

Можно осуществлять запросы с участием одной и той же таблицы назначая ей разные псевдонимы такие запросы - самообъединение таблиц
```
mysql> SELECT
	*
	FROM
	catalogs AS fst
	JOIN
	catalogs AS snd;
```
избавимся от повторов
```
mysql> SELECT
	*
	FROM
	catalogs AS fst
	JOIN
	catalogs AS snd
	ON
	fst.id = snd.id;
```
Названия столбцов в `ON` условии совпадают различаются только псевдонимы таблицы в этом случае допускается использование ключевого слова `USING()`
```
mysql> SELECT
	*
	FROM
	catalogs AS fst
	JOIN
	catalogs AS snd
	USING(id);
```
При использовании условий у нас появляются ограничения согласно которому строки одной таблицы сопоставляются с другой

# ТИПЫ JOIN соединений
- JOIN (INNERT JOIN)
- LEFT JOIN
- RIGHT JOIN
- OUTER JOIN - не поддерживается mysql

Без дорполнительных ключевых слов `JOIN` осуществляет перекрёстное соединение таблиц, если для записей одной таблицы отсутствует сопоставление в другой таблице то такая запись отбрасывается `LEFT JOIN` , `RIGHT JOIN` левое и правое соединение в результирующей таблице присутствуют все записи левой и правой таблицы, даже если им нет подходящего сопоставления из другой таблицы. Кросс join производит соединение записей обеих таблиц, даже если нет подходящего сопоставления

# НЕ ПОДДЕРЖИВАЕТСЯ В MYSQL `OUTER JOIN`

Рассмотрим  `LEFT JOIN` на примере соединения таблиц catalogs и products
```
mysql> SELECT
	p.name,
	p.price,
	c.name
	FROM
	catalogs AS с
	JOIN
	products AS p
	ON
	c.id = p.catalog_id;
```
в таблице catalogs 3 записи для раздела видеокарты сопоставления с таблицей products нет, поэтому эта запись не попадает в результирующую таблиц `JOIN` соединений заменяем `JOIN` на `LEFT JOIN`
```
mysql> SELECT
	p.name,
	p.price,
	c.name
	FROM
	catalogs AS с
	LEFT JOIN
	products AS p
	ON
	c.id = p.catalog_id;
```
Раздел видеокарты появится в результирующей таблице с `NULL` значениями вместо недостающих полей

Порядок таблиц имеет значение таблица catalogs должна распологаться слева от `LEFT JOIN` если таблицы поменять местами , то надо использовать `RIGHT JOIN`
```
mysql> SELECT
	p.name,
	p.price,
	c.name
	FROM
	products AS p
	RIGHT JOIN
	catalogs AS c
	ON
	c.id = p.catalog_id;
```
Многотабличные запросы можно использовать для обновления данных
```
mysql> SELECT
	p.id, p.name, p.price, c.name
	FROM
	catalogs AS с
	JOIN
	products AS p
	ON
	c.id = p.catalog_id;
```
например если мы хотим снизить цену на 10% для материнских плат воспользуемся следующим `UPDATE` запросом
```
mysql> UPDATE
	catalogs
	JOIN
	products
	ON
	catalogs.id = products.catalog_id
	SET
	price = price * 0.9
	WHERE
	catalogs.name = 'Мат.платы';
```
посмотрим изменилась ли цена
```
mysql> SELECT
	p.id, p.name, p.price, c.name
	FROM
	catalogs AS c
	ON
	c.id = p.catalog_id;
```
Схожим образом действуют и многотабличные удаления, но в нём надо явно указывать из каких таблиц мы будем удалять записи
```
mysql> DELETE
	products, catalogs
	FROM
	catalogs
	JOIN
	products
	ON
	catalogs_id = products.catalog_id
	WHERE
	catalogs.name = 'Мат.платы';
```
Мы удалили любые упоминания о материнских патах в нашем каталоге. Если мы не хотим удалять из нашего каталога записи то после ключевого слова `DELETE` мы должны указать только одну таблицу products давайте удалим процессоры
```
mysql> DELETE
	products
	FROM
	catalogs
	OIN
	products
	ON
	catalogs.id = products.catalog_id
	WHERE
	catalogs.name = 'Процессоры';
```
# ССЫЛОЧНАЯ ЦЕЛОСТНОСТЬ И ОГРАНИЧЕНИЯ ВНЕШНЕГО КЛЮЧА
- ограничения внешнего ключа
- нарушение ссылочной целостности
- ключевое слово FOREIGN KEY

Давольно много механизмов поддержания целостности данных. Один из самых важных механизмов ограничение внешнего ключа

Таблицы catalogs и products отношением один ко многим одному каталогу может соответствовать множество товарных позиций в то время как у каждой товарной позиции может быть только один каталог для осуществления такой связи в таблице products  в поле catalog_id мы хроним значение первичного ключа из таблицы catalogs

Давайте представим, что мы удаляем каталог с идентификатором 1
```
mysql> DELETE FROM catalogs WHERE id = 1;
mysql> SELECT id, name, price, catalog_id FROM products;
```
Но в таблице products остаются записи которые соответствуют данному каталогу таким образом запрос на удаление из таблицы catalogs привёл к тому, что БД перетала быть согласованной мы нарушили целостность данных при удалении из таблицы catalogs нам необходимо помнить, что нам требуется внести изменения в таблицу products например удалить записи с внешним ключом, который ссылается на несуществующую запись или как вариант присвоить внешшнему ключу значение `NULL`

Когда база данных содржит десятки и сотни тысяч таблиц, которые ссылаются на таблицу catalogs для решения такого рода проблем в sql преднозначено ограничение внешнего ключа таблица с первичным ключём catalogs - предок таблица products - потомок

Возможны несколько ситуаций способных приводить к нарушению целостности данных удаление строки предка, обновление первичного ключа в строке предки для того чтобы задать реакцию на эти ситуации в таблицу добавляется внешний ключ ограничение которого задаётся ключевым словом `FOREIGN KEY` после ключевого слова `FOREIGN KEY` указывается название ключа и в скобках столбцы, которые играют роль внешнего ключа `FOREIGN KEY (col1,...) REFERENCES tbl (tbl_col,...)` после ключевого слова `REFERENCES` указывается имя таблицы и столбцы, которые играют роль первичного ключа необязаельные конструкции `[ON DELETE...] [ON UPDATE ...]` позволяют задать поведение СУБД при удалении или обновлении строки из таблицы предка

Стратегий может быть несколько все они задаются ключевыми словами.

# Ограничение внешнего ключа
- `CASCADE` - при обновлении или удалении записи в таблице предке соответствующие записи в таблице потомке удаляются или обнавляются автоматически
- `SET NULL` - при обновлении или удалении записи содержащей первичный ключ в таблице потомке значение внешнего ключа устанавливается в NULL
- `NO ACTION` - при обновлении или удалении записи содержащей первичный ключ в таблице потомке никаких дополнительных действий не происходит. Мы просто обозначаем логическую связь таблиц не вводя ограничений
- `RESTRICT` - если в таблице потомке имеются записи ссылающиеся на первичный ключ в таблице предка при удалении или обновлении записи с таким первичным ключом возникает ошибка. СУБД не позволяет изменять и удалять запись с первичным ключом пока не останется ни одной ссылки из таблицы потомка
- `SET DEFAULT` - очень похоже на SET NULL, только вместо NULL устанавливается значение DEFAULT

на парктике: посмотрим структуру таблицы catalogs
```
mysql> SHOW CREATE TABLE catalogs \G
-->
*************************** 1. row ***************************
        Table: catalogs
Create Table: CREATE TABLE `catalogs` (
   `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
   `name` varchar(255) COLLATE utf8_romanian_ci DEFAULT NULL COMMENT 'Название раздела',
   PRIMARY KEY (`id`),
   UNIQUE KEY `id` (`id`),
   UNIQUE KEY `unique_name` (`name`(10))
 ) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_romanian_ci COMMENT='Разделы интернет-магазина'
1 row in set (0.07 sec)

mysql> SHOW CREATE TABLE products \G
-->
*************************** 1. row ***************************
        Table: products
 Create Table: CREATE TABLE `products` (
   `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
   `name` varchar(255) COLLATE utf8_romanian_ci DEFAULT NULL COMMENT 'Название',
   `desription` text COLLATE utf8_romanian_ci COMMENT 'Описание',
   `price` decimal(11,2) DEFAULT NULL COMMENT 'Цена',
   `catalog_id` int(10) unsigned DEFAULT NULL,
   `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
   `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
   PRIMARY KEY (`id`),
   UNIQUE KEY `id` (`id`),
   KEY `index_of_catalog_id` (`catalog_id`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_romanian_ci COMMENT='Товарные позиции'
 1 row in set (0.00 sec)
```
в таблице products имеется внешний ключ `catalog_id` ``catalog_id` int(10) unsigned DEFAULT NULL,` добавим ограничение внешнего ключа для этого воспользуемся оператором `ALTER TABLE`
```
mysql> ALTER TABLE products
	ADD FOREIGN KEY (catalog_id)
	REFERENCES catalogs (id)
	ON DELETE NO ACTION
	ON UPDATE NO ACTION;
```
Получаем сообщение об ошибке связана с тем что типы первичного ключа catalogs и внешнего ключа таблицы products отличаются
```
`id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
`catalog_id` int(10) unsigned DEFAULT NULL,
```
Внешние ключи имеют значения `INT` а id - `BIGINT` исправим тип у внешнего ключа catalog_id таблицы products
```
mysql> ALTER TABLE products
	CHANGE catalog_id catalog_id BIGINT UNSIGNED DEFAULT NULL;
```
При повторной поптке добавить внешний ключ ошибки не возникает

посмотрим снова настройки таблицы
```
mysql> SHOW CREATE TABLE products \G
-->
*************************** 1. row ***************************
        Table: products
 Create Table: CREATE TABLE `products` (
   `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
   `name` varchar(255) COLLATE utf8_romanian_ci DEFAULT NULL COMMENT 'Название',
   `desription` text COLLATE utf8_romanian_ci COMMENT 'Описание',
   `price` decimal(11,2) DEFAULT NULL COMMENT 'Цена',
   `catalog_id` bigint(20) unsigned DEFAULT NULL,
   `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
   `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
   PRIMARY KEY (`id`),
   UNIQUE KEY `id` (`id`),
   KEY `index_of_catalog_id` (`catalog_id`),
   CONSTRAINT `products_ibfk_1` FOREIGN KEY (`catalog_id`) REFERENCES `catalogs` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_romanian_ci COMMENT='Товарные позиции'
 1 row in set (0.00 sec)
```
У нас появилось ограничение внешнего ключа, который не предпринимает пока никаких действий. Обратим внимание, что имя ключу назначено автоматически 
```
CONSTRAINT `products_ibfk_1`
```
Имя ключа задаётся дополнительным ключевым словом `CONSTRAINT` который синтаксически относится к конструкции `FOREIGN KEY` и предназначена для управления именем ограничения внешнего ключа. Это имя может пригодиться если мы захотим удалить ограничения из таблицы
```
mysql> ALTER TABLE products
	DROP FOREIGN KEY products_ibfk_1;

mysql> SHOW CREATE TABLE products \G
-->
*************************** 1. row ***************************
        Table: products
 Create Table: CREATE TABLE `products` (
   `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
   `name` varchar(255) COLLATE utf8_romanian_ci DEFAULT NULL COMMENT 'Название',
   `desription` text COLLATE utf8_romanian_ci COMMENT 'Описание',
   `price` decimal(11,2) DEFAULT NULL COMMENT 'Цена',
   `catalog_id` bigint(20) unsigned DEFAULT NULL,
   `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
   `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
   PRIMARY KEY (`id`),
   UNIQUE KEY `id` (`id`),
   KEY `index_of_catalog_id` (`catalog_id`)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_romanian_ci COMMENT='Товарные позиции'
 1 row in set (0.00 sec)
```
Убедимся что ограничение `FOREIGN KEY` было удалено

Имя для ограничения `FOREIGN KEY` мы можем задавать и явно для этого можем его указывать после необязательного ключевого слова `CONSTRAINT`
```
mysql> ALTER TABLE products
	ADD CONSTRAINT fk_catalog_id
	FOREIGN KEY (catalog_id)
	REFERENCES catalog (id)
	ON DELETE NO ACTION
	ON UPDATE NO ACTION;
```
создадим ограничение указав каскадный режим для удаления
```
mysql> ALTER TABLE products
	ADD CONSRTAINT fk_catalog_id
	FOREIGN KEY (catalog_id)
	REFERENCES catalogs (id)
	ON DELETE CASCADE
	ON UPDATE CASCADE;

mysql> SELECT * FROM catalogs;
```
Давайте изменим первичный ключ для микропроессоров с 1 на 4 в таблице products имеется внешний ключ catalogs_id, который ссылается на первичный ключ табоицы products т.к включён каскадный режим обнавлений должны обновится ключи в обеих таблицах
```
mysql> UPDATE catalogs SET id = 4 WHERE name = 'Процессоры';
```
изменения затронули обе таблицы. Если мы сейчас удалим раздел процессоры из таблицы catalogs то все товары из таблицы products тоже будут удалены
```
mysql> DELETE FROM catalogs WHERE name = 'Процессоры';
```
раздел процессоры и все относящиеся к нему товары удалены

Ограничение `SET NULL` но перед этим удалим текущее ограничение
```
mysql> ALTER TABLE products
	DROP FOREIGN KEY fk_catalog_id;
```
добавим новое ограничение
```
mysql> ALTER TABLE products
	ADD CONSTRAINT fk_catalog_id
	FOREIGN KEY (catalog_id)
	REFERENCES catalogs (id)
	ON DELETE SET NULL;
```
Для удаления можем устанавливать одно ограничение, для удаления - другое. При удалении раздела в таблице `catalogs` в таблице `products` внешний ключ получает значение `NULL`
