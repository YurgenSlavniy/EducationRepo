# Урок 4. CRUD-операци.

Команды для работы с данными `CRUD/ DML (Data Manipulation Language)`
Команды: 
- INSERT, 
- SELECT, 
- UPDATE, 
- DELETE

Работа с документацией^умение читать документацию поможет быстро найти нужные команды и разделы #https://dev.mysql.com/doc/refman/8.0/en/insert.html# на сайте находим мануал, а в нём про команду `INSERT` нас интересует техническое описание команды:

```
INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
     [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
     [(col_name [, col_name] ...)]
     { {VALUES | VALUE} (value_list) [, (value_list)] ...
       |
       VALUES row_constructor_list
     }
     [AS row_alias[(col_alias [, col_alias] ...)]]
     [ON DUPLICATE KEY UPDATE assignment_list]

 INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
     [INTO] tbl_name
     [PARTITION (partition_name [, partition_name] ...)]
     [AS row_alias[(col_alias [, col_alias] ...)]]
     SET assignment_list
     [ON DUPLICATE KEY UPDATE assignment_list]

 INSERT [LOW_PRIORITY | HIGH_PRIORITY] [IGNORE]
     [INTO] tbl_name
     [PARTITION (partition_name [, partition_name] ...)]
     [(col_name [, col_name] ...)]
     [AS row_alias[(col_alias [, col_alias] ...)]]
     {SELECT ... | TABLE table_name}
     [ON DUPLICATE KEY UPDATE assignment_list]

 value:
     {expr | DEFAULT}

 value_list:
     value [, value] ...

 row_constructor_list:
     ROW(value_list)[, ROW(value_list)][, ...]

 assignment:
     col_name = [row_alias.]value

 assignment_list:
     assignment [, assignment] ...
```
Мы видим три отдельных варианта команды `INSERT` они разделены пустыми строчками .
```
 INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
     [INTO] tbl_name
     [PARTITION (partition_name [, partition_name] ...)]
     [(col_name [, col_name] ...)]
     { {VALUES | VALUE} (value_list) [, (value_list)] ...
       |
       VALUES row_constructor_list
     }
     [AS row_alias[(col_alias [, col_alias] ...)]]
     [ON DUPLICATE KEY UPDATE assignment_list]
```
Этот вариант позволяет за одну команду вставить несколько строк данных

```
INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
     [INTO] tbl_name
     [PARTITION (partition_name [, partition_name] ...)]
     [AS row_alias[(col_alias [, col_alias] ...)]]
     SET assignment_list
     [ON DUPLICATE KEY UPDATE assignment_list]
```
Вставляется одна строка но более подробно прописывается что в какую колонку уйдёт
```
 INSERT [LOW_PRIORITY | HIGH_PRIORITY] [IGNORE]
     [INTO] tbl_name
     [PARTITION (partition_name [, partition_name] ...)]
     [(col_name [, col_name] ...)]
     [AS row_alias[(col_alias [, col_alias] ...)]]
     {SELECT ... | TABLE table_name}
     [ON DUPLICATE KEY UPDATE assignment_list]
```
Позволяет вставить данные из другого иного источника скопировать их

## ПЕРВЫЙ ВАРИАНТ `INSERT`:

Вставить несколько строк данных одной командой `>>> INSERT` встречаем что то в квадратных скобках - [] это необязательные опции
`[LOW_PRIORITY | DELAYED | HIGH_PRIORITY]`, `[IGNORE]` "|" - это перечисление и один из вариантов мы можем использовать если опции перечисляются внутри квадратных скобок - это необязательные опции, которые мы можем не брать. В этом случае будет использован самый первый вариант `LOW_PRIORITY`

{} - внутри фигурных скобок обязательные опции
```
{ {VALUES | VALUE} (value_list) [, (value_list)] ...
       |
       VALUES row_constructor_list
     }
```
Что то из того что внутри нужно обязательно использовать

