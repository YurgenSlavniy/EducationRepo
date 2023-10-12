# Урок 5. 
# Операторы, фильтрация, сортировка и ограничение. Агрегация данных.

### Арифметические операторы
- Ключевое слово AS в SELECT
- Логические операторы
- Логические И и ИЛИ
- STORED-столбцы

Операторы - конструкции языка, которые производят преобразование данных. Данные над которыми осуществляются операции - операнды

### Арифметические операторы:
- 2+5  - сложение
- 5-2 - вычитание
- 5*7 - умножение
- 2\3 - деление
- 9%8 - остаток от деления
- 10 DIV 8 - целочисленное деление

Переходим в консоль (командная строка)
```
 >>> mysql -u root -p
```
Подключаемся к mysql
```
mysql> SELECT 3 + 5;
-->
+-------+
| 3 + 5 |
+-------+
|     8 |
+-------+
1 row in set (0.01 sec)
```
Результат - таблица из одного столбца и одной строки, название столбца совпадает с вычисляемым значением

Переименуем название столбца с помощью ключевого слова `AS`

```
mysql> SELECT 3 + 5 AS summ;
-->
+------+
| summ |
+------+
|    8 |
+------+
1 row in set (1.80 sec)
```
Применять арифметические операторы можно со столбцами
```
mysql> SELECT * FROM catalogs;
-->
+------+--------------+
| id   | name         |
+------+--------------+
|    1 | Processors   |
|    2 | Motherboards |
|    3 | Videocards   |
+------+--------------+
3 rows in set (0.00 sec)
```
Увеличим значение идентификатора id на 10
```
mysql> UPDATE catalogs SET id = id + 10;
mysql> SELECT * FROM catalogs;
-->
+------+--------------+
| id   | name         |
+------+--------------+
|   11 | Processors   |
|   12 | Motherboards |
|   13 | Videocards   |
+------+--------------+
3 rows in set (0.00 sec)
```
Операция сложения числа с `NULL` даёт `NULL`
```
mysql> SELECT NULL + 6 ;
mysql> SELECT '3' + '5' ;
```
Операция будет выполнена автоматически приведтся к числу. Но если строка не может быть приведена к числу
```
mysql> SELECT 'asd' + 'ksh';
-->
+---------------+
| 'asd' + 'ksh' |
+---------------+
|             0 |
+---------------+
1 row in set, 2 warnings (0.00 sec)
```
Вычитание аналогично сложению. При делении на ноль получаем NULL
```
mysql> SELECT 9 / 0;
-->
+-------+
| 9 / 0 |
+-------+
|  NULL |
+-------+
1 row in set, 1 warning (0.00 sec)
```
Cравним два деления:
```
mysql> SELECT 5 / 2, 5 DIV 2;
-->
+--------+---------+
| 5 / 2  | 5 DIV 2 |
+--------+---------+
| 2.5000 |       2 |
+--------+---------+
1 row in set (0.00 sec)
```
При целочисленном делении дробная часть просто отбрасывается

Остаток от деления операторо `%`
```
mysql> SELECT 5 % 2 ;
`mysql> SELECT 5 % 2;
-->
+-------+
| 5 % 2 |
+-------+
|     1 |
+-------+
1 row in set (0.00 sec)
```
Оператор действует следующим образом: 5 - 2 * 2 = 1.  Альтернативная форма написания `%`
```
mysql> SELECT 5 MOD 2 ;
```
логические операторы:
```
mysql> SELECT TRUE, FALSE;
-->
+------+-------+
| TRUE | FALSE |
+------+-------+
|    1 |     0 |
+------+-------+
1 row in set (0.00 sec)
```
Операторы сравнения дают результатом истину или ложь

- > больше
- < меньше
- >= больше равно
- <= меньше равно
- = равно
- !=, <> не равно
- <=> безопасное сравнение, позволяет сравнивать со значение NULL
```
mysql> SELECT 8 > 11;
-->
+--------+
| 8 > 11 |
+--------+
|      0 |
+--------+
1 row in set (0.00 sec)

mysql> SELECT 8 < 11;
-->
+--------+
| 8 < 11 |
+--------+
|      1 |
+--------+
1 row in set (0.00 sec)
```
для точного сравнения
```
mysql> SELECT 2 = 2, 3 = 2;
-->
+-------+-------+
| 2 = 2 | 3 = 2 |
+-------+-------+
|     1 |     0 |
+-------+-------+
1 row in set (0.00 sec)
```
Для использования отрицания используется оператор `NOT` эквивалентом служит "!"
```
mysql> SELECT NOT TRUE, ! FALSE;
-->
+----------+---------+
| NOT TRUE | ! FALSE |
+----------+---------+
|        0 |       1 |
+----------+---------+
1 row in set (0.00 sec)
```
Сравнение с NULL всегда возвращает NULL. Для безопасного сравнения с NULL
```
mysql> SELECT 2 <=> NULL, NULL <=> NULL;
-->
+------------+---------------+
| 2 <=> NULL | NULL <=> NULL |
+------------+---------------+
|          0 |             1 |
+------------+---------------+
1 row in set (0.00 sec)
```
Более классические операторы сравнения IS , IS NOT
```
mysql> SELECT 2 IS NULL, 2 IS NOT NULL, NULL IS NULL, NULL IS NOT NULL;
-->
+-----------+---------------+--------------+------------------+
| 2 IS NULL | 2 IS NOT NULL | NULL IS NULL | NULL IS NOT NULL |
+-----------+---------------+--------------+------------------+
|         0 |             1 |            1 |                0 |
+-----------+---------------+--------------+------------------+
1 row in set (0.00 sec)
```
Конструкция  `IS NULL`  - ровно ли проверяемое значение `NULL` или нет вставим в таблицу catalogs ещё пару значений
```
mysql> INSERT INTO catalogs VALUES();
-->
Query OK, 1 row affected (0.08 sec)

mysql> INSERT INTO catalogs VALUES(NULL, 'netdivaces');
-->
Query OK, 1 row affected (0.07 sec)

mysql> SELECT * FROM catalogs;
-->
+------+--------------+
| id   | name         |
+------+--------------+
|   11 | Processors   |
|   12 | Motherboards |
|   13 | Videocards   |
| NULL | NULL         |
| NULL | netdivaces   |
+------+--------------+
5 rows in set (0.00 sec)
```
Чтобы извлечь из таблицы значения NULL
```
mysql> SELECT * FROM catalogs WHERE id IS NULL;
-->
+------+------------+
| id   | name       |
+------+------------+
| NULL | NULL       |
| NULL | netdivaces |
+------+------------+
2 rows in set (0.00 sec)

