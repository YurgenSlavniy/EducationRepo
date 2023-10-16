#  >>> mysql -u root -p
#  >>> mysql -u root -h 192.168.0.10 -P 3306 -p
# mysql> show databases; - посмотреть базы данных
# mysql> select version(); - посмотреть версию mysql
# mysql> exit; - выход
# mysql> SELECT 'Hello Databases';
# mysql> SHOW VARIABLES LIKE 'datadir';
# mysql> DESCRIBE users; - просмотр структуры таблицы
# mysql> HELP DESCRIBE; - помощь в консоли
#

# Команда   Сокращкение  Описание
# USE       \u           выбор БД
# SOURCE    \.           Выполнение sql-команд из файла
# SYSTEM    \!           Выполнение команды ОС
# STATUS    \s           Вывод информации о состоянии сервера
# EXIT      \q           Выход
#           \G           Вывод результата в вертикальном формате

# mysql> SELECT * FROM mysql.user LIMIT 1\G
# mysql> STATUS
# mysql> \s
# mysql> SYSTEM dir
# mysql> SOURCE hello.sql - выполнить файл
# mysql> mysqldump mysql > mysql.sql - дамп базы
# >>> tail -10 mysql.sql - прочитать последние 10 строчек файла
# mysql> mysql mysql < hello.sql - это когда мы хотим развернуть dump
# mysql> CREATE DATABASE crypto; - создадим базу данных с именем crypto
# mysql> SHOW VARIABLES LIKE 'datadir';
# >>> cd /crypto/
# >>> ls -la
# >>> cat db.opt
# >>> cd .. - возвращаемся на уровень выше
# >>> cp -r crypto foo   -r для рекурсивного копирования всего содержимого директории
# mysql> DROP DATABASE crypto; - удаление БД
# mysql> CREATE DATABASE IF NOT EXISTS crypto;
# mysql> DROP DATABASE IF EXIST crypto;
# mysql> USE crypto;
# mysql> SHOW TABLES FROM mysql;
# mysql> SELECT mysql.user.user, mysql.user.Host FROM mysql.User;
# >>> mysql -u root -p crypto;
# >>> CREATE TABLE users (k INT);
# >>> CREATE TABLE IF NOT EXIST users(k INT);
# mysql> DESCRIBE users; - просмотр структуры таблицы
# mysql> DESCRIBE user 'User'; - используем доп параметр имя столбца
# mysql> DESCRIBE user 'm%'; - все начинающеес на букву m
# mysql> SELECT * FROM information_schema.SCHEMATA;
# mysql> SELECT * FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'crypto';
# mysql> SELECT * FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'crypto'\G;
# -- это однострочный комментарий
# /* многострочный комментарий */
# mysql> SELECT id, name FROM users WHERE name='Игорь'
# mysql> SELECT 'Hello db\'s' - экранируем ковычку
# mysql> CREATE TABLE tbl (id INT(8)); - создаём таблицу tbl со столбцом id
# mysql> CREATE TABLE tbl (id INT(3) ZEROFILL); - ZEROFILL вместо пробелов отображать нули
# mysql> SELECT NULL;
# mysql> INSERT INTO tbl VALUES (5); - поместим в таблицу число 5
# mysql> DROP TABLE IF EXISTS tbl;
#        CREATE TABLE tbl (
#        name CHAR(10) DEFAULT 'anonimus',
#        description VARCHAR(255)
#    );
# mysql> ALTER TABLE tbl CHANGE id id INT UNSIGNED NOT NULL; - изменения в таблице
# mysql> TRUNCATE tbl; - очищает таблицу
# mysql> DESCRIBE tbl\G; - Посмотреть структуру таблицы
# mysql> SELECT '2021-09-09 00:00:00' - INTERVAL 1 DAY
# mysql> SELECT '2021-09-09 00:00:00' + INTERVAL 1 WEEK
# mysql> SELECT '2021-09-09 00:00:00' + INTERVAL '1-1' YEAR_MONTH
# mysql> ALTER TABLE tbl ADD collect JSON; -  добавим столбец при помощи ALTER TABLE
# mysql> INSERT INTO tbl VALUES (1, '{"first": "Hello", "second": "World"}'); - вставляем данные
# mysql> SELECT collect->>"$.first" FROM tbl; - обращаться к полям JSON извлекая значение ключей
# mysql> DROP TABLE IF EXISTS users;
#   CREATE TABLE users (
#       id INT UNSIGNED NOT NULL,
#       name VARCHAR(255) COMMENT 'name buyer',
#       irthday_at DATE COMMENT 'user birhtday',
#       created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'date of registration',
#       updated_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT ON UPDATE CURRENT_TIMESTAMP 'date of update'
#       ) COMMENT = 'buyers'; - создание талицы
# mysql> PRIMARY KEY(id);  - обьявление первичного ключа
# mysql> PRIMARY KEY(id, name(10)) -  допустимо объявление индека не по одному столбцу по двум и более
# mysql> id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT; - автоматическое создание уникального номера
# SERIAL == BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE
# mysql> CREATE INDEX index_of_catalog_id ON products (catalog_id); - создание индекса
# mysql> CREATE INDEX index_of_catalog_id USING BTREE ON products (catalog_id); - с указанием типа индекса
# mysql> INSERT INTO catalogs VALUES (NULL, 'Процессоры'); - вставка данных
# mysql> INSERT INTO catalogs VALUES (NULL, 'Мат.платы'); - вставка данных
# mysql> INSERT INTO catalogs VALUES (NULL, 'Видеокарты'); - вставка данных
# Многострочная вставка
#   mysql> INSERT INTO catalogs VALUES
#       (NULL, 'процессоры'),
#       (NULL, 'Мат.платы'),
#       (NULL, 'Видеокарты');
# mysql> INSERT INTO catalogs (id, name) VALUES (NULL, 'Motherboards');
# mysql> UNIQUE unigue_name(name(10)); - проиндексируем только первые 10 символов
# mysql> INSERT IGNORE INTO catalogs VALUES (NULL, 'Processors'); - вставка с игнорированием существующих значений
# mysql> DELETE FROM catalogs; - удаление записей
# mysql> TRUNCATE catalogs; - удаляет все записи и обнуляет счётчики AUTOINCREMANT
# mysql> DELETE FROM catalogs LIMIT 2; - первые 2 записи таблицы удалятся
# mysql> DELETE FROM catalogs WHERE id > 1 LIMIT 1; - Удалять только те записи первичный ключ ай ди которых больше 1
# mysql> UPDATE
#   catalogs
# SET
#   name = 'Processors (Intel)'
# WHERE
#   name = 'Processors'; - обновление данных
# mysql>  INSERT INTO
#        cat
#    SELECT
#        *
#    FROM
#        catalogs; - позволяет вставлять записи из одной таблицы в другую
# >>> mysqldump -u root -p crypto > crypto.sql - ДАМП БАЗЫ ДАННЫХ В КОМАНДНОЙ СТРОКЕ!
# >>> dir - посмотреть содержимое папки в командной строке виндоус
# >>> mysql -u root -p new_db < crypto.sql - загрузка дампа в майсикюль
#
#
# #############################