минимально что длжно быть: `INSERT имя_таблицы (tbl_name)`  `имя_таблицы` - куда вставляем в круглых скобках набор значение которые мы хотим вставлять `{ {VALUES | VALUE} (value_list) [, (value_list)] ...` самая первая необязательная опция позволяет нам определить приоритет `[LOW_PRIORITY | DELAYED | HIGH_PRIORITY]` значение по умолчанию `LOW_PRIORITY` т.к сервера БД живут в режиме многочисленных единовременных подключений когда наш запрос прибывает на сервер то он встанет в очередь из запросов, которые пришли чуть пораньше, но ещё не успели исполниться. Можем использовать у запроса опцию  `HIGH_PRIORITY` тем самым подняв его приоритет

- `[IGNORE]`- позволяет игнорировать ошибки данных
- `[INTO]` - старая опция практически не используется. синтаксис, указывающий конкретную табличку после `[INTO]` идёт имя таблицы. Никакого симантического значения не несёт. `[INTO] tbl_name`
- `[PARTITION (partition_name [, partition_name] ...)]` -  разделы, мы их пока не пользуем `[(col_name [, col_name] ...)]` названия колонок, но в квадратных скобках `[AS row_alias[(col_alias [, col_alias] ...)]]` позволяет задать псевдонимы для строчек
- `[ON DUPLICATE KEY UPDATE assignment_list]` позволяет задать поведение в случае обнаружения дубликатов по умолчанию если есть дубликат, а его не должно быть это вызывает ошибку о мы можем на такой случай прописать отдельный список присвоений.

в `DBeaver` выбираем БД которую создали на том уроке socialnet, если в `DBeaver` прописать после `INSERT` необязательную команду `INTO`, нажав ctrl + пробел появятся подсказки
```
>>> INSERT INTO users(id, firstname, lastname, email, phone)
```
В круглых скобках выбираем поля. Для подсказки можем нажать  ctrl + пробел перечисляем поля значения которых мы хотим внести
```
>>> VALUES (1, 'Roni', 'Minov', 'algo@ya.ru', '978808876');
```
В скобках указываем значения, которые хотим вставить в соотвествующие столбцы порядок полей строго важен

`ALT + x`   исполним эту команду
 
Все поля заполнены кроме password там стоит значение   `NULL` т.е `NULL` - это отсутствие значения это не пустая строка и это не 0

Попытавшись исполнить эту же команду второй раз получаем сообщение об ошибке, потому что дублируются значение, а у `id` у нас стоит `primary key` уникальное значение, если все поля с уникальными значениями изменим, то команда исполнится

`F5` - обнавляет базу данных когда её отображаем

# Опция [IGNORE]
```
>>> INSERT IGNORE INTO users(id, firstname, lastname, email, phone)
      VALUES (1, 'Roni', 'Minov', 'algo@ya.ru', '978808876');
```
Ошибка не возникнет, но и в таблицу ничего не добавится, чтобы ошибка не останавливала выполнения скрипта. применение - дамп базы

# Какие поля обязательны для заполнения, а какие не обязательны?
Попробуем исполнить
```
INSERT INTO users ()
VALUES ();
```
Ошибки это не вызвало. У нас появилась новая строчка.

В `DBreaver` открылась вкладка статистика
```
Updated Rows 1
Queries	2
```
у нас результат :
```
1	Roni	Minov	algo@ya.ru		978808876
2	[NULL]	[NULL]    [NULL]        [NULL]
```
Во всех полях `NULL` кроме `id`, потому что у ай ди `AUTO_INCREMENT` для этого поля хронится счётчик автоинкремента, т. е можно вставлять значения без `id`
```
>>> INSERT INTO users (firstname, lastname, email, phone)
```