mysql> SELECT * FROM catalogs WHERE id IS NULL AND name IS NULL;
-->
+------+------+
| id   | name |
+------+------+
| NULL | NULL |
+------+------+
1 row in set (0.00 sec)
```
Для того чтобы извлечь заполненные строки
```
mysql> SELECT * FROM catalogs WHERE name IS NOT NULL;
-->
+------+--------------+
| id   | name         |
+------+--------------+
|   11 | Processors   |
|   12 | Motherboards |
|   13 | Videocards   |
| NULL | netdivaces   |
+------+--------------+
4 rows in set (0.00 sec)
```
Условия можно комбинировать с помощью логического И (AND)
- AND     true   false
- true    true   false
- false   false  false

Условия можно комбинировать с помощью логического ИЛИ (OR)
- OR     true   false
- true   true   true
- false  true   false

```
mysql> SELECT TRUE AND TRUE, TRUE AND FALSE, FALSE AND TRUE, FALSE AND FALSE;
-->
+---------------+----------------+----------------+-----------------+
| TRUE AND TRUE | TRUE AND FALSE | FALSE AND TRUE | FALSE AND FALSE |
+---------------+----------------+----------------+-----------------+
|             1 |              0 |              0 |               0 |
+---------------+----------------+----------------+-----------------+
1 row in set (0.00 sec)