В документации было сказано, что мы можем пропускать набор полей
```
>>> INSERT INTO users
    VALUES ('Roni', 'Minov', 'algo@ya.ru', '978808876');
```
Получаем сообщение об ошибке количество колонок, заявленное в запросе не совпадает с количеством колонок в таблице, если хотим вставлять в табличку без указания полей, то в VALUES мы должны перечислить абсолютно все поля, которые  унас там есть. строго в том порядке, в котором они в базе присутствуют
```
>>> INSERT INTO users
    VALUES ('108', 'Roni', 'Minov', 'alhgo@ya.ru', '', '9788908876');
```
Обратим внимание, что мы нарушили порядок ай дишника, вставляя следующую запись присвоится ай ди 109, если вставим строку с айдишником который меньше, запись появится, если этот ай дишник будет уникальным `AUTO_INCREMENT` следит за последним максимальным значением, а `PRIMARY_KEY` за уникальностью значения, если мы перепутаем порядок полей, подавая запрос, то он выполнится, но некорректно. поля будут перепутаны мы допустили ошибку в данных а в некотором случае, когда поля перепутаны это вызывает ошибку т.к у нас разные типы данных

Пакетная вставка данных
```
>>> INSERT IGNORE INTO users(id, firstname, lastname, email, phone)
        VALUES
        (15, 'Min', 'Chu', 'alo@ya.ru', '9708876'),
        (16, 'Linud', 'Dui', 'dh@ya.ru', '970887876'),
        (17, 'Sorl', 'Chunj', 'ad@ya.ru', '9766176');
```
работает гораздо быстрее

## ВТОРОЙ ВАРИАНТ INSERT:
когда надо вставить одну строку данных
```
 INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
     [INTO] tbl_name
     [PARTITION (partition_name [, partition_name] ...)]
     [AS row_alias[(col_alias [, col_alias] ...)]]
     SET assignment_list
     [ON DUPLICATE KEY UPDATE assignment_list]

   SET assignment_list    SET список_присвоений
   >>> INSERT INTO `users`
       SET
           `firstname` = 'Kate',
           `lastname` = 'Uza',
           `email` = 'k@YA',
           `phone` = '89375'
        ;
```
Позволяет вставить только одну строку за команду, но позволяет явно прописывать значения для полней

```
>>> INSERT INTO `users`
      SET
       `lastname` = 'Liza'
       ;
```
Также всё отработает, заполнится только указанное поле

## ТРЕТИЙ ВАРИАНТ INSERT:
```
INSERT [LOW_PRIORITY | HIGH_PRIORITY] [IGNORE]
     [INTO] tbl_name
     [PARTITION (partition_name [, partition_name] ...)]
     [(col_name [, col_name] ...)]
     [AS row_alias[(col_alias [, col_alias] ...)]]
     {SELECT ... | TABLE table_name}
     [ON DUPLICATE KEY UPDATE assignment_list]
```
Позволяет вставить данные с другого источника

У нас есть учебная база sakila там есть табличка staff скопируем оттуда данные в нашу базу
```
>>> INSERT INTO `users` (`firstname`, `lastname`, `email`)
       SELECT first_name, last_name, email
       FROM sakila.staff
```
# SELECT запрос - запрос на чтение данных
откроем страничку тех. документации:
```
 SELECT
     [ALL | DISTINCT | DISTINCTROW ]
     [HIGH_PRIORITY]
     [STRAIGHT_JOIN]
     [SQL_SMALL_RESULT] [SQL_BIG_RESULT] [SQL_BUFFER_RESULT]
     [SQL_NO_CACHE] [SQL_CALC_FOUND_ROWS]
     select_expr [, select_expr] ...
     [into_option]
     [FROM table_references
       [PARTITION partition_list]]
     [WHERE where_condition]
     [GROUP BY {col_name | expr | position}, ... [WITH ROLLUP]]
     [HAVING where_condition]
     [WINDOW window_name AS (window_spec)
         [, window_name AS (window_spec)] ...]
     [ORDER BY {col_name | expr | position}
       [ASC | DESC], ... [WITH ROLLUP]]
     [LIMIT {[offset,] row_count | row_count OFFSET offset}]
     [into_option]
     [FOR {UPDATE | SHARE}
         [OF tbl_name [, tbl_name] ...]
         [NOWAIT | SKIP LOCKED]
       | LOCK IN SHARE MODE]
     [into_option]

 into_option: {
     INTO OUTFILE 'file_name'
         [CHARACTER SET charset_name]
         export_options
   | INTO DUMPFILE 'file_name'
   | INTO var_name [, var_name] ...
 }
```