mysql> SELECT TRUE OR TRUE, TRUE OR FALSE, FALSE OR TRUE, FALSE OR FALSE;
-->
+--------------+---------------+---------------+----------------+
| TRUE OR TRUE | TRUE OR FALSE | FALSE OR TRUE | FALSE OR FALSE |
+--------------+---------------+---------------+----------------+
|            1 |             1 |             1 |              0 |
+--------------+---------------+---------------+----------------+
1 row in set (0.00 sec)
```
Выражение можно сохранять в таблицах, оператор `create table` допускает создание столбцов значение которых автоматически создаётся как арифметическое значение других столбцов
```
mysql> CREATE TABLE tbl (x INT, y INT, summ INT AS (x + y));
-->
Query OK, 0 rows affected (0.14 sec)
```
заполним таблицу данными:
```
mysql> INSERT INTO tbl(x, y) VALUES (1, 1), (4, 5), (2, 32);
-->
Query OK, 3 rows affected (0.10 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM tbl;
-->
+------+------+------+
| x    | y    | summ |
+------+------+------+
|    1 |    1 |    2 |
|    4 |    5 |    9 |
|    2 |   32 |   34 |
+------+------+------+
3 rows in set (0.00 sec)
```
По умолчанию эти значения не сохраняются на жёсткий диск, а каждый раз вычисляются заново, чтобы сохронялся надо добавить ключевое слово `STORED`
```
mysql> CREATE TABLE tbl (x INT, y INT, summ INT AS (x + y) STORED);
```
# Операторы. фильтрация. сортировка и ограничение. УСЛОВНАЯ ВЫБОРКА
- оператор BETWEEN (блок-схемы)
- оператор LIKE
- оператор RLIKE
- регулярные выражения

т.к БД хронят по миллиону записей, ситауция когда требуется изменить количество вводимых строк встречается очень часто, ключевое слово `WHERE` после которого следует логическое усовие
```
mysql> SELECT * FROM catalogs;
mysql> SELECT * FROM catalogs WHERE id > 2;
mysql> SELECT * FROM catalogs WHERE id > 2 AND id <= 4;
```
Для выборки записей из определённого интервала существует специальный оператор `BETWEEN` возвращает `TRUE` если значение входит в диапозон `FALSE` в противном случае
```
mysql> SELECT 2 BETWEEN 2 AND 4;
-->
+-------------------+
| 2 BETWEEN 2 AND 4 |
+-------------------+
|                 1 |
+-------------------+
1 row in set (0.97 sec)

mysql> SELECT 1 BETWEEN 2 AND 4;
-->
+-------------------+
| 1 BETWEEN 2 AND 4 |
+-------------------+
|                 0 |
+-------------------+
1 row in set (0.00 sec)
```
Перепишем запрос с помощью BETWEEN
```
mysql> SELECT * FROM catalogs WHERE id BETWEEN 3 AND 4;
```

Конструкция `NOT BETWEEN` - возвращает значения не попадающие в интервал

Извлечь записи удовлетваряющие списку например записи с идентификаторами 1, 2, 5
```
mysql> SELECT * FROM catalogs WHERE id IN (1, 2, 5);
```
Возаращает `FALSE` если значение не входит в список `TRUE` если такое значение в списке имеется, если в списке значение `NULL` возвращается `NULL`

Существует противоположная конструкция `NOT IN` возвращает `TRUE` для элементов, которые не входят в список

```
mysql> SELECT * FROM catalogs WHERE name = 'Videocards';
-->
+------+------------+
| id   | name       |
+------+------------+
|   13 | Videocards |
+------+------------+
1 row in set (0.03 sec)
```
Для формирования условий можем использовать не только числовой тип данных условную выборку с участием строк удобно производить с помощью оператора `LIKE`. `LIKE` возвращает истину, если шаблон соответствует.
```
mysql> SELECT * FROM catalogs WHERE name LIKE 'processors';
```
Использование спецсимволов для `LIKE`
- % - любое количество символов или их отсутствие
- _ - Ровно один символ

```
mysql> SELECT 'Program' LIKE 'P%m', 'Pigman' LIKE 'P%m';
-->
+----------------------+---------------------+
| 'Program' LIKE 'P%m' | 'Pigman' LIKE 'P%m' |
+----------------------+---------------------+
|                    1 |                   0 |
+----------------------+---------------------+
1 row in set (0.00 sec)

mysql> SELECT 'man' LIKE '___', 'as' LIKE '___', 'mi' LIKE '__';
-->
+------------------+-----------------+----------------+
| 'man' LIKE '___' | 'as' LIKE '___' | 'mi' LIKE '__' |
+------------------+-----------------+----------------+
|                1 |               0 |              1 |
+------------------+-----------------+----------------+
1 row in set (0.00 sec)
```
Для помещения в шаблон самих символов без их интерпритации необходимо экранировать их с помощью обратного слэша
```
mysql> SELECT '15 %', 'my_sql';
-->
+------+--------+
| 15 % | my_sql |
+------+--------+
| 15 % | my_sql |
+------+--------+
1 row in set (0.00 sec)

mysql> SELECT '15 %' LIKE '15 \%', 'my_sql' LIKE 'my\_sql';
mysql> SELECT * FROM catalogs WHERE name LIKE '%s'
```
Оператор `NOT LIKE` противоположен оператору `LIKE`

Заполним таблицу users.
```
mysql> DROP TABLE IF EXISTS users;
          CREATE TABLE users (
    id INT UNSIGNED NOT NULL,
    name VARCHAR(255) COMMENT 'name buyer',
    birthday_at DATE COMMENT 'user birhtday',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'date of registration',
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
 ) COMMENT = 'buyers';

   mysql> INSERT INTO users (name, birthday_at) VALUES
       ('Mos', '1990-10-05'),
       ('Kate', '1986-05-03'),
       ('Tyhon', '1965-01-18'),
       ('Ivan', '1997-02-01'),
       ('Mariya', '1969-07-30'),
       ('Nadya', '1998-08-16');
```
Пользователи родившиеся с 1990 по 2000
```
mysql> SELECT * FROM users WHERE birthday_at >= '1990-01-01' AND birthday_at < '2000-01-01';
```
тотже запрос с помощью оператора `BETWEEN`
```
mysql> SELECT * FROM users WHERE birthday_at BETWEEN '1990-01-01' AND '2000-01-01';
```
При использовании оператора `LIKE` календарный столбец преобразуется к строке
```
mysql> SELECT * FROM users WHERE birthday_at LIKE '199%';
```
# ОПЕРАТОРЫ `RLIKE` и `REGEXP`
Поиск в соотвествии с регулярными выражениями это специализированный язык поиска подстрок в тексте
```
mysql> SELECT content RLIKE '[[:digit:]]*\\.[[:digit:]]{2}';
```
Имеется шаблон в котором также присутствуют спецсимволы слева от оператора `RLIKE` распологаем строку в которой осуществляем поиск справа находится регулярное выражение
```
mysql> SELECT 'грамм' RLIKE 'грам', 'граммпластинка' RLIKE 'грам';
-->
+-------------------------------+-------------------------------------------------+
| 'грамм' RLIKE 'грам'          | 'граммпластинка' RLIKE 'грам'                   |
+-------------------------------+-------------------------------------------------+
|                             1 |                                               1 |
+-------------------------------+-------------------------------------------------+
1 row in set (0.08 sec)
```
Часто необходимо привязать регулярное выражение к началу слова чтобы регулярное выражение грам соответствовало подстроке которая начинается с грам символ `^`- соотвествует началу строки
```
mysql> SELECT 'грампластинка' RLIKE '^грам', 'программирование' RLIKE '^грам'\G
       'грампластинка' RLIKE '^грам': 1
 'программирование' RLIKE '^грам': 0
 1 row in set (0.00 sec)
```
спецсимвол `$`  позволяет привязать регулярное выражение к концу строки
```

mysql> SELECT 'граммпластинка' RLIKE '^граммпластинка$';
-->
+-----------------------------------------------------------------------+
| 'граммпластинка' RLIKE '^граммпластинка$'                             |
+-----------------------------------------------------------------------+
|                                                                     1 |
+-----------------------------------------------------------------------+
1 row in set (0.00 sec)

mysql> SELECT 'граммпластинка на столе' RLIKE '^граммпластинка$';
-->
+---------------------------------------------------------------------------------------+
| 'граммпластинка на столе' RLIKE '^граммпластинка$'                                    |
+---------------------------------------------------------------------------------------+
|                                                                                     0 |
+---------------------------------------------------------------------------------------+
1 row in set (0.00 sec)
```
Применение символов `^` `$` позволяет указать что регулярное выражение должно в точности соответствовать всей строке от начала до конца.  Д ля задания альтернатив символ  `|` выступает как логическое или
```
mysql> SELECT 'abc' RLIKE 'abc|абв', 'абв' RLIKE 'abc|абв';
```

Если спецсимвол должен быть частью строки, то используем двойной обратный слэш для экранирования `\\` для задания классов символов используются квадратные скобки `[]` ограничивают поиск теми символами, которые в них заключены
```
mysql> SELECT 'a' RLIKE '[abc]' AS a, 'b' RLIKE '[abc]' AS b, 'w' RLIKE '[abc]' AS w;
-->
+---+---+---+
| a | b | w |
+---+---+---+
| 1 | 1 | 0 |
+---+---+---+
1 row in set (0.00 sec)
```
В квадратных скобках допускается использовать диапазоны
```mysql> SELECT 'р' RLIKE '[а-яё]';
```
буква ё в диапазон не входит её включаем отдельно
```
mysql> SELECT 7 RLIKE '[0-9]', 7 RLIKE '[0123456789]';
-->
+-----------------+------------------------+
| 7 RLIKE '[0-9]' | 7 RLIKE '[0123456789]' |
+-----------------+------------------------+
|               1 |                      1 |
+-----------------+------------------------+
1 row in set (0.00 sec)
```
Существуют специальные классы, например для только что рассмотренного диапазона существует класс digit, который соответствует числам, ему не будут удовлетворять строковые значения классы задаются в двойных квадратных скобках
```
mysql> SELECT 7 RLIKE '[[:digit:]]';
```
для строковых символов специальный класс альфа

квантификаторы для того чтобы распространить действие класса на несколько символов указываются сразу после квадратных скобок
- ? - символ входит ноль или один раз
- * - любое количество вхождений, включая ноль
- + - одно или более вхождений символа в строку
```
mysql> SELECT '1' RLIKE '^[0-9]+$' AS '1',
	'34234' RLIKE '^[0-9]+$' AS '34234',
	'342.34'RLIKE '^[0-9]+$' AS '342.34',
	'' RLIKE '^[0-9]+$' AS '';
+---+-------+--------+---+
| 1 | 34234 | 342.34 |   |
+---+-------+--------+---+
| 1 |     1 |      0 | 0 |
+---+-------+--------+---+
1 row in set (0.00 sec)
```
Создадим регулярное выражение для цены т.е для 342.34 целая часть состоит из любого количества цифр, а дробная всегда состоит из 2ух
```
mysql> SELECT 342.34 RLIKE '^[0-9]*\\.[0-9]{2}$' AS '342.34';
```

# СОРТИРОВКА, ОГРАНИЧЕНИЕ ВЫБОРКИ, УНИКАЛЬНЫЕ ЗНАЧЕНИЯ
- сортировка
- огрничение выборки
- извлечение уникальных значений
- сортировка и ограничения в DELETE и UPDATE

Запрос выдаёт результаты в порядке, в котором они хронятся в БД записи не всегда будут выводиться в порядке добавления, при добавлении, апдейте, удалении порядок может нарушаться

```
mysql> SELECT * FROM catalogs ORDER BY name;
```
Сортируем по столбцу `name.` По умолчанию сортировка в прямом порядке, в случае со строками по алфавиту если хотим в обратном порядке
```
mysql> SELECT * FROM catalogs ORDER BY name DESC;
```
по нескольким столбцам:
```
mysql> SELECT id, catalog_id, price, name FROM products;
mysql> SELECT id, catalog_id, price, name FROM products ORDER BY catalog_id, price;
```
в обратном порядке по двум столбцам
```
mysql> SELECT id, catalog_id, price, name FROM products ORDER BY catalog_id DESC, price DESC;
```
Когда большой объём информации лучше разбить её на страницы и предоставлять пользователю порциями для этого используем ключевое слово `LIMIT` после ставим число выводимых значений
```
mysql> SELECT id, catalog_id, price, name FROM products LIMIT 2;
```
для извлечения следующих записей
```
mysql> SELECT id, catalog_id, price, name FROM products LIMIT 2, 2;
```
для извлечения следующих записей
```
mysql> SELECT id, catalog_id, price, name FROM products LIMIT 4, 2;
```
Можно указывать с какой позиции выводить с помощью ключевого слова `OFFSET`
```
mysql> SELECT id, catalog_id, price, name FROM products LIMIT 2 OFFSET 4;
```
Часто стоит задача вывода уникальных значений из таблицы
```
mysql> SELECT DISTINCT catalog_id FROM products ORDER BY catalog_id;
```
Извлечение всех значений столбца в том числе и повторяющихся
```
mysql> SELECT ALL catalog_id FROM products ORDER BY catalog_id;
```
т.к это стоит по умолчанию, ключевое слово `ALL` опускается

Можно применять к `DELETE` и `UPDATE`
```
mysql> SELECT id, catalog_id, price, name FROM products WHERE catalog_id = 2 AND price > 5000;
```
теперь применим `UPDATE` к выбранным значениям
```
mysql> UPDATE products SET price = price * 0.9 WHERE catalog_id =2 AND price > 5000;
```
удалим 2 самые дорогие позиции
```
mysql> SELECT id, catalog_id, price, name FROM products ORDER BY price;
```
разместим позиции, так чтобы самые дорогие были вверху
```
mysql> SELECT id, catalog_id, price, name FROM products ORDER BY price DESC;
```
ограничим выборку только 2 умя строками
```
mysql> SELECT id, catalog_id, price, name FROM products ORDER BY price DESC LIMIT 2
mysql> DELETE FROM products ORDER BY price DESC LIMIT 2;
```
подобрать подходящие условия при помощи select запроса, а потом заменить SELECT на DELETE и UPDATE

# ПРЕДОПРЕДЕЛЕННЫЕ ФУНКЦИИ
- предопределёные функции
- календарные функции
- выборка случайного значения
- справочные функции

предопределёные функции - готовые функции, которые предоставляет система управления БД. функции характеризуются именем и аргументами, которые перечисляются за именем в круглых скобках. Результат который возвращает функция подставляется в место вызова
```
mysql> SELECT NOW();
-->
+---------------------+
| NOW()               |
+---------------------+
| 2021-10-10 13:41:17 |
+---------------------+
1 row in set (0.06 sec)
```
посмотрим характеристики таблицы
```
mysql> DESCRIBE users;
-->
+-------------+------------------+------+-----+-------------------+-------+
| Field       | Type             | Null | Key | Default           | Extra |
+-------------+------------------+------+-----+-------------------+-------+
| id          | int(10) unsigned | NO   |     | NULL              |       |
| name        | varchar(255)     | YES  |     | NULL              |       |
| birthday_at | date             | YES  |     | NULL              |       |
| created_at  | datetime         | YES  |     | CURRENT_TIMESTAMP |       |
| updated_at  | datetime         | YES  |     | CURRENT_TIMESTAMP |       |
+-------------+------------------+------+-----+-------------------+-------+
5 rows in set (0.05 sec)
```
Добавим значение и используем явную временную функцию для заполнения полей с датой
```
mysql> INSERT INTO users VALUES (NULL, 'Александр'. '1985-07-13', NOW(), NOW());
```
Отсекём время, чтобы оставалась только дата
```
mysql> SELECT name, DATA(created_at), DATE(updated_at) FROM users WHERE name = 'Александр';

mysql> SELECT
	id,
	name,
	birthday_at,
	DATE(created_at) AS created_at
	DATE(updated_at) AS updated_at
	FROM
	users;
```
Функция `DATE_FORMAT(аргумент1, аргумент2)` для форматирования календарных типов:

- аргумент 1 - время в одном из календарных типов
- аргумент 2 - строка форматирования
```
mysql> SELECT DATE_FORMAT('2018-06-12 01:59:59', 'На дворе %Y год');
-->
+-----------------------------------------------------------------+
| DATE_FORMAT('2018-06-12 01:59:59', 'На дворе %Y год')           |
+-----------------------------------------------------------------+
| На дворе 2018 год                                               |
+-----------------------------------------------------------------+
1 row in set (0.18 sec)
```
Заменим сколярное значение даты функцией `NOW()`
```
mysql> SELECT DATE_FORMAT(NOW(), 'На дворе %Y год');
-->
+-------------------------------------------------+
| DATE_FORMAT(NOW(), 'На дворе %Y год')           |
+-------------------------------------------------+
| На дворе 2021 год                               |
+-------------------------------------------------+
1 row in set (0.00 sec)
```
`%Y` отвечает за извлечение года из календарного значения со всеми последовательнастями `(%Y, %D)` можем ознакомиться по документации

Например отформатируем день рождения пользователя в удобном формате
```
mysql> SELECT name, DATE_FORMAT(birthday_at, '%d.%m.%y') AS birthday_at FROM users;
```
Преобразование двты и времени в `UNIXSTAMP` формат т.е количество секунд которое прошло с полуночи 1 января 1970 года по 2038 год т.к это целое число его можно быстро обрабатывать, индексировать и оно занимает меньше места функция `UNIX_TIMESTAMP()` обратное преобразование `FROM_UNIXTIME()`
```
mysql> SELECT
	UNIX_TIMESTAMP('2018-10-10 10:09:23') AS TIMESTAMP,
	FROM_UNIXTIME (168998866) AS DATETIME;
-->
+------------+---------------------+
| TIMESTAMP  | DATETIME            |
+------------+---------------------+
| 1584428949 | 1991-05-29 22:02:56 |
+------------+---------------------+
1 row in set (0.10 sec)
```
Очистим таблицу users;
```
mysql> TRUNCATE users;
```
Изменим первый столбец в таблице users
```
mysql> ALTER TABLE users MODIFY COLUMN id INT UNSIGNED NOT NULL PRIMARY KEY;
```
Добавляем значения в таблицу, вычислим текущий возраст пользователя по полю `birthday_at` преобразуем дату рождения и текущую дату в дни полученные дни делятся на 365.25
```
mysql> SELECT
	name,
	(TO_DAYS(NOW()) - TO_DAYS(birthday_at)) / 365.25 AS age
	FROM
	users;
```
избавится от дробной части
```
mysql> SELECT
	name,
	FLOOR(TO_DAYS(NOW()) - TO_DAYS(birthday_at)) / 365.25 AS age
	FROM
	users;
```
функция `TIMESTAMPDIFF`
```
mysql> SELECT
	name,
	TIMESTAMPDIFF(YEAR, birthday_at, NOW()) AS age
	FROM
	users;
```
Везде где используется имя столбца можем использовать функции . Для вывода записей в случайном порядке
```
mysql> SELECT * FROM users ORDER BY RAND();
```
выведим одну случайную запись
```
mysql> SELECT * FROM users ORDER BY RAND() LIMIT 1;
```
существуют информационные функции текущая версия mysql сервера
```
mysql> SELECT VERSION();
+-------------------------+
| VERSION()               |
+-------------------------+
| 5.7.33-0ubuntu0.16.04.1 |
+-------------------------+
1 row in set (0.02 sec)
```
```
mysql> SELECT VERSION() FROM DUAL;
```
Использование псевдотаблицы `DUAL`

Узнать значения присвоиные столбцу, снабжённому `AUTO_INCREMENT`
```
mysql> SELECT LAST_INSERT_ID();
```
можно использовать для вставки внешнего ключа
```
mysql> TRUNCATE catalogs;
mysql> TRUNCATE products;
mysql> INSERT INTO catalogs VALUES (NULL, 'Процессоры');
mysql> INSERT INTO products
	(name, description, price, catalog_id)
	VALUES
	('intel core i3', 'процессор Intel', 7890.00, LAST_INSERT_ID()),
	('intel core i5', 'процессор Intel', 12890.00, LAST_INSERT_ID()),
	('AMD FX-8320E', 'процессор AMD', 4670.00, LAST_INSERT_ID()),
	('AMD FX-8320', 'процессор AMD', 14670.00, LAST_INSERT_ID());
```
Добавим следующую категорию и дозаполним таблицу products
```
mysql> INSERT INTO catalogs VALUES (NULL, 'Материснские платы');
mysql> INSERT INTO products
	(name, description, price, catalog_id)
	VALUES
	('Asus rog maximus x hero', 'Z370', 19300.00, LAST_INSERT_ID()),
	('Gigabyte H310', 'B250', 11300.00, LAST_INSERT_ID()),
	('MSI C679', 'L690', 54300.00, LAST_INSERT_ID());
```
К информационным функциям относится
```
mysql> SELECT DATABASE();
-->
+------------+
| DATABASE() |
+------------+
| example_db |
+------------+
1 row in set (0.00 sec)
```
возвращает текущую базу данных

возвращает текущего пользователя
```
mysql> SELECT USER();
-->
+----------------+
| USER()         |
+----------------+
| root@localhost |
+----------------+
1 row in set (0.04 sec)
```
# огромное количество математических функций

получение случайного числа
```
mysql> SELECT RAND();
-->
+--------------------+
| RAND()             |
+--------------------+
| 0.9775705411821329 |
+--------------------+
1 row in set (0.03 sec)
```
`SQRT()` - квадратный корень числа
```
mysql> CREATE TABLE distances (
id SERIAL PRIMARY KEY,
x1 INT NOT NULL,
y1 INT NOT NULL,
x2 INT NOT NULL,
y2 INT NOT NULL,
distance DOUBLE AS (SQRT(POW(x1 - x2, 2) + POW(y1 - y2, 2)))
) COMMENT = 'Расстояние между двумя точками';
```
Заполним таблицу
```
mysql> INSERT INTO distances
	(x1, y1, x2, y2)
	VALUES
	(1, 1, 4, 5),
	(4, -1, 3, 2),
	(-2, 5, 1, 3);

mysql> SELECT * FROM distances;
-->
+----+----+----+----+----+--------------------+
| id | x1 | y1 | x2 | y2 | distance           |
+----+----+----+----+----+--------------------+
|  1 |  1 |  1 |  4 |  5 |                  5 |
|  2 |  4 | -1 |  3 |  2 | 3.1622776601683795 |
|  3 | -2 |  5 |  1 |  3 |  3.605551275463989 |
+----+----+----+----+----+--------------------+
3 rows in set (0.00 sec)
```
Можно использовать JSON поля. Cимвол `$` как начало коллекции
```
mysql> CREATE TABLE distances (
	id SERIAL PRIMARY KEY,
	a JSON NOT NULL,
	b JSON NOT NULL,
	distance DOUBLE AS (SQRT(POW(a->>'$.x' - b->>'$.x', 2) + POW(a->>'$.x' - b->>'$.y', 2)))
	) COMMENT = 'Расстояние между двумя точками';
```
заполним таблицу JSON полями
```
mysql> INSERT INTO distances
	(a, b)
	VALUES
	('{"x": 1, "y": 1}', '{"x": 4, "y": 5}'),
	('{"x": 5, "y": 8}', '{"x": -4, "y": 0}'),
	('{"x": -1, "y": 1}', '{"x": -4, "y": -5}');

mysql> SELECT * FROM distances;
-->
+----+-------------------+--------------------+-----------------+
| id | a                 | b                  | distance        |
+----+-------------------+--------------------+-----------------+
|  1 | {"x": 1, "y": 1}  | {"x": 4, "y": 5}   |               5 |
|  2 | {"x": 5, "y": 8}  | {"x": -4, "y": 0}  | 10.295630140987 |
|  3 | {"x": -1, "y": 1} | {"x": -4, "y": -5} |               5 |
+----+-------------------+--------------------+-----------------+
```
Для некоторых задач требуются тригонометрические функции. Вычислить площадь треугольника, если известны длины сторон и угол между ними

создадим таблицу. состоящую из 5 столбцов
```
mysql> CREATE TABLE triangles (
	id SERIAL PRIMARY KEY,
	a DOUBLE NOT NULL COMMENT 'сторона треугольника',
	b DOUBLE NOT NULL COMMENT 'сторона треугольника',
	angle INT NOT NULL COMMENT 'угол в градусах',
	square DOUBLE AS (a * b * SIN(RADIANS(angle)) / 2.0)
	) COMMENT = 'площадь треугольника';
```
т.к `SIN` ожидает значение аргумента в радианах с помощью функции `RADIANS()` переводим градусы в радианы

заполним таблицу значениями
```
mysql> INSERT INTO
	triangles (a, b, angle)
	VALUES
	(1.12, 4 , 65),
	(3.32, 5 , 15),
	(2, 4 , 30),
	(5.67, 4.78 , 45),
	(1.12, 14 , 125);

mysql> SELECT * FROM triangles;
-->
+----+------+------+-------+--------------------+
| id | a    | b    | angle | square             |
+----+------+------+-------+--------------------+
|  1 | 1.12 |    4 |    65 |  2.030129442962096 |
|  2 | 3.32 |    5 |    15 | 2.1481980743509217 |
|  3 |    2 |    4 |    30 | 1.9999999999999998 |
|  4 | 5.67 | 4.78 |    45 |   9.58221612389326 |
|  5 | 1.12 |   14 |   125 |  6.422152027225695 |
+----+------+------+-------+--------------------+
5 rows in set (0.00 sec)
```
Результат вычислений можно округлить при помощи функции `ROUND()` поменяем значение столбца `ROUND(выражение, число знаков после запятой)`
```
mysql> ALTER TABLE triangles CHANGE square square DOUBLE AS (ROUND(a * b * SIN(RADIANS(angle)) / 2.0, 4));
```
Осуществляется математическое округление до ближайшего целого числа

Функция `CEILING()` округление в большую сторону
```
mysql> SELECT CEILING(-2.8), CEILING(-0.8), CEILING(0.8), CEILING(5.8);
-->
+---------------+---------------+--------------+--------------+
| CEILING(-2.8) | CEILING(-0.8) | CEILING(0.8) | CEILING(5.8) |
+---------------+---------------+--------------+--------------+
|            -2 |             0 |            1 |            6 |
+---------------+---------------+--------------+--------------+
1 row in set (0.00 sec)

mysql> SELECT ROUND(-2.8), ROUND(-0.8), ROUND(0.8), ROUND(-5.8);
-->
+-------------+-------------+------------+-------------+
| ROUND(-2.8) | ROUND(-0.8) | ROUND(0.8) | ROUND(-5.8) |
+-------------+-------------+------------+-------------+
|          -3 |          -1 |          1 |          -6 |
+-------------+-------------+------------+-------------+
1 row in set (0.00 sec)

mysql> SELECT FLOOR(-2.8), FLOOR(-0.8), FLOOR(0.8), FLOOR(5.8);
-->
+-------------+-------------+------------+------------+
| FLOOR(-2.8) | FLOOR(-0.8) | FLOOR(0.8) | FLOOR(5.8) |
+-------------+-------------+------------+------------+
|          -3 |          -1 |          0 |          5 |
+-------------+-------------+------------+------------+
```
Существует большое количество функций, обслуживающих строки выбрать из таблицы первые несколько символов
```
mysql> SELECT id, SUBSTRING(name, 1, 5) AS name FROM users;
```
Выводит символы с 1 по 5-ый для колонки name

 Объединяются строки с помощью функции `CONCAT()`
```
mysql> SELECT id, CONCAT(name, ' ', TIMESTAMPDIFF(YEAR, birthday_at, NOW())) AS name FROM users;
```
`CONCAT(первая строка, соединительный символ, вторая строка)`

ЛОГИЧЕСКИЕ ФУНУЦИИ позволяют преобразовать результат в зависимости от выполнения того или иного условия выведим слово совершеннолетний или несовершеннолетний в зависимости от того достиг пользователь 18 лет или нет
```
mysql> SELECT name,
	IF (TIMESTAMPDIFF(YEAR, birthday_at, NOW()) >= 18,
	'cовершеннолетний',
	'несовершеннолетний')
	AS status FROM users;
```
Если необходимо проверить больше условий можно использовать выражение `CASE`

```
mysql> CREATE TABLE rainbow(
	id SERIAL PRIMARY KEY,
	color VARCHAR(255)
	) COMMENT = 'цвета радуги';
```
заполним таблицу с цветами радуги значениями
```
mysql>  INSERT INTO
	rainbow (color)
	VALUES
	('red'),
	('orange'),
	('yellow'),
	('green'),
	('blue'),
	('indigo'),
	('violet');
```
Таблица содержит только английские названия цветов, если при выводе захотим изменить англ. названия русскими
```
mysql> SELECT
	CASE
	WHEN color = 'red' THEN 'красный'
	WHEN color = 'orange' THEN 'оранжевый'
	WHEN color = 'yellow' THEN 'желтый'
	WHEN color = 'green' THEN 'кзелёный'
	WHEN color = 'blue' THEN 'голубой'
	WHEN color = 'indigo' THEN 'синий'
	ELSE 'фиолетовый'
	END AS russian
	FROM
	rainbow;
```
mysql предоставляет различные вспомогательные функции `INET_ATON()` принимает ай пи адрес и представляет его в виде целого числа
```
mysql> SELECT INET_ATON('85.145.54.10'), INET_ATON('127.0.0.1');
-->
+---------------------------+------------------------+
| INET_ATON('85.145.54.10') | INET_ATON('127.0.0.1') |
+---------------------------+------------------------+
|                1435579914 |             2130706433 |
+---------------------------+------------------------+
1 row in set (0.00 sec)
```
обратная задача
```
mysql> SELECT INET_NTOA(1435579914), INET_NTOA(2130706433);
```
уникальный идентификатор возвращает функция `UUID()`
```
mysql> SELECT IUUID();
-->
+--------------------------------------+
| UUID()                               |
+--------------------------------------+
| 1b579d31-2a83-11ec-a534-a3137308ceef |
+--------------------------------------+
1 row in set (0.00 sec)
```
# АГРЕГАЦИЯ ДАННЫХ
- группировка данных
- агрегационные функции
- специальные возможности GROUP BY

### ГРУППИРОВКА ДАННЫХ
- группировка данных
- Ключевое слово `GROUP BY`
- функция `COUNT`
- функция `GROUP_CONCAT`

используя операцию `%` - остаток от деления можем разбивать таблицу на отдельные группы
```
mysql> SELECT id, name, id % 3 FROM products ORDER BY id % 3;
```
задача получения уникальных значений
```
SELECT catalog_id FROM products GROUP BY catalog_id;
```

Разобъём таблицу пользователей на группы родившиеся в 80, 90, 2000 ых
```
mysql> SELECT id, name, SUBSTRING(birthday_at, 1, 3) FROM users;
```
`SUBSTRING(birthday_at, 1, 3)` - отображаем символы с 1 по 3 для колонки birthday_at и преобразуем к строковому значению
```
mysql> SELECT id, name, SUBSTRING(birthday_at, 1, 3) AS decode FROM users;
```
Назначаем для вычисляемого поля псевдоним `AS decode` который сможем использовать в других ключевых словах
```
mysql> SELECT id, name, SUBSTRING(birthday_at, 1, 3) AS decode FROM users ORDER BY decode;
```
Отсортировываем по псевдониму
```
mysql> SELECT SUBSTRING(birthday_at, 1, 3) AS decode FROM users GROUP BY decode;
```
Если после `SELECT` сейчас попробуем ввести другие поля будет ошибка
```
mysql> SELECT id, name, SUBSTRING(birthday_at, 1, 3) ...
```
Каждая из групп содержит несколько пользователей не понятно кого из них нужно выводить

# АГРИГАЦИОННЫЕ ФУНКЦИИ
Позволяют работать с содержимым групп полученных при помощи `GROUP BY` например подсчитать количество записей внутри каждой из групп
```
mysql> SELECT COUNT(*), SUBSTRING(birthday_at, 1, 3) AS decode FROM users GROUP BY decode;
```
Полученные значения можем сортировать при помощи `ORDER BY`
```
mysql> SELECT
	COUNT(*),
	SUBSTRING(birthday_at, 1, 3) AS decode
	FROM
	users
	GROUP BY
	decode
	ORDER BY
	decode DESC;
```
Назначим функции `COUNT(*)` псевдоним `total` и отсортируем по этому псевдониму
```
mysql> SELECT
	COUNT(*) AS total,
	SUBSTRING(birthday_at, 1, 3) AS decode
	FROM
	users
	GROUP BY
	decode
	ORDER BY
	total DESC;
```
# ! ПОРЯДОК СЛЕДОВАНИЯ КЛЮЧЕВЫХ СЛОВ ВАЖЕН !
`ORDER BY` не может быть раньше `GROUP BY` также относится к ключевому слову `LIMIT`, которое должно распологаться после овсех оставльных ключевых слов

Если не используем `GROUP BY` - вся таблица она большая группа
```
mysql> SELECT COUNT(*) FROM users;
```
посмотреть содержание группы с помощью функции `GROUP_CONCAT()`
```
mysql> SELECT
	GROUP_CONCAT(name),
	SUBSTRING(birthday_at, 1, 3) AS decode
	FROM
	users
	GROUP BY
	decode;
```
Функция  `GROUP_CONCAT()` допускает задание разделителя с помощью `SEPARATOR`
```
mysql> SELECT
	GROUP_CONCAT(name SEPARATOR ' '),
	SUBSTRING(birthday_at, 1, 3) AS decode
	FROM
	users
	GROUP BY
	decode;
```
 Можно отсортировать значения в рамках возвращаемой строки с помощью  `ORDER BY`
```
mysql> SELECT
	GROUP_CONCAT(name ORDER BY name DESC SEPARATOR ' '),
	SUBSTRING(birthday_at, 1, 3) AS decode
	FROM
	users
	GROUP BY
	decode;
```
Имеет ограничения `GROUP_CONCAT` - максимум 1000 извлекаемых значений

# АГРЕГАЦИОННЫЕ ФУНКЦИИ
- особенности функции `COUNT()`
- поиск минимального и максимального значений
- среднее значение
- подсчёт суммы столбца

При помощи функции `COUNT()` можем узнать количество значений в таблице. В качестве аргумента функция принимает название столбца
```
mysql> SELECT COUNT(id) FROM catalogs;
```
значения `NULL` не учитываются
```
mysql> SELECT COUNT(*) FROM catalogs;
```
значения `NULL` учитываются

используя `GROUP BY` разбиваем таблицу на отдельные группы
```
mysql> SELECT catalog_id FROM products GROUP BY catalog_id;
```
функция `COUNT()` возвращает результаты для каждой из этих групп
```
mysql> SELECT catalog_id, COUNT(*) AS total FROM products GROUP BY catalog_id;
```
### Реакция агригационных функций на NULL значения
Создадим таблицу с 2умя столбцами
```
mysql> CREATE TABLE tbl(
	d INT NOT NULL,
	value INT DEFAULT NULL
	);
```
заполним таблицу
```
mysql> INSERT INTO tbl VALUES
	(1, 340),
	(2, NULL),
	(1, 40),
	(1, NULL);

mysql> SELECT * FROM tbl;
-->
+----+-------+
| id | value |
+----+-------+
|  1 |   340 |
|  2 |  NULL |
|  3 |    40 |
|  4 |  NULL |
+----+-------+

mysql> SELECT COUNT(id), COUNT(value) FROM tel;
-->
+-----------+--------------+
| COUNT(id) | COUNT(value) |
+-----------+--------------+
|         4 |            2 |
+-----------+--------------+
1 row in set (0.07 sec)

mysql> SELECT COUNT(*) FROM tel;
-->
+----------+
| COUNT(*) |
+----------+
|        4 |
+----------+
1 row in set (0.00 sec)
```
Для подсчёта только уникальных значений
```
SELECT COUNT(DISTINCT id) AS total_ids FROM products;
```

функции `MIN()` и `MAX()` возвращают минимальное и максимальное значение столбца
```
mysql>SELECT MIN(price) AS min, MAX(price) AS max FROM products;
```
при группировке получим мин и макс для каждой группы
```
mysql> SELECT
	MIN(price) AS min,
	MAX(price) AS max
	FROM
	products
	GROUP BY
	catalog_id;
```
максимальное значение без функции `MAX()`
```
mysql> SELECT id, name, price FROM products ORDER BY price DESC LIMIT 1;
```
функция `AVG()` возвращает среднее значение
```
mysql> SELECT AVG(price) FROM products;
```
округлим до 2ух знаков после запятой
```
mysql> SELECT ROUND(AVG(price), 2) FROM products;
```
получить средние цены для каждого из разделов
```
mysql> SELECT
	catalog_id,
	ROUND(AVG(price), 2) AS price
	FROM
	products
	GROUP BY
	catalog_id;
```
допускается использование вычисляемых значений
```
mysql> SELECT
	catalog_id,
	ROUND(AVG(price * 1.2), 2) AS price
	FROM
	products
	GROUP BY
	catalog_id;
```
сумма всех значений столбца `SUM()`
```
mysql> SELECT SUM(price) FROM products;
```
сумма всех цен в каждом из разделов
```
mysql> SELECT catalog_id, SUM(price) FROM products GROUP BY catalog_id;
```
# ДОПОЛНИТЕЛЬНЫЕ КЛЮЧЕВЫЕ СЛОВА влияющие на GROUP BY
- условие HAVING
- Получение уникальных значений
- функция ANY_VALUE()
- конструкция WITH ROLLUP

Каждая строка в результирующем запросе с участием `GROUP BY` представляет собой отдельную группу. Агригационные функции предназначены для получения результатов каждой из групп

Требуется ограничить выборку по результатам функций
```
mysql> SELECT COUNT(*) AS total,
	SUBSTRING(birthday_at, 1, 3) AS decode
	FROM users
	GROUP BY decode;
```
Например требуется выбрать где количества записей больше или равно 2
```
mysql> SELECT COUNT(*) AS total,
	SUBSTRING(birthday_at, 1, 3) AS decode
	FROM users
	GROUP BY decode
	WHERE total >=2;
```
это приведёт к ошибке! не можем взять агригационное значение и подставить в условие WHERE

для этого используем конструкцию `HAVING`
```
mysql> SELECT COUNT(*) AS total,
	SUBSTRING(birthday_at, 1, 3) AS decode
	FROM users
	GROUP BY decode
	HAVING total >=2;
```
Допускается использование `HAVING`  без `GROUP BY`
```
mysql> SELECT * FROM users HAVING birthday_at >= '1990-01-01'
```
Когда требуется обнаружить повторяющиеся значения:
- сформируем запрос на извлечение данных, которые пойдут в промежуточную таблицу
```
mysql> SELECT
	name, description, price, catalog_id
	FROM
	products
	GROUP BY
	name, description, price, catalog_id;
```
У нас остаются только уникальные значения.  Уникальности добились при помощи `GROUP BY`. `GROUP BY` может принимать несколько столбцов? чтобы записи попали в группу все значения столбцов должны совпадать

Создадим таблицу `products_new`, которая полностью совпадает с таблицей products и с помощью операции `INSERT SELECT` мы все данные из временной таблицы перенесём в новую таблицу
```
mysql> CREATE TABLE products_new (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255),
	description TEXT,
	price DECIMAL(11, 2),
	catalog_id INT UNSIGNED,
	created_at DATATIME DEFAULT CURRENT_TIMESTAMP,
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESRAMP,
	KEY index_of_catalog_id (catalog_id)
	);