Если посмотреть, обратив внимание на синтаксис, После `SELECT` идёт много необязательных опций и `select_expr`
- `[ALL | DISTINCT | DISTINCTROW ]` - определяет поведение в случае обнаружения дубликатов
- `ALL` - значение по умолчанию, мы выводим все дубликаты
- `DISTINCT` - вывести только уникальные значения
- `[SQL_SMALL_RESULT] [SQL_BIG_RESULT] [SQL_BUFFER_RESULT] [SQL_NO_CACHE] [SQL_CALC_FOUND_ROWS]` эти опции отвечают за совместимость
- `select_expr` - выражение, значение полей, то что мы забираем
- `[into_option]` - описывает то, куда мы сохроняем результат
- `INTO OUTFILE` 'file_name' - либо в файл
- `INTO DUMPFILE` 'file_name' - либо в дамп
- `INTO var_name [, var_name]` ... - либо во временный файл
- `[FROM table_references` - откуда брать данные,
Это мы пишем постоянно, тут идёт название таблицы, а если надо и название БД
- `[WHERE where_condition]` - условия фильтрации
- `[GROUP BY {col_name | expr | position}, ... ` - группировка
- `[HAVING where_condition]` - условия фильтрации после группировки
- `[ORDER BY {col_name | expr | position}` - сортировка
- `[ASC`  - по умолчанию сортировка по возрастанию
- `DESC]` - по убыванию
- `[LIMIT {[offset,] row_count | row_count OFFSET offset}]` количество строк которое мы хотим вывести
- `LIMIT OFFSET` - пейджинг (по страницам)

На примере кода:
```
>>> SELECT 'hello SQL'
```
Просто вывод строчки. как пример . это не прменяется
```
>>> SELECT * FROM users;
```
Выводит всю таблицу users все строки и все поля

### SELECT *  vs. SELECT id, firstname, lastname, email, password, phone
Вроде выводит одно и тоже, но `*` - выводит абсолютно всё из таблицы, и со временем в таблице появятся новые колонки и при использовании `*` они также будут выводиться, а при перечислении столбцов выводится только то, что прописали вариант без звёздочки более стабилен

# применение фильтрации
```
SELECT id, firstname, lastname, email, password, phone
FROM users
WHERE id = 1;

SELECT id, firstname, lastname, email, password, phone
FROM users
WHERE firstname = 'Mike';
```
# КОМАНДА UPDATE. Запрос на обновление данных.
Смотрим техническую документацию:
```
 Single-table syntax:

 UPDATE [LOW_PRIORITY] [IGNORE] table_reference
     SET assignment_list
     [WHERE where_condition]
     [ORDER BY ...]
     [LIMIT row_count]

 value:
     {expr | DEFAULT}

 assignment:
     col_name = value

 assignment_list:
     assignment [, assignment] ...

 Multiple-table syntax:

 UPDATE [LOW_PRIORITY] [IGNORE] table_references
     SET assignment_list
     [WHERE where_condition]
```
- `[WHERE where_condition]` - фильтрация
- `[ORDER BY ...]` - сортировка
- `[LIMIT row_count]` - ограничения

Обновится только то, что останется после этих операций