mysql> INSERT INTO
	products_new
	SELECT
	NULL, name, description, price, catalog_id, NOW(), NOW()
	FROM
	products
	GROUP BY
	name, description, price, catalog_id;
```
Посмотрим значения промежуточной таблицы
```
mysql> SELECT id, name, description, catalog_id FROM products_new;
```
Уничтожим таблицу products
```
mysql> DROP TABLE products;
```
переиминуем таблицу products_new в products
```
mysql> ALTER TABLE products_new RENAME products;
```
посмотрим содержимое таблицы products;
```
mysql> SELECT id, name, catalog_id FROM products;
```
для группировки можно использовать вычисляемые значения
```
mysql> SELECT name, birthday_at FROM users;
```
извлечём года на которые приходится дата раждения случайного пользователя из этого года, посмотрим табличку и сгруппируем
```
mysql> SELECT name, birthday_at FROM users ORDER BY birthday_at;
```
извлечём из таблицы года. на которые приходятся даты рождения
```
mysql> SELECT YEAR(birthday_at) FROM users ORDER BY birthday_at;
```
избавимся от повторов
```
mysql> SCELECT
	YEAR(birthday_at) AS birthday_year
	FROM
	users
	GROUP_BY
	birthday_year
	ORDER BY
	birthday_year;