### как это работает в коде.
Например мы стучимся кому то в друзья за это отвечает таблица `friend_requests`  на текущий момент у нас пустая табличка. Вставим несколько строк. Когда отправляем заявку в друзья выполняем команду  `INSERT`
```
-- отправка запроса в друзья --
>>> INSERT INTO friend_requests (`initiator_user_id`, `target_user_id`, `status`)
       VALUES
       ('1', '2', 'requested'),
       ('1', '3', 'requested'),
       ('1', '4', 'requested'),
       ('1', '5', 'requested')
       ;
```
Заполнено всего три поля, но если посмотреть на нашу табличку:
```
DROP TABLE IF EXISTS friend_request;
CREATE TABLE friend_requests(
       initiator_user_id INT UNSIGNED NOT NULL,
 	    target_user_id INT UNSIGNED NOT NULL,
       create_at DATETIME DEFAULT NOW(),
       update_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
       status ENUM('requested', 'approved', 'deslined', 'unfriended'),
```
Есть колонка `update_at` предположим ай ди 5 зашёл в сеть и подтверждает добавление в друзья. При этом выполняется следующий запрос: фактически нам надо будет изменить статус - `status` вместо 'requested' должно стать 'approved' нам нужно обновить существующую строку
```
>>> UPDATE friend_requests
       SET
           status = 'approved'
       WHERE initiator_user_id = 1 AND target_user_id = 5
       ;
```
Запрос отработал, произошло изменение в 4-ой записи нашей таблицы, а также добавилась запись в колонке `update_at` т.к `ON UPDATE CURRENT_TIMESTAMP` когда прописывали свойства колонки

### например пользователь отклоняет запрос
```
>>> UPDATE friend_requests
       SET
           status = 'deslined'
       WHERE initiator_user_id = 1 AND target_user_id = 2
       ;
```
# DELETE запрос
Запрос на удаление данных. Удалить существующую строку с данными посмотрим страничку с документацией:
```
DELETE [LOW_PRIORITY] [QUICK] [IGNORE] FROM tbl_name [[AS] tbl_alias]
     [PARTITION (partition_name [, partition_name] ...)]
     [WHERE where_condition]
     [ORDER BY ...]
     [LIMIT row_count]
     
 -- добавим несколько сообщений эмитируем активность в нашей соц. сети --
>>> INSERT INTO `messeges` VALUES
       ('1', '1', '2', 'hello user', '1995-08-28 22:44:29'),
       ('2', '2', '1', 'hi man', now()),
       ('3', '3', '1', 'mamamia', '1995-08-28 22:44:29'),
       ('4', '1', '2', 'matumba', '1995-08-28 22:44:29'),
       ('5', '1', '5', 'finish massege', '1995-08-28 22:44:29')
       ;
```
Предположим пользователь 1 захотел удалить сообщения отправленные 2 пользователю, то. е мы должны удалить строки, где получатель 2 - `to_user_id`, а отправитель 1 - `from_user_id`
```
>>> DELETE FROM messeges WHERE from_user_id = 1 AND to_user_id = 2;
```
# КОМАНДА TRUNCATE .
Посмотрим тех. документацию:
```
TRUNCATE [TABLE] tbl_name
>>> TRUNCATE TABLE messeges;
```
Полностью удаляет таблицу и обнуляет все `AUTO_INCREMENT` она выполняет по сути `DROP TABLE` и `CREATE TABLE`

# СИНТАКСИС ВСЕГДА МОЖНО ПОДСМОТРЕТЬ В ТЕХ. ДОКУМЕНТАЦИИ

`DBreaver` может заниматься кодогенирацией
```
ЛП -> выбираем таблицу -> ПКМ -> Генерация SQL
```
и выбираем команду

# Генераторы данных
Сервисы для генерации данных:

- http://filldb.info/
- http://www.generatedata.com/
- https://sourceforge.net/p/benerator/wiki/Home/
- http://www.dominicgiles.com/datagenerator.html

`MVP - Minimal Vibal Product`
То что мы показываем заказчику после разработки. Первые прототипы работающие

# SQL инъекции
Внедрение sql кода в процесс обработки вебстраницы например мы обращаемся к вебсайту по url `https://habr.com/ru/company/blog/65833` и например этот адрес заканчивается на какое нибудь число это число может быть ай дишником к которому обращается запрос типа `SELECT * FROM posts WHERE id = это число` часто бывает что это айдишник записи в таблице опытного программиста может навести на мысль , что мы можем ручками поправить это число `https://habr.com/ru/company/blog/65833;drop table users;` урл адрес примит это, распарсит, поймёт какой страничке это отдавать можно уронить сайт...опракинуть...