mysql> SCELECT
	MAX(name),
	YEAR(birthday_at) AS birthday_year
	FROM
	users
	GROUP_BY
	birthday_year
	ORDER BY
	birthday_year;
```
Мы использовали игригационную функцию `MAX` чтобы обойти ограничения на вывод имени пользователя, потомучто при исполнении с name произойдёт ошибка:
```
mysql> SCELECT
	name,
	YEAR(birthday_at) AS birthday_year
	FROM
	users
	GROUP_BY
	birthday_year
	ORDER BY
	birthday_year;
```
предусмотрена специальная функция `ANY_VALUE ()` для вывода случайного значения
```
mysql> SCELECT
	ANY_VALUE(name),
	YEAR(birthday_at) AS birthday_year
	FROM
	users
	GROUP_BY
	birthday_year
	ORDER BY
	birthday_year;
```
конструкция позволяет добавить ещё одну строку суммы значений всех предыдущих строк
```
mysql> SELECT
	SUBSTRING(birthday_at, 1, 3) AS decode,
	COUNT(*)
	FROM
	users
	GROUP BY
	decode;
```
подсчитываем количество пользователей, которые родились в 198(0) в 199(0) и в 200(0) года можем добавить последнюю результирующую строку с количеством всех пользователей
```
mysql> SELECT
	SUBSTRING(birthday_at, 1, 3) AS decode,
	COUNT(*)
	FROM
	users
	GROUP BY
	decode
	WITH ROLLUP;
```
