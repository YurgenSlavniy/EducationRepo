# УРОК 2.
# Управление БД. Язык запросов SQL

- Типы баз данных
- Основы реляционных БД
- MySQL и клиенты
- Управление БД

- Данные и программы
- Иерархические БД
- Сетевые БД
- Реляционные БД
- NoSQL БД
- БД в современных приложениях

Данные живут дольше программ. Одни и теже данные могут обслуживать несколько программ одновременно. (десктопная программа, web сайт, мобильное приложение) могут обращаться к одной БД. Данные отделяются от кода и хронятся в БД отдельно.

### Трудности работы с файлами:
- Трудно добиться компактности
- Сложно обеспечить конкурентный доступ
- Затруднено удаление и редактирование данных
- Сканирование всех данных во время поиска
- файл может не помещаться на компьютере
- конфликты при совместном редактировании

данные лучше записывать для компактности в бинарном. а не в текстовом формате

### Системы управления БД (СУБД). Надстройка для БД
Для управления, редактирования, и удобной работы с БД

История развития СУБД:

- Иерархические
- Сетевые
- Реляционные
- NoSQL

##### Иерархические БД
Иерархия дерево состоящие из узлов.

`Транспорт:` водный воздушный наземный. `Водный:` речной морской. Наземный: Авто ЖД

Есть вершина - транспорт. от него расходятся 3 ветки
1) водный
2) воздушный
3) наземный

от водного расходятся 2 ветки
1) речной
2) морской
 
минус иерархий: невозможность реализовать отношение многие-ко-многим

##### сетевая бд 
Одна запись участвует в нескольких отношениях предок-потомок. сейчас реализуются в виде графовых СУБД

##### реляционные БД
Отсутствие явной структуры предок-потомок, все данные в виде простых таблиц, разбитых на строки и столбцы, самый распространёный вид БД

##### Реляционные СУБД:
Коммерческие: 
- Oracle,
- MS SQL (Microsoft),
- DB2 (IBM),

свободные СУБД:
- MySQL,
- PostgreSQL,
- Firebird

`db-engines.com`  - можно следить за рейтингом БД

Если раньше на одном сервере умещалось множество сайтов, то сейчас один сайт занимает множество серверов с базами данных. Анологичное развитие - множество сайтов к одной БД. А сейчас один сайт к множеству БД. Распределённые хранилища.

##### Специализированные NoSQL БД
- Redis,
- MongoDB,
- ElasticSearch,
- ClickHouse,
- Cassandra

Могут полностью распологаться в оперативной памяти со своим языком запросов. Например Redis. Очень быстрое хронилище построенное по принципу: ключ-значение, оно полностью расположено в оперативной памяти. Сервер реализован в виде однопоточного eventloop цикла поток опрашивает по кругу соединения в неблокирующем режиме за счёт того что не происходит переключение процессора на другие процессы достигается гигантская производительность достигающая 100 000 рпс.

Сейчас актуально совместное использование СУБД под конкретные задачи специализированные БД нам надо запоминать результаты ресурсоёмкой операции для ускорения и кэш в оперативной памяти - REDIS.  Основная БД для долговременного хронения - MySQL. Искать данные, полнотекстовый поиск - ElasticSearch. Перемолоть большие объёмы накопенных данных колоночная БД - ClickHouse

### Основы реляционных БД
- реляционные БД
- Таблицы, строки и столбцы
- первичные и внешние ключи
- Транзакции ACID
- CAP-теорема

В реаляционных БД информация организована в виде прямоугольных таблиц разделёных на строки и столбцы на пересечении которых содержится значение. БД состоит из нескольких таблиц. Каждая таблица имеет уникальное имя описывающее её содержимое

Начнём формировать БД. На пересечении столбца и строки содержится только одно значение. Все значения содержащиеся в одном и том же столбце - данные одного типа. У каждого столбца в таблице есть своё имя обычно служит заголовком столбца. Все столбцы в одной таблице должны иметь уникальные имена. Разрешается присваивать одинаовые имена столбцам, расположенным в разных таблицах. столбцы таблицы упорядочены слева направо. У любой таблицы есть минимум один столбец. В таблице может содержаться любое количество строк в том числе и ноль строк. в этом случае таблица путсая. т.к строки не упорядочены, в таблице нет первой, поледней n-ой строки. В правильно построенной РБД в каждой таблице есть столбец, или комбинация столбцов, для кторого значения во всех строках различны (столбец ID с порядковыми номерами) этот столбец или столбцы - ПЕРВИЧНЫЙ КЛЮЧ (primary key). Первичный ключ у каждой строки - уникален. Таблица в которой все строки отличаются друг от друга в математических терминах   - отношения (Relation)

В иерархических БД очень легко выстраивать отношения `предок-потомок`. 

Столбец одной таблицы, значения которого совпадают со значением столбца, являющегося первичным ключом другой таблицы называется `внешним ключом`
```
Categories
|id | name          |
|1  | Процессоры    |
|2  | Видеокарты    |
```
```
products
|id | name          | category_id  |
| 1 |intel core i7  | 1            |
| 2 |intel xeon     | 1            |
| 3 |AMD  Ryzen     | 1            |
| 4 |GeForce 1060   | 2            |
| 5 |Radeon RX 5500 | 2            |
| 6 |GeForce 1280   | 2            |
```
category_id  - `ВНЕШНИЙ КЛЮЧ`

В РБД можно извлекать связанные между собой данные, используя эти отношения

В приложении многое может пойти не так:
- отказ аппаратного обеспечения
- исключительная ситуация внутри приложения
 разрыв сети может отрезать приложение от БД

все эти проблемы обычно решаются при омощи транзакций.

`ТРАНЗАКЦИИ ` - способ группировки приложением нескольких операций записи и чтения в одну логическую единицу все опрации записи и чтения выполняются как одна, все транзакции либо целиком выполняются успешно с фиксацией изменений либо целиком завершается неудачно с прерыванием и откатом к исходному состоянию.

Почти все РБД поддерживают транзакции

Исходные гарантии безопасности которые должны обеспечивать транзакции:
##### ACID
- `a` - atomicy - атомарность (Реакция БД на сбой)
- `c` - consistency - согласованность
- `i` - isolation  - изолированность
- (параллельно выполняемые транзакции изолированы друг от друга)
- `d` - durability  - сохраняемость

допустимость или недопустимость данных проверяется приложением. БД лишь обеспечивает хронение

С развитием web мы получили приложения к которым одновременно обращаются тысячи клиентов это приводит к проблеме масштабированности БД

Одна БД может оказаться на разных машинах и даже в разных data центрах. Как только БД оказывается распределённой необходимо обеспечивать устойчивость к сетевым сбоям. Противоречие обеспечения согласованности и распределёности систем
##### CAP-теорема
Теорема касается трёх взаимосвязанных терминах:
1) `доступность (availibility)` - Все клиенты БД всегда имеют возможность читать и записвать БД
2) `согласованность (consistency)` - Все клиенты должны прочитать одно и тоже значение в ответ на один и тот же запрос
3) `Устойчивость к разделению (Partition tolerance)` - БД можно разделить между несколькими машинами и она продолжет работу даже в случае отказа сегмента сети

Теорема утверждает, что в любой системе можно гарантировано обеспечить выполнение только 2ух из этих трёх требований. Аналог поговорки:
```
программа может быть хорошей, быстрой и дешёвой выбирайте любые 2 свойства.
```

Чем больше требуется согласованность от системы тем меньше будет её устойчивость к разделению в распределёной системе сетевые сбою вероятны мы не можем избежать задержек и потери пакетов избежать узла устойчивости к разделению в современых реалиях практически невозможно.

Традиционные реляционные СУБД спроектированы для работы на одном компьютере обеспечивают согласованность и доступность и с трудом может обеспечить устойчивость к разделению.

# MySQL И КЛИЕНТЫ

- СУБД MySQL
- Клиент-серверное взаимодействие
- Утилита mysql
- Конфигурационный файл .my.cnf
- Утилита mysqldump SQL-дамп

MySQL на сегодняшний день самая популярная БД с открытым кодом. Например википедия создана с применением MySQL. Существует множество форков БД

### Архитектура MySQL
Условно разбивается на 2 части:
1) ядро - сама БД
2) движки которые реализуют тот или иной механизм БД

InnoDB, MyISAM, Memory, Archive

Такая архитектура позволяет разробатывать БД усилиями нескольких команд кто то сосредотачивается на ядре, кто то на отдельном движке

MySQL построена по клиент-серверной технологии. Сервер хронит и обслуживает БД. Клиенты шлют ему запросы на языке SQL и получают в ответ результирующие таблицы с данными. Клиентами могут выступать разные программы:
- mysql,
- Dbeaver,
- Ruby,
- Python,
- Java

Например программа Dbeaver позволяет подключаться к различным БД и доступна в основных ОС

### Будем учиться работать в консольных утилитах.
в командной строке
```
>>> mysql -u root -p
```
Вводим пароль и у нас в консоле запускается сервер и в консольном окне можно работать с скюль запросами.
```
mysql> SELECT 'Hello Databases';
```

КОМАНДЫ ЗАВЕРШАЮТСЯ ";" - СИНТАКСИ

Только после того как консольный клиент mysql встретит ';' команда отправляется на сервер. Обратим внимание на результирующую таблицу
```
 +-----------------+
| Hello Databases |
+-----------------+
| Hello Databases |
+-----------------+
1 row in set
```
В первой строке таблицы с результатами содержится заголовок столбцов в следующих строках идёт ответ сервера на запрос для ввода команд можем использовать любой регистр (верхний и нижний). `КЛАВИШИ ВВЕРХ И ВНИЗ ДЛЯ ПРОСМОТРА ВВЕДЁНЫХ КОМАНД`

Если сервер установлен на удалённом хосте, соединяемся указав ай пи адрес или домен удалёного сервера в параметре ейч (h) в параметре P мы можем указать порт
```
>>> mysql -u root -h 192.168.0.10 -P 3306 -p
```
Утилиты mysql поддерживает различные команды:
```
Команда   Сокращкение  Описание
USE       \u           выбор БД
SOURCE    \.           Выполнение sql-команд из файла
SYSTEM    \!           Выполнение команды ОС
STATUS    \s           Вывод информации о состоянии сервера
EXIT      \q           Выход
          \G           Вывод результата в вертикальном формате
```

`\G` иногда результирующие таблицы очень велики и они рассыпаются в консольном выводе
```
mysql> SELECT * FROM mysql.user LIMIT 1\G
```
-->
```
*************************** 1. row ***************************
                    Host: localhost
                    User: debian-sys-maint
             Select_priv: Y
             Insert_priv: Y
             Update_priv: Y
             Delete_priv: Y
             Create_priv: Y
               Drop_priv: Y
             Reload_priv: Y
           Shutdown_priv: Y
            Process_priv: Y
               File_priv: Y
              Grant_priv: Y
         References_priv: Y
              Index_priv: Y
              Alter_priv: Y
            Show_db_priv: Y
              Super_priv: Y
   Create_tmp_table_priv: Y
        Lock_tables_priv: Y
            Execute_priv: Y
         Repl_slave_priv: Y
        Repl_client_priv: Y
        Create_view_priv: Y
          Show_view_priv: Y
     Create_routine_priv: Y
      Alter_routine_priv: Y
        Create_user_priv: Y
              Event_priv: Y
            Trigger_priv: Y
  Create_tablespace_priv: Y
                ssl_type: 
              ssl_cipher: 0x
             x509_issuer: 0x
            x509_subject: 0x
           max_questions: 0
             max_updates: 0
         max_connections: 0
    max_user_connections: 0
                  plugin: caching_sha2_password
   authentication_string: $A$005$
                                 @F~<,zGg
                                         GjTVrKxBLEfbIu0sk.DGdZK.gdYIoSDtN/UNpMEbi.b8
        password_expired: N
   password_last_changed: 2023-09-18 12:02:09
       password_lifetime: NULL
          account_locked: N
        Create_role_priv: Y
          Drop_role_priv: Y
  Password_reuse_history: NULL
     Password_reuse_time: NULL
Password_require_current: NULL
         User_attributes: NULL
1 row in set (0,00 sec)

```
это команда mysql а не часть sql запроса

Посмотрим как работают разные команды:
```
mysql> STATUS
```
запрос статуса сервера
```
mysql> \s
```
Аналогичная команда в сокращёном варианте
-->
```
mysql  Ver 8.0.34-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))

Connection id:		24
Current database:	
Current user:		root@localhost
SSL:			Not in use
Current pager:		stdout
Using outfile:		''
Using delimiter:	;
Server version:		8.0.34-0ubuntu0.20.04.1 (Ubuntu)
Protocol version:	10
Connection:		Localhost via UNIX socket
Server characterset:	utf8mb4
Db     characterset:	utf8mb4
Client characterset:	utf8mb4
Conn.  characterset:	utf8mb4
UNIX socket:		/var/run/mysqld/mysqld.sock
Binary data as:		Hexadecimal
Uptime:			21 hours 39 min 27 sec

Threads: 2  Questions: 78  Slow queries: 0  Opens: 184  Flush tables: 3  Open tables: 103  Queries per second avg: 0.001
--------------
```
выполнить системную команду:
```
mysql> SYSTEM ls
```
Для linux и Mac и для windows:
```
mysql> SYSTEM dir
```
в сокращённом варианте
```
mysql> \! dir
```

Команды можно набирать в файлах в любом редакторе. После того как sql файл сформирован, мы можем выполнить его при помощи команды SOURCE

Воспользуемся редактором DBeaver для создания sql файла
1) ВП -> Новое соединение
2) ВП -> Открыть скрипт SQL
3) в открывшимся пространстве
```
>>> SELECT 'Hello database!;
```
4) ВП -> файл -> сохранить как

Файл с рабочего стола не получилось запустить. Затем файл перетащил в папку `C:\Program Files\MySQL\MySQL Server 8.0\bin` где аходится MySQL.exe
```
mysql> SOURCE hello.sql
```
-->
```
+-----------------+
| Hello Databases |
+-----------------+
| Hello Databases |
+-----------------+
1 row in set
```
Файл открылся ! и команды записанные в файле отработают

короткий вариант команды
```
mysql> \. hello.sql
```

### Специальный конфигурационный файл:
Обычно распологается в домашней директории пользователя, если параметры не задаются явно, они извлекаются из конфигурационного файла

создадим файл с помощью клиента DBeaver
```
>>> [mysql]
    user=root
    password=0108
```
Конфиг файлы sql начинаются обычно с секций. Секция начинается с квадратных скобок в которых указывается утилита. Мы настраиваем утилиту [mysql]
- user=root - укажем имя пользователя
- password=0108 и его пароль

сохранить как .my.cnf

Теперь можем запускать mysql без запуска пароля.

### Перенос бд с одного сервера на другой или создание резервной копии бд.
Для этого создаётся `sql dump` текстовый файл с командами

### утилита mysql dump
Откроем в Dbreaver сновва файл `.my.cnf` и внесём изменения
```
[client]
user=root
password=0108
```
`[client]` означает что для всех дестрибютивов mysql

создадтим дамп системной базы mysql
```
mysql> mysqldump mysql > mysql.sql
```
> mysql.sql - перенаправляем > в файл mysql.sql

```
>>> tail -10 mysql.sql
```
прочитать последние 10 строчек файла

```
mysql> mysql mysql < hello.sql
```
Это когда мы хотим развернуть dump мы будем пользоваться утилитой mysql, далее указываем базу данных, вторая mysql в  mysql> mysql mysql < hello.sql и направляем туда содержимое файла < hello.sql

### УПРАВЛЕНИЕ БАЗАМИ ДАННЫХ
- создание и удаление баз данных
- текущая база данных
- создание и удаление таблиц
- оператор SHOW
- информационная схема
- документация

Запустим клиент  `mysql`

`CTRL + l` - очистка экрана

Создать базу данных с помощью SQL оператора
```
mysql> CREATE DATABASE crypto;
```
Cоздадим базу данных с именем crypto, бд создана. Посмотрим список существующих БД
```
mysql> SHOW DATABASES;
```
БД появилась в списке. Узнаем где расположен каталог данных
```
mysql> SHOW VARIABLES LIKE 'datadir';
```
--> 
```
/var/lib/mysql/
```

`CTRL + D` - выходим из MySQL
```
mysql> exit
mysql> \q
```
Каждая папка - это база данных
```
>>> cd /crypto/
>>> ls -la
```
--> видим файл db.opt
```
>>> cat db.opt
```
--> 
```
default-character-set=utf8
default-collation=utf8_general_ci
```
Это файл с настройками кодировки
```
>>> cd ..
```
Возвращаемся на уровень выше
```
>>> cp -r crypto foo
```
`-r` для рекурсивного копирования всего содержимого директории, `crypto foo` - мы скопировали каталог crypto в каталог foo

Для копирования таблиц лучше применять sql dump или к специализированным утилитам

### УДАЛЕНИЕ БАЗ ДАННЫХ
```
mysql> DROP DATABASE crypto;
```
Чтобы избежать моментов повторяющихся имён
```
mysql> CREATE DATABASE IF NOT EXISTS crypto;
```
Если бд с таким именем уже существует ничего не произойдёт
```
mysql> DROP DATABASE IF EXIST crypto;
```
Если база данных есть она удалится, если бд нет - ничего не произойдёт

Запросим список текущих таблиц не выбирая БД
```
mysql>  SHOW TABLES;
```
--> 
```
No database selected
```
Cообщние об ошибке - бд не выбрана
```
mysql> USE crypto
```
`;` можно не указывать т.к `USE` не является SQL оператором, а является командой клиента mysql
```
mysql>  SHOW TABLES;
```
Отработало без ошибки

Если не выбирать БД. то в каждом операторе надо явно указывать какая БД будет использоваться
```
mysql>  SHOW TABLES FROM mysql;
mysql>  SHOW TABLES FROM crypto;
```
```
mysql> SELECT mysql.user.user, mysql.user.Host FROM mysql.User;
```
В операторе select мы явно указываем имя БД mysql. Имя таблицы user. и имя столбцов user Host и в ключевой команде `FROM` указываем имя БД и таблицы `FROM mysql.user;`
```
>>> mysql -u root -p crypto;
```
Мы выбрали БД по умолчанию crypto при входе

### СОЗДАНИЕ ТАБЛИЦЫ ВНУТРИ БД
```
>>> CREATE TABLE имя_таблицы (
      имя_столбца параметры,
      имя_столбца параметры,
     ...
       )
```
```
>>> CREATE TABLE users (k INT);
```
Создалась таблица с именем users в которой есть одна колонка k и значения в этой колонке INT

При повторной попытки создать такую же таблицу у нас сообщение об ошибке, чтобы этого избежать
```
>>> CREATE TABLE IF NOT EXIST users(k INT);
```
Если такой таблицы нет то она создастся, иначе ничего не произойдёт
```
>>> SHOW TABLES;
```
смотрим создана ли таблица 
```
mysql> SHOW TABLES;
```
```
+------------------+
| Tables_in_crypto |
+------------------+
| tradepair        |
+------------------+
1 row in set (1,20 sec)
```
### ПРОСМОТР СТРУКТУР ТАБЛИЦЫ
```
>>> DESCRIBE users;
```
-->
```
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| first | int(11) | YES  |     | NULL    |       |
+-------+---------+------+-----+---------+-------+
1 row in set (2,30 sec)
```
Каждая строка в результирующей таблице соответствует отдельному столбцу. У нас в таблице содержится единственный столбец Field :first

Выберем бд Mysql чтобы порботать с боле еобъёмной таблицей
```
>>> USE mysql;
>>> DESCRIBE user;
```
Оператор Describe может принимать доп. параметр - имя столбца
```
>>> DESCRIBE user 'User';
```
-->
```
+-------+----------+------+-----+---------+-------+
| Field | Type     | Null | Key | Default | Extra |
 +-------+----------+------+-----+---------+-------+
| User  | char(32) | NO   | PRI |         |       |
+-------+----------+------+-----+---------+-------+
 1 row in set (0,00 sec)
```
Используем лайтшаблоны вместе с оператором DESCRIBE заменять с помощью символа процента `%` любое количество символов, а символом `_` один символ. Запросим с таблице юзер все столбцы, которе начинаются с символа m
```
>>> DESCRIBE user 'm%';
```
-->
```
+----------------------+------------------+------+-----+---------+-------+
| Field                | Type             | Null | Key | Default | Extra |
+----------------------+------------------+------+-----+---------+-------+
| max_questions        | int(11) unsigned | NO   |     | 0       |       |
| max_updates          | int(11) unsigned | NO   |     | 0       |       |
| max_connections      | int(11) unsigned | NO   |     | 0       |       |
| max_user_connections | int(11) unsigned | NO   |     | 0       |       |
+----------------------+------------------+------+-----+---------+-------+
4 rows in set (0,00 sec)
```
Операторы SHOW DESCRIBE не реализуют другие БД.

БД information_schema находится в ОЗУ , специальная, её невозможно выбрать с помощью команды USE INSERT UPDATE DELITE нельзя выполнять для таблиц этой БД. Имеем дело не с таблицами а с представлениями
```
>>>SHOW DATABASES;
```
-->
```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| crypto             |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (1,52 sec)
```
Запросим весь список баз данных из information_schema
```
>>> SELECT * FROM information_schema.SCHEMATA;
```
-->
```
+--------------+--------------------+----------------------------+------------------------+----------+
| CATALOG_NAME | SCHEMA_NAME        | DEFAULT_CHARACTER_SET_NAME | DEFAULT_COLLATION_NAME | SQL_PATH |
+--------------+--------------------+----------------------------+------------------------+----------+
| def          | information_schema | utf8                       | utf8_general_ci        | NULL     |
| def          | crypto             | latin1                     | latin1_swedish_ci      | NULL     |
| def          | mysql              | latin1                     | latin1_swedish_ci      | NULL     |
| def          | performance_schema | utf8                       | utf8_general_ci        | NULL     |
| def          | sys                | utf8                       | utf8_general_ci        | NULL     |
+--------------+--------------------+----------------------------+------------------------+----------+
5 rows in set (0,00 sec)
```
```
>>> SELECT * FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'crypto';
```
-->
```
+---------------+--------------+------------+------------+--------+---------+------------+------------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+-------------+------------+-------------------+----------+----------------+---------------+
| TABLE_CATALOG | TABLE_SCHEMA | TABLE_NAME | TABLE_TYPE | ENGINE | VERSION | ROW_FORMAT | TABLE_ROWS | AVG_ROW_LENGTH | DATA_LENGTH | MAX_DATA_LENGTH | INDEX_LENGTH | DATA_FREE | AUTO_INCREMENT | CREATE_TIME         | UPDATE_TIME | CHECK_TIME | TABLE_COLLATION   | CHECKSUM | CREATE_OPTIONS | TABLE_COMMENT |
+---------------+--------------+------------+------------+--------+---------+------------+------------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+-------------+------------+-------------------+----------+----------------+---------------+
| def           | crypto       | tradepair  | BASE TABLE | InnoDB |      10 | Dynamic    |          0 |              0 |       16384 |               0 |            0 |         0 |           NULL | 2021-09-05 19:42:15 | NULL        | NULL       | latin1_swedish_ci |     NULL |                |               |
+---------------+--------------+------------+------------+--------+---------+------------+------------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+-------------+------------+-------------------+----------+----------------+---------------+
1 row in set (0,14 sec)
```
Воспользуемся вертикальным выводом:
```
>>> SELECT * FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'crypto'\G;
```
-->
```
# *************************** 1. row ***************************
#   TABLE_CATALOG: def
#    TABLE_SCHEMA: crypto
#      TABLE_NAME: tradepair
#      TABLE_TYPE: BASE TABLE
#          ENGINE: InnoDB
#         VERSION: 10
#      ROW_FORMAT: Dynamic
#      TABLE_ROWS: 0
#  AVG_ROW_LENGTH: 0
#     DATA_LENGTH: 16384
# MAX_DATA_LENGTH: 0
#    INDEX_LENGTH: 0
#       DATA_FREE: 0
#  AUTO_INCREMENT: NULL
#     CREATE_TIME: 2021-09-05 19:42:15
#     UPDATE_TIME: NULL
#      CHECK_TIME: NULL
# TABLE_COLLATION: latin1_swedish_ci
#        CHECKSUM: NULL
#  CREATE_OPTIONS:
#   TABLE_COMMENT:
# 1 row in set (0,00 sec)
#
# ERROR:
# No query specified
```
```
mysql> HELP DESCRIBE;
```
откроет помощь прямо в коноле

# ВВЕДЕНИЕ В SQL
- ЧИСЛОВЫЕ И СТРОКОВЫЕ ТИПЫ ДАННЫХ
- КАЛЕНДАРНЫЕ ТИПЫ ДАННЫХ И МНОЖЕСТВА
- ИНДЕКСЫ
- CRUD-ОПЕРАЦИИ

### ВВЕДЕНИЕ В SQL
- стандарт sql
- Описание данных DDL
- управление данными DML
- комментарии
- ключевые слова
- кавычки и их использование

# SQL - STRUCTURED QUERY LANGUAGE
Язык для интерактивного общения с СУБД

Достоинства:
- декларативная природа
- высокоуровневая структура
- высокая эффективность обработки множеств
- независимость от конкретных СУБД
- межплатформенная переносимость
- наличие стандартов

Недостатки:
- слабоструктурированый язык
- язык старый
- Плохо взаимодействует с ООП-языками
- SQL - не универсальный язык
- Множество диалектов

Элементы языка:
- комментарии
- скалярные выражения
- ключевые слова
 операторы
- таблицы
- столбцы
- индексы
- предопределенные функции
- представления
- переменные
- хранимые процедуры
- хранимые функции
- триггенры
- коды ошибок

### КОММЕНТАРИИ .
Односрочные начинаются с 2 ух символов дефиса `--`. `--` это однострочный комментарий

`/* многострочный комментарий */`

### DDL (Data Definition Language) - язык описания данных

Инструкция создания, удаления, редактирования бд и таблиц, операторы позволяющие воссоздать структуру БД

### DML (Data Manipulation Language) - язык управления данных

Запросы на зоздание, удаление и извлечения данных из бд из таблиц. Операторы обслуживающие данные которые хронятся внутри бд

### структура запроса
```
mysql> SELECT id, name FROM users WHERE name='Игорь'
```
ключевые слова : `SELECT, FROM, WHERE`

- `SELECT id, name ` (id, name - столбцы)
- `FROM users` (users - тблица)
- `WHERE name='Игорь'` ( name='Игорь' - скалярное выражение)

Скалярные выражения - числа и строки. фактически это константы
```
mysql> SELECT 'Hello db!'
```
'Hello db!' - скалярное выражение
```
#   mysql> SELECT 'Hello db!'s'
```
когда ковычки внутри ковычек интерпритатор запутается надо экранировать символ ковычек при помощи слэша
```
mysql> SELECT 'Hello db\'s'
```
также можем воспользовться двойными ковычками
```
mysql> SELECT "Hello db's"
```

Имена БД , таблиц, столбцов строк могут содержать разные символы кроме `|\./` если имя совпадает с ключевым словом его заключают в обратные ковычки `
```
mysql> CREATE TABLE tbl (create INT)
```
имя команды CREATE совпадает с именем столбца create мы получим ошибку.
```
mysql> CREATE TABLE tbl (`create` INT)
```

ТИПЫ ДАННЫХ:
- типы данных
- целые числа
- вещественные числа
- строки

В таблице в каждом столбце данные одного типа

### Типы данных MySQL:
- числовые (целые, вещественные с плавающей точкой)
- строковые (фиксированные, переменного типа)
- NULL (неопределённое значение, отсутствие информации)
- календарные (сохраниение даты и времени)
- коллекции (множество значение , json документ)

### Атрибуты
- `NULL или NOT NULL` (задаёт ограничение на столбец, позволяя присваивать элементам неопределённые значения)
- `DEFAULT` (задать полю значени епо умолчанию)
- `UNSIGNED` (только для числовых значений запрещает хронить отрицательные значения)

- `INT` (-2 147 683 648  до 2 147 683 647)
- `INT` (-2^31  до 2^31)
- `INT UNSIGNED` (0 - 4 294 967 295 )  (0 - 2^32)

### Числовые типы

числовые:
1) целочисленные
```
TINYINT (1 байт = 8 бит) (0 - 2^8) (0-256) (-128 до 127)
SMALLINT
MEDIUMINT
INT
BIGINT
```
2) вещественные (с плавающий точкой)
```
#   FLOAT
#   DOUBLE
```
3) точные
```
DECIMAL
```

```
mysql> CREATE TABLE tbl (id INT(8));
```
Cоздаём таблицу `tbl` со столбцом `id` тип данных `INT`  и поле размером `8` символов (8)

поместим в таблицу число 5
```
mysql> INSERT INTO tbl VALUES (5);
```
выведим содержимое таблицы
```
mysql> SELECT * FROM tbl;
```
-->
```
+------+
| id   |
+------+
|    1 |
+------+
```
```
mysql> DROP TABLE IF EXISTS tbl;
```
Удаляем таблицу tbl
```
mysql> CREATE TABLE tbl (id INT(3) ZEROFILL);
```
Создадим таблицу, где столбец id будет содержать числовое значение INT, столбец будет занимать 3 символа INT(3), ZEROFILL вместо пробелов отображать нули
```
mysql> INSERT INTO tbl VALUES (1);
```
поместим в таблицу значение 1
```
mysql> SELECT * FROM tbl;
```
-->
```
# +------+
# | id   |
# +------+
# |  001 |
# +------+
```

Можем указывать количество символов после INT
```
mysql> INSERT INTO tbl VALUES (1000);
mysql> SELECT * FROM tbl;
```
-->
```
+------+
| id   |
+------+
|  001 |
|  200 |
+------+
```

- FLOAT - 4 байта
- DOUBLE - 8 байт
- DECIMAL(7,4) 111.2000 - под всё число отводится 7 байт под дробную часть 4 байта число хранится в  виде строки максимально возможное 999.9999
```
mysql> CREATE TABLE tbldec (price DECIMAL(7,4));
mysql> INSERT INTO tbldec VALUES (111.2);
mysql> SELECT * FROM tbldec;
```
попытаемся ввести число которое не подходит под условия
```
mysql> INSERT INTO tbldec VALUES (11111)
```
сообщение об ошибке

### СТРОКОВЫЕ ТИПЫ
строковые:
- фиксированные (имеется фиксированный размер)
```
CHAR
```
- переменные (нет фикс. размера)
```
VARCHAR
```
- BLOB (для хронения бинарных больших объёмов)
```
TINYTEXT
TEXT
MEDIUMTEXT
LONGTEXT
```
В круглых скобках после типа можно задать максимальный размер строки

Создадим таблицу со строковыми данными. Воспользуемся графическим редактором DBeaver
```
ВП -> Редактор SQL -> открылся блокнот
>>> DROP TABLE IF EXISTS tbl;
    CREATE TABLE tbl (
    name CHAR(10) DEFAULT 'anonimus',
    description VARCHAR(255)
  );
```
`name CHAR(10) DEFAULT 'anonimus'` создали столбец - `name`, тип данных фиксированный `CHAR`, `(10)` - фиксированный размер 10 байт `DEFAULT 'anonimus'` - если имя не задано,то по умалчанию имя будет 'anonimus' создали столбец `description`, `VARCHAR(255)` - переменного размера, `(255)` байт будет дано на это столбец

вставим новую строку
```
>>> INSERT INTO tbl VALUES (DEFAULT, 'Новый пользователь');
>>> INSERT INTO tbl VALUES ('Юрген', 'Новый пользователь');
>>> SELECT * FROM tbl;
```
Если имя будет больше чем 10 символов - ошибка выпадет, `ALT + X` запустить скрипт в DBeaver

Столкнулся со следующими трудностями и ошибками. В DBeaver надо ВП -> текущее соединение выставляю `MySQL Host`, ВП -> текущий каталог\схема - выбираю `crypto` базу данных в командах
```
>>> INSERT INTO tbl VALUES (DEFAULT, 'Новый пользователь');
```
Русские символы не читаются и БД ругается в дебивере, надо менять кодировку или использовать латиницу

Итого рабочий скрипт:
 ```
DROP TABLE IF EXISTS tbl;
CREATE TABLE tbl (
 	name CHAR(10) DEFAULT 'anonimus',
 	description VARCHAR(255)
);
INSERT INTO tbl VALUES (DEFAULT, 'New User');
INSERT INTO tbl VALUES ('Yurgen', 'User');
SELECT * FROM tbl;
```
Запись переменной длины под неё отводится 65536 байт (2^16)

Для хранения объёмного текста используется тип `TEXT`
```
TINYTEXT 2^8 байт
TEXT 2^16
MEDIUMTEXT 2^24
LONGTEXT 2^32
```

# СОЗДАДИМ УЧЕБНУЮ БД

Мы создаём интернет магазин в БД crypto

1) создадим файл `shop.sql` куда будем записывать наши наработки.
- ВП -> открыть скрипт SQL -> новый скрипт
- ПКМ -> переиминовать в shop.sql
  
2) первым делом создадим таблицу `catalog`
```
mysql> DROP TABLE IF EXISTS catalogs;
```
удаляем таблицу если она существует
```
mysql> CREATE TABLE catalogs (
      id INT UNSIGNED,
      name VARCHAR(255) COMMENT 'название раздела'
  ) COMMENT = 'Разделы интернет магазина';
```

- `id INT UNSIGNED,` - создадим первичный ключ
- `UNSIGNED` т.к отрицательные значения нам не нужны
- `name` имя для каталога . тип данных VARCHAR(255)
- таблицы и столбцы можно снабжать комментариями

По аналогии составляем БД для пользователей
```
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT UNSIGNED,
    name VARCHAR(255) COMMENT 'name buyer'
) COMMENT = 'buyers';
```
Создадим таблицу для товара
```
DROP TABLE IF EXISTS products;
CREATE TABLE products (
   id INT UNSIGNED,
   name VARCHAR(255) COMMENT 'название',
   discription TEXT COMMENT 'описание',
   price DECIMAL (11,2) COMMENT 'цена',
   catalog_id INT UNSIGNED
) COMMENT = 'Товарные позиции';
```
Нам потребуются заказы пользователей, первичный ключ ай ди и юзер ай ди
```
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
   id INT UNSIGNED,
   user_id INT UNSIGNED
) COMMENT = 'orders';
```
Введём промежуточную таблицу
```
DROP TABLE IF EXISTS orders_products;
CREATE TABLE orders_products (
   id INT UNSIGNED,
   order_id INT UNSIGNED,
   product_id INT UNSIGNED,
   total INT UNSIGNED DEFAULT 1 COMMENT 'all orders'
) COMMENT = 'value orders';
```
таблица для скидок
```
DROP TABLE IF EXISTS discounts;
CREATE TABLE discounts (
   id INT UNSIGNED,
   user_id INT UNSIGNED,
   product_id INT UNSIGNED,
   discount FLOAT UNSIGNED COMMENT 'discount 0.0 - 1.0'
) COMMENT = 'discounts';
```
Введём таблицу склада и свяжем её с товаром
```
DROP TABLE IF EXISTS storehouses;
CREATE TABLE storehouses (
   id INT UNSIGNED,
   name VARCHAR(255) COMMENT 'name'
) COMMENT = 'storehouses';
```
```
DROP TABLE IF EXISTS storehouses_products;
CREATE TABLE storehouses_products (
   id INT UNSIGNED,
   storehouse_id INT UNSIGNED,
   product_id INT UNSIGNED,
   value INT UNSIGNED COMMENT 'value products'
) COMMENT = 'value products on storehouses';
```
Это всё каркас нашей учебной БД, скрипт выглядит целиком так:
```
DROP TABLE IF EXISTS catalogs;
CREATE TABLE catalogs (
    id INT UNSIGNED NOT NULL,
    name VARCHAR(255) COMMENT 'name BD categories'
) COMMENT = 'categories internet shop';

DROP TABLE IF EXISTS users;
CREATE TABLE users (
   id INT UNSIGNED NOT NULL,
   name VARCHAR(255) COMMENT 'name buyer'
) COMMENT = 'buyers';

DROP TABLE IF EXISTS products;
CREATE TABLE products (
   id INT UNSIGNED NOT NULL,
   name VARCHAR(255) COMMENT 'name',
   discription TEXT COMMENT 'discription',
   price DECIMAL (11,2) COMMENT 'price' ,
   catalog_id INT UNSIGNED
) COMMENT = 'Positions';LL

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
   id INT UNSIGNED NOT NULL,
   user_id INT UNSIGNED
) COMMENT = 'orders';

DROP TABLE IF EXISTS orders_products;
CREATE TABLE orders_products (
    id INT UNSIGNED NOT NULL,
    order_id INT UNSIGNED,
   product_id INT UNSIGNED,
   total INT UNSIGNED DEFAULT 1 COMMENT 'all orders'
) COMMENT = 'value orders';

DROP TABLE IF EXISTS discounts;
CREATE TABLE discounts (
   id INT UNSIGNED NOT NULL,
   user_id INT UNSIGNED,
   product_id INT UNSIGNED,
   discount FLOAT UNSIGNED COMMENT 'discount 0.0 - 1.0'
) COMMENT = 'discounts';

DROP TABLE IF EXISTS storehouses;
CREATE TABLE storehouses (
   id INT UNSIGNED NOT NULL,
   name VARCHAR(255) COMMENT 'name'
) COMMENT = 'storehouses';

DROP TABLE IF EXISTS storehouses_products;
CREATE TABLE storehouses_products (
   id INT UNSIGNED NOT NULL,
   storehouse_id INT UNSIGNED,
   product_id INT UNSIGNED,
   value INT UNSIGNED COMMENT 'value products'
) COMMENT = 'value products on storehouses';
```
### КАЛЕНДАРНЫЕ ТИПЫ ДАННЫХ И МНОЖЕСТВА
- значение NULL
- календарные типы
- ENUM
- SET
- JSON тип
- изменение структуры таблицы при помощи ALTER TABLE
```
 mysql> SELECT NULL;
```
--> NULL , Все операции с NULL возвращают NULL
```
mysql> SELECT NULL + 2
```
--> NULL
```
mysql> CREATE TABLE tbl (id INT UNSIGNED);
mysql> INSERT INTO tbl VALUES();
```
вставляем новую строку, но не  будем задавать ни одного значения

### ПРЕОБРАЗУЕМ С ПОМОЩЬЮ ALTER TABLE
```
mysql> ALTER TABLE tbl CHANGE id id INT UNSIGNED NOT NULL;
```
- `ALTER TABLE` - ключевое слово (команда)
- `tbl` - назвние таблицы
- `CHANGE` - ключевое слово (изменить)
- `id` - столбец который изменяем
- `id INT UNSIGNED NOT NULL` - указываем новые значения столбца
```
mysql> TRUNCATE tbl;
```
Очистить таблицу
```
mysql> DESCRIBE tbl\G
```
Посмотреть структуру таблицы

### КАЛЕНДАРНЫЕ ТИПЫ
- `TIME` (хранение времени в течении суток)
- `YEAR` (хронит год)
- `DATE` (хронит дату с точностью до дня)
- `DATETIME` (хронит дату и время)
- `TIMESTAMP` (хронит дату и время занимает меньше места
  
Хронит даты от 1970 до 2038 года. первый столбец этой таблицы обнавляется автоматически при операции создания и обнавления)

### Формат календарных типов
- `YEAR` 0000
- `DATE` '0000-00-00'
- `TIME` '00:00:00'
- `TIMESTAMP` '0000-00-00 00:00:00'
- `DATETIME` '0000-00-00 00:00:00'

```
mysql> SELECT '2021-09-09 00:00:00'
mysql> SELECT '2021-09-09 00:00:00' - INTERVAL 1 DAY
```

Можем вычитать, складывать
```
mysql> SELECT '2021-09-09 00:00:00' + INTERVAL 1 WEEK
mysql> SELECT '2021-09-09 00:00:00' + INTERVAL '1-1' YEAR_MONTH
```
Интервалы могут быть комбинированными

### ENUM и SET
Их допустимые значения задаются списком строк внутри БД, элементы множеств хронятся в виде чисел
- `ENUM` - поле может получить всего одно значение из списка
- `SET` - может применять комбинацию заданных значений

### JSON формат столбца
Добавим столбец при помощи ALTER TABLE
```
mysql> ALTER TABLE tbl ADD collect JSON;
```
посмотрим структуру таблицы
```
mysql> DESCRIBE tbl;
```
вставим новую запись из JSON объекта
```
mysql> INSERT INTO tbl VALUES (1, '{"first": "Hello", "second": "World"}');
```
в столбце id добавится 1., в столбец collect '{"first": "Hello", "second": "World"}' обращаться к полям JSON извлекая значение ключей
```
mysql> SELECT collect->>"$.first" FROM tbl;
```
Поправим БД нашего магазина, используя вышеизложенное: первичные ключи снабдим атрибутом `NOT NULL`, добавим в таблицу пользователей столбец день рожденья
```
DROP TABLE IF EXISTS users;
CREATE TABLE users (
   id INT UNSIGNED NOT NULL,
   name VARCHAR(255) COMMENT 'name buyer',
   birthday_at DATE COMMENT 'user birhtday'
-> created_at DATETIME COMMENT 'date of registration'
) COMMENT = 'buyers';
```
Добавим дату и время создания записи время регистрации.
```
DROP TABLE IF EXISTS users;
CREATE TABLE users (
   id INT UNSIGNED NOT NULL,
   name VARCHAR(255) COMMENT 'name buyer',
   birthday_at DATE COMMENT 'user birhtday'
-> created_at DATETIME COMMENT 'date of registration'
) COMMENT = 'buyers';
```
Добавим дату и время последгнего обновления записи пользователя чтобы автоматически дата обнавлялась `DEFAULT CURRENT_TIMESTAMP` если этим полям не присваивать значение, автоматически присвоится текущее значение даты и времени
```
DROP TABLE IF EXISTS users;
CREATE TABLE users (
   id INT UNSIGNED NOT NULL,
   name VARCHAR(255) COMMENT 'name buyer',
   birthday_at DATE COMMENT 'user birhtday',
   created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'date of registration',
   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT ON UPDATE CURRENT_TIMESTAMP 'date of update'
) COMMENT = 'buyers';
```
Чтобы поле `updated_at` обнавлялось автоматически при операции вставки и обнавлении записи `ON UPDATE CURRENT_TIMESTAMP`
```
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT ON UPDATE CURRENT_TIMESTAMP 'date of updqte'
```
Добавим в таблицу данные
```
>>> INSERT INTO users (id, name, birthday_at) VALUES (1, 'hello', '1979-01-27');
>>> SELECT * FROM users;
```
Внесём аналогичные изменения в таблицу products, orders, orders_product. В таблицу discounts добавим 4 календарных поля
- started_ad - начало действия скидки
- finish_ad - конец действия скидки
- добавляем в 2 оставшиеся таблицы
- created_at и updated_at

Итоговый скрипт:
```
DROP TABLE IF EXISTS catalogs;
CREATE TABLE catalogs (
    id INT UNSIGNED NOT NULL,
    name VARCHAR(255) COMMENT 'name BD categories'
) COMMENT = 'categories internet shop';

DROP TABLE IF EXISTS users;
CREATE TABLE users (
   id INT UNSIGNED NOT NULL,
   name VARCHAR(255) COMMENT 'name buyer',
   birthday_at DATE COMMENT 'user birhtday',
   created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'date of registration',
   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'buyers';

DROP TABLE IF EXISTS products;
CREATE TABLE products (
   id INT UNSIGNED NOT NULL,
   name VARCHAR(255) COMMENT 'name',
   discription TEXT COMMENT 'discription',
   price DECIMAL (11,2) COMMENT 'price' ,
   catalog_id INT unsigned,
   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'Positions';

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
   id INT UNSIGNED NOT NULL,
   user_id INT UNSIGNED,
   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'orders';

DROP TABLE IF EXISTS orders_products;
CREATE TABLE orders_products (
   id INT UNSIGNED NOT NULL,
   order_id INT UNSIGNED,
   product_id INT UNSIGNED,
   total INT UNSIGNED DEFAULT 1 COMMENT 'all orders',
   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'value orders';

DROP TABLE IF EXISTS discounts;
CREATE TABLE discounts (
   id INT UNSIGNED NOT NULL,
   user_id INT UNSIGNED,
   product_id INT UNSIGNED,
   discount FLOAT UNSIGNED COMMENT 'discount 0.0 - 1.0',
   started_at DATETIME,
   finished_at DATETIME,
   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'discounts';

DROP TABLE IF EXISTS storehouses;
CREATE TABLE storehouses (
   id INT UNSIGNED NOT NULL,
   name VARCHAR(255) COMMENT 'name',
   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'storehouses';

DROP TABLE IF EXISTS storehouses_products;
CREATE TABLE storehouses_products (
   id INT UNSIGNED NOT NULL PRIMARY KEY,
   storehouse_id INT UNSIGNED,
   product_id INT UNSIGNED,
   value INT UNSIGNED COMMENT 'value products',
   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'value products on storehouses';
```
# ИНДЕКСЫ
- индексы
- устройство индекса
- типы индексов
- атрибут AUTO_INCREMENT
- управление индексами

Ключи - столбцы при помощи которых мы добиваемся уникальности записей и связываем записи в разных таблицах ключи могут снабжаться ИНДЕКСАМИ. ИНДЕКСИРОВАТЬ можно любой столбец

Идея индексов - создать копию стлбца которая постоянно будет поддерживаться в отсортированном состоянии

Индексы:
- обычные
- уникальные (первичный ключ)
- полнотекстовый

В таблице может быть только один первичный ключ, первичный ключ таблицы помечается специальным ключевым словом значение должно быть уникальным и не повторяться в пределах таблицы столбцы помеченные `pramiery key` не могут принимать значение `NULL`
```
DROP TABLE IF EXISTS catalogs;
CREATE TABLE catalogs (
    id INT UNSIGNED NOT NULL PRIMARY KEY,
    name VARCHAR(255) COMMENT 'name BD categories'
) COMMENT = 'categories internet shop';
```
Посмотрим в консоле на описание таблицы
```
mysql> DESCRIBE catalogs;
```
Альтернативный способ объявления первичного ключа. выбрали БД.
```
mysql> PRIMARY KEY(id)
```
В скбках название столбца к которому применяем `(id)` ключвое слово `PRIMARY KEY` может встречаться в таблице только 1 раз т.к в таблице разрешён только один первичный ключ
```
mysql> PRIMARY KEY(id, name(10))
```
Допустимо объявление индека не по одному столбцу по двум и более, первичный ключ создаётся по столбцу id и по первым 10 символам столбца name(10) как правило для индекса достаточно первых индексов строки

`AUTO_INCREMENT` - автоматическое создание уникального номера
```
mysql> id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT;
mysql> SELECT * FROM catalogs;
```
Убедимся что таблица пустая, вставим несколько строк
```
mysql> INSERT INTO catalogs (name) VALUES ('Процессоры');
```
Не указываем поле id - оно должно сформироваться автоматически, значение поле id - 1
```
mysql> INSERT INTO catalogs (name) VALUES ('Видеокарты');
```
Поле ай ди сформировалось автоматически . значение поля id 2 В `INSERT` запросе специально не указали id, чтобы оно получило значение `NULL`

Псевдоним `SERIAL`
```
SERIAL == BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE
```
Это позволяет более компактно записывать
```
id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT;
```
равнозначно
```
mysql> id SERIAL PRIMARY KEY;
```
Таблица может содержать несколько обычных и уникальных индексов для того чтобы их различать индексы могут иметь собственные имена часто имена индексов совпадают с именами столбцов, которые они индексируют. Для индекса можно назначить совершенно другое имя.

Объявление индекса происходит с помощью ключевого слова `INDEX` или `KEY` для уникальных индексов доп. ключевое слово `UNIQUE`

В таблице ptoducts снабдим индексом поле catalog_id
```
DROP TABLE IF EXISTS products;
CREATE TABLE products (
   id SERIAL PRIMARY KEY,
   name VARCHAR(255) COMMENT 'name',
   discription TEXT COMMENT 'discription',
   price DECIMAL (11,2) COMMENT 'price' ,
   catalog_id INT unsigned,
   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
-> KEY index_of_catalog_id(catalog_id)
) COMMENT = 'Positions';
```
посмотрим через консоль
```
#   mysql> DESCRIBE products;
```
-->
```
+-------------+-----------------+------+-----+-------------------+--------------
---------------------------------+
| Field       | Type            | Null | Key | Default           | Extra
                                 |
+-------------+-----------------+------+-----+-------------------+--------------
---------------------------------+
| id          | bigint unsigned | NO   | PRI | NULL              | auto_incremen
t                                |
| name        | varchar(255)    | YES  |     | NULL              |
                                 |
| discription | text            | YES  |     | NULL              |
                                 |
| price       | decimal(11,2)   | YES  |     | NULL              |
                                 |
| catalog_id  | int unsigned    | YES  | MUL | NULL              |
                                 |
| created_at  | datetime        | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENER
ATED                             |
| updated_at  | datetime        | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENER
ATED on update CURRENT_TIMESTAMP |
+-------------+-----------------+------+-----+-------------------+--------------
---------------------------------+
7 rows in set (0.01 sec)
```
Создать индекс в уже существующей таблице можно с помощью оператора `CREATE INDEX`

```
mysql> CREATE INDEX index_of_catalog_id ON products (catalog_id);
```
удалить индекс из таблицы
```
mysql> DROP INDEX index_of_catalog_id ON products;
```
### Индексы BTREE и ХЭШиндексы
Мы можем явно указывать тип индекса `USING BTREE`
```
mysql> CREATE INDEX index_of_catalog_id USING BTREE ON products (catalog_id);
```
указываем явно чтобы индекс был построен как бинарное дерево в качестве альтернативы можем использовать `HASH`
```
mysql> CREATE INDEX index_of_catalog_id USING HASH ON products (catalog_id);
```
Полезен для точного поиска с указанием всех столбцов индекса в индоксе хронятся хэштеги и указатели на соответствующие строки

отрефакторим таблицу products;

### ЗАПРОСЫ НА ПОИСК ИНФО
```
mysql> SELECT * FROM tbl WHERE year = 1990
mysql> SELECT * FROM tbl WHERE year = 1990 AND last_name = Борисов
```
ДОБАВЛЯЕМ ИНДЕКСЫ ТОЛЬКО В ТОМ СЛУЧАЕ КОГДА ЭТО НЕОБХОДИМО

# CRUD ОПЕРАЦИИ
- Введение в CRUD-операции
- Вставка данных
- Извлечение данных
- Обновление данных
- удадение данных
- Команда INSERT ... SELECT

4 базовые операции: создания, чтения, обновления и удаления
1) Crete - INSERT
2) Read - SELECT
3) Update - UPDATE
4) Delete - DELETE

# CRUD

### Вставка. Оператор INSERT
Одиночная вставка
```
mysql> INSERT INTO catalogs VALUES (NULL, 'Процессоры');
mysql> INSERT INTO catalogs VALUES (NULL, 'Мат.платы');
mysql> INSERT INTO catalogs VALUES (NULL, 'Видеокарты');
```
Многострочная вставка
```
mysql> INSERT INTO catalogs VALUES
      (NULL, 'процессоры'),
      (NULL, 'Мат.платы'),
      (NULL, 'Видеокарты');
```
Вставим в нашу таблицу catalogs записи
```
DROP TABLE IF EXISTS catalogs;
CREATE TABLE catalogs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) COMMENT 'name BD categories'
) COMMENT = 'categories internet shop';

INSERT INTO catalogs VALUES (NULL, 'Processors');
```
Мы вставляем в таблицу первую запись полю id мы присваиваем неопредлённое значение NULL, Полю name присваиваем значение 'Processors'

Мы можем явно указывать список столбцов, которые мы вставяем
```
mysql> INSERT INTO catalogs (id, name) VALUES (NULL, 'Motherboards');
```
можем поменять местами столбцы, такая запись тоже допустима
```
mysql> INSERT INTO catalogs (name, id) VALUES ('Motherboards', NULL);
```
также вместо ключевого слова `NULL` можем использовать ключевое слово `DEFAULT`
```
mysql> INSERT INTO catalogs VALUES (DEFAULT, 'Videocards');
```
Множество `INSERT` запросов можно заменить многострочниым вариантом запроса
```
mysql> INSERT INTO catalogs VALUES
     (DEFAULT, 'Processors'),
     (DEFAULT, 'Motherboards'),
     (DEFAULT, 'Videocards');
```
Для извлечения данных используется оператор SELECT
```
mysql> SELECT id, name FROM catalogs;
```
После ключевого оператора `SELECT` указываем список столбцов id, name ключевое слово `FROM` указываем откуда извлекаем из какой таблицы catalogs, порядок столбцов после ключевого слова можно изменять тем самым будем менять порядок столбцов в результиующей таблице
```
mysql> SELECT name, id FROM catalogs;
```
можем выводить только часть столбцов
```
mysql> SELECT name FROM catalogs;
```
часто столбцы заменяются символом `*` в этом случае выводятся все столбцы, в порядке в котором они определены в `CREATE TABLE`
```
mysql> SELECT * FROM catalogs;
```
### вставка при помощи `INSERT`
добавим уникальный индекс на столбец name таблицы catalogs; тем самым мы запретим вставку разделов, которые уже вставлены в таблицу для того чтобы не раздувать индекс, проиндексируем только первые 10 символов `UNIQUE unigue_name(name(10))`

```
DROP TABLE IF EXISTS catalogs;
CREATE TABLE catalogs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) COMMENT 'name BD categories',
    UNIQUE unigue_name(name(10))
) COMMENT = 'categories internet shop';
```
в случае вставки уже имеющихся значений, получим сообщение об ошибке

Уникальный ключ не допускает нарушения целостности БД избежать такого поведения можно с помощью ключевого слова `IGNORE`
```
mysql> INSERT IGNORE INTO catalogs VALUES (NULL, 'Processors');
```
попытка вставить существующее значение просто блокируется

# Удаление данных
```
mysql> DELETE FROM catalogs;
```
удаляет все или часть записай из таблицы

очистка таблицы
```
mysql> TRUNCATE catalogs;
```
удаляет все записи и обнуляет счётчики `AUTOINCREMANT`

Можем удалять часть данных
```
mysql> DELETE FROM catalogs LIMIT 2;
```
мы удалм только 2 записи. Перые 2 записи таблицы удалятся

Удалять только те записи первичный ключ ай ди которых больше 1
```
mysql> DELETE FROM catalogs WHERE id > 1 LIMIT 1;
```
При использовании операции `DELETE` счётчик и автоинкремент не затрагивается

вставим данные, удалим и снова вставим, чтобы посмотреть как работаетсчётчик автоинкремент
```
mysql> INSERT INTO catalogs VALUES
     (DEFAULT, 'Processors'),
     (DEFAULT, 'Motherboards'),
     (DEFAULT, 'Videocards');
mysql> DELETE FROM catalogs;
mysql> INSERT INTO catalogs VALUES
     (DEFAULT, 'Processors'),
     (DEFAULT, 'Motherboards'),
     (DEFAULT, 'Videocards');
```
столбец id  с натсройками:
id SERIAL PRIMARY KEY, во второй вставке имеет id 4,5,6

сброс счётчиков
```
mysql> TRINCATE catalogs;
```
очищает таблицу, обнуляет счётчики

команда `UPDATE` позволяет редактировать данные
```
UPDATE
  catalogs
SET
  name = 'Processors (Intel)'
WHERE
  name = 'Processors';
```
Если убрать ограничение `WHERE` произошла бы попытка замены всех записей таблицы, а если поле проиндексировано уникальным ключом произойдёт ошибка

Специалиный оператор `INSERT SELECT` позволяет вставлять записи из одной таблицы в другую в том числе осуществляя преобразоваие над данными если таблицы имеют идентичные столбцы перемещаем все данные изтаблицы catalog в таблицу cat
```
 INSERT INTO
      cat
  SELECT
      *
  FROM
      catalogs;
```
 КОД И КОМАНДЫ:
```
- >>> mysql -u root -p | запускаем сервер скюль
- mysql> SELECT 'Hello Databases'; | выбираем базу данных
- >>> mysql -u root -h 192.168.0.10 -P 3306 -p | Если сервер установлен на удалённом хосте, соединяемся указав ай пи адрес или домен удалёного сервера в параметре ейч (h) в параметре P мы можем указать порт
- USE       \u           выбор БД
- SOURCE    \.           Выполнение sql-команд из файла
- SYSTEM    \!           Выполнение команды ОС
- STATUS    \s           Вывод информации о состоянии сервера
- EXIT      \q           Выход
-           \G           Вывод результата в вертикальном формате
- mysql> SELECT * FROM mysql.user LIMIT 1\G - вертикальный вывод длинной таблицы. Построчно.
- mysql> STATUS | посмотреть статус сервера
- mysql> \s | посмотреть статус сервера
- mysql> SYSTEM ls | системные команды из mysql
- mysql> SOURCE hello.sql | запуск sql скрипта
- mysql> \. hello.sql | запуск sql скрипта
- mysql> mysqldump mysql > mysql.sql |  дамп системной базы mysql
- >>> tail -10 mysql.sql | прочитать последние 10 строчек файла
- mysql> mysql mysql < hello.sql |  развернуть дамп базы данных
- mysql> CREATE DATABASE crypto; |  создать базу данных (создаётся база данных crypto)
- mysql> SHOW DATABASES; | Посмотреть существующие БД
- mysql> SHOW VARIABLES LIKE 'datadir'; | Узнаем где расположен каталог данных
- mysql> exit |  выход из sql 
- mysql> \q |  выход из sql
- >>> cp -r crypto foo | рекурсивное копирование из директории crypto в директорию foo
- mysql> DROP DATABASE crypto; | удаление базы данных
- mysql> CREATE DATABASE IF NOT EXISTS crypto; |  создание базы данных на проверку имени, Если бд с таким именем уже существует ничего не произойдёт
- mysql> DROP DATABASE IF EXIST crypto;  | Если база данных есть она удалится, если бд нет - ничего не произойдёт
- mysql> SHOW TABLES; | список текущих таблиц
- mysql> USE crypto |  выбрать базу данных crypto
- mysql> SHOW TABLES FROM mysql;  | Если не выбирать БД. то в каждом операторе надо явно указывать какая БД будет использоваться
- mysql> SHOW TABLES FROM crypto; | Если не выбирать БД. то в каждом операторе надо явно указывать какая БД будет использоваться
- mysql> SELECT mysql.user.user, mysql.user.Host FROM mysql.User; | В операторе select мы явно указываем имя БД mysql. Имя таблицы user. и имя столбцов user Host и в ключевой команде FROM указываем имя БД и таблицы FROM mysql.user;
- >>> mysql -u root -p crypto; | выбор базы данных при входе
- >>> CREATE TABLE имя_таблицы (
      имя_столбца параметры,
      имя_столбца параметры,
     ...
       )    | Создание таблицы внутри базы данных
- >>> CREATE TABLE users (k INT); | Создание таблицы `users` с колонокой `К` и значение этой колонки `INT`
- >>> CREATE TABLE IF NOT EXIST users(k INT); | Если такой таблицы нет то она создастся, иначе ничего не произойдёт
- >>> DESCRIBE users; | Просмотр структуры таблицы
- >>> DESCRIBE user 'User'; | Оператор Describe может принимать доп. параметр - имя столбца
- >>> DESCRIBE user 'm%'; | лайтшаблоны вместе с оператором DESCRIBE заменять с помощью символа процента % любое количество символов, а символом _ один символ. Запросим с таблице юзер все столбцы, которе начинаются с символа m
- >>> SELECT * FROM information_schema.SCHEMATA; | Запросим весь список баз данных из information_schema
- >>> SELECT * FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'crypto'; | выбираем таблицу 'crypto' из списка таблиц базы information_schema.TABLES
- >>> SELECT * FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'crypto'\G; | вывод результата предыдущего запроса в строковом виде
- mysql> HELP DESCRIBE; | откроет помощь прямо в коноле
- mysql> SELECT id, name FROM users WHERE name='Игорь' | выбрать столбцы id, name из таблицы users, где в столбце name содержится значение 'Игорь'
- mysql> SELECT 'Hello db\'s' | когда ковычки внутри ковычек интерпритатор запутается надо экранировать символ ковычек при помощи слэша
- mysql> SELECT "Hello db's" | также можем воспользовться двойными ковычками
- mysql> CREATE TABLE tbl (`create` INT) | Имена БД , таблиц, столбцов строк могут содержать разные символы кроме |\./ если имя совпадает с ключевым словом его заключают в обратные ковычки `
- mysql> CREATE TABLE tbl (id INT(8));  |  создаём таблицу tbl с одним столбцом id значение которого INT в котором 8 символов
- mysql> INSERT INTO tbl VALUES (5); | поместим в таблицу число 5
- mysql> CREATE TABLE tbl (id INT(3) ZEROFILL); | Создадим таблицу, где столбец id будет содержать числовое значение INT, столбец будет занимать 3 символа INT(3), ZEROFILL вместо пробелов отображать нули
- mysql> INSERT INTO tbl VALUES (1000); | можем указывать количество символов после INT
- mysql> CREATE TABLE tbldec (price DECIMAL(7,4));
- mysql> INSERT INTO tbldec VALUES (111.2);
- mysql> SELECT * FROM tbldec;
- mysql> ALTER TABLE tbl CHANGE id id INT UNSIGNED NOT NULL; | ALTER TABLE - ключевое слово (команда), tbl - назвние таблицы, CHANGE ключевое слово (изменить), id - столбец который изменяем, id INT UNSIGNED NOT NULL - указываем новые значения столбца
- mysql> TRUNCATE tbl; | Очистить таблицу
- mysql> DESCRIBE tbl\G | Посмотреть структуру таблицы в строковом виде
- mysql> SELECT '2021-09-09 00:00:00' |  Работа с датами
- mysql> SELECT '2021-09-09 00:00:00' - INTERVAL 1 DAY | Можем вычитать, складывать
- mysql> SELECT '2021-09-09 00:00:00' + INTERVAL 1 WEEK | Можем вычитать, складывать
- mysql> SELECT '2021-09-09 00:00:00' + INTERVAL '1-1' YEAR_MONTH | Интервалы могут быть комбинироваными,
- mysql> ALTER TABLE tbl ADD collect JSON; |  Добавим JSON столбец при помощи ALTER TABLE
- mysql> INSERT INTO tbl VALUES (1, '{"first": "Hello", "second": "World"}'); |  вставим новую запись из JSON объекта
- mysql> SELECT collect->>"$.first" FROM tbl; |
- mysql> PRIMARY KEY(id) | Альтернативный способ объявления первичного ключа. выбрали БД. В скбках название столбца к которому применяем (id)
- mysql> PRIMARY KEY(id, name(10))  | Допустимо объявление индека не по одному столбцу по двум и более, первичный ключ создаётся по столбцу id и по первым 10 символам столбца name(10) как правило для индекса достаточно первых индексов строки
- mysql> id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT;  |  AUTO_INCREMENT - автоматическое создание уникального номера
- mysql> INSERT INTO catalogs (name) VALUES ('Процессоры'); | Вставляем значения в таблицу catalogs
- mysql> INSERT INTO catalogs (name) VALUES ('Видеокарты'); | Вставляем значения в таблицу catalogs
- mysql> CREATE INDEX index_of_catalog_id ON products (catalog_id);  | Создать индекс в уже существующей таблице можно с помощью оператора CREATE INDEX
- mysql> DROP INDEX index_of_catalog_id ON products;  |  удалить индекс из таблицы
- mysql> CREATE INDEX index_of_catalog_id USING BTREE ON products (catalog_id);  | Мы можем явно указывать тип индекса USING BTREE
- mysql> CREATE INDEX index_of_catalog_id USING HASH ON products (catalog_id); | указываем явно чтобы индекс был построен как бинарное дерево в качестве альтернативы можем использовать HASH
- mysql> SELECT * FROM tbl WHERE year = 1990 | запросы на поиск информации 
- mysql> SELECT * FROM tbl WHERE year = 1990 AND last_name = Борисов | запросы на поиск информации
- mysql> INSERT INTO catalogs VALUES (NULL, 'Процессоры'); | одиночная вставка. Вставляем значения в таблицу catalogs
- mysql> INSERT INTO catalogs VALUES (NULL, 'Мат.платы'); | одиночная вставка. Вставляем значения в таблицу catalogs
- mysql> INSERT INTO catalogs VALUES (NULL, 'Видеокарты'); | одиночная вставка. Вставляем значения в таблицу catalogs
- mysql> INSERT INTO catalogs VALUES
      (NULL, 'процессоры'),
      (NULL, 'Мат.платы'),
      (NULL, 'Видеокарты');  | Многострочная вставка\
- mysql> INSERT INTO catalogs (id, name) VALUES (NULL, 'Motherboards');  | Мы можем явно указывать список столбцов, которые мы вставяем
- mysql> INSERT INTO catalogs (name, id) VALUES ('Motherboards', NULL);  | можем поменять местами столбцы, такая запись тоже допустима
- mysql> INSERT INTO catalogs VALUES (DEFAULT, 'Videocards');  | также вместо ключевого слова NULL можем использовать ключевое слово DEFAULT
- mysql> INSERT INTO catalogs VALUES
     (DEFAULT, 'Processors'),
     (DEFAULT, 'Motherboards'),
     (DEFAULT, 'Videocards');  | Множество INSERT запросов можно заменить многострочниым вариантом запроса
- mysql> DELETE FROM catalogs;  | удаляет все или часть записай из таблицы
- mysql> TRUNCATE catalogs;  | удаляет все записи и обнуляет счётчики AUTOINCREMANT
- mysql> DELETE FROM catalogs LIMIT 2; | мы удалм только 2 записи. Перые 2 записи таблицы удалятся
- mysql> DELETE FROM catalogs WHERE id > 1 LIMIT 1;  | Удалять только те записи первичный ключ ай ди которых больше 1
```
SQL ЗАПРОСЫ
```
--. -- |  Однострочный комментарий
/* многострочный комментарий */

>>> DROP TABLE IF EXISTS tbl;
    CREATE TABLE tbl (
    name CHAR(10) DEFAULT 'anonimus',
    description VARCHAR(255)
  );

Удаляем таблицу tbl, если она существует , создаём таблицу tbl с 1-ым столбцом `name` значение которого текстовое `CHAR`, длина колонки `10 символов`, Если поле не заполнено, автоматически заполняется 'anonimus', и 2-ой столбец `description` с типом данных VARCHAR и длинною 255

>>> INSERT INTO tbl VALUES (DEFAULT, 'Новый пользователь');
>>> INSERT INTO tbl VALUES ('Юрген', 'Новый пользователь');
>>> SELECT * FROM tbl;

вставляем 2 строки с данными (DEFAULT, 'Новый пользователь') и ('Юрген', 'Новый пользователь') и смотрим содержание таблицы

***
Итоговый готовый скрипт:

DROP TABLE IF EXISTS tbl;
CREATE TABLE tbl (
	name CHAR(10) DEFAULT 'anonimus',
	description VARCHAR(255)
);
INSERT INTO tbl VALUES (DEFAULT, 'New User');
INSERT INTO tbl VALUES ('Yurgen', 'User');
SELECT * FROM tbl;

***

Это всё каркас нашей учебной БД, скрипт выглядит целиком так:

DROP TABLE IF EXISTS catalogs;
CREATE TABLE catalogs (
    id INT UNSIGNED NOT NULL,
    name VARCHAR(255) COMMENT 'name BD categories'
) COMMENT = 'categories internet shop';

DROP TABLE IF EXISTS users;
CREATE TABLE users (
   id INT UNSIGNED NOT NULL,
   name VARCHAR(255) COMMENT 'name buyer',
   birthday_at DATE COMMENT 'user birhtday',
   created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'date of registration',
   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'buyers';

DROP TABLE IF EXISTS products;
CREATE TABLE products (
   id INT UNSIGNED NOT NULL,
   name VARCHAR(255) COMMENT 'name',
   discription TEXT COMMENT 'discription',
   price DECIMAL (11,2) COMMENT 'price' ,
   catalog_id INT unsigned,
   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'Positions';

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
   id INT UNSIGNED NOT NULL,
   user_id INT UNSIGNED,
   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'orders';

DROP TABLE IF EXISTS orders_products;
CREATE TABLE orders_products (
   id INT UNSIGNED NOT NULL,
   order_id INT UNSIGNED,
   product_id INT UNSIGNED,
   total INT UNSIGNED DEFAULT 1 COMMENT 'all orders',
   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'value orders';

DROP TABLE IF EXISTS discounts;
CREATE TABLE discounts (
   id INT UNSIGNED NOT NULL,
   user_id INT UNSIGNED,
   product_id INT UNSIGNED,
   discount FLOAT UNSIGNED COMMENT 'discount 0.0 - 1.0',
   started_at DATETIME,
   finished_at DATETIME,
   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'discounts';

DROP TABLE IF EXISTS storehouses;
CREATE TABLE storehouses (
   id INT UNSIGNED NOT NULL,
   name VARCHAR(255) COMMENT 'name',
   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'storehouses';

DROP TABLE IF EXISTS storehouses_products;
CREATE TABLE storehouses_products (
   id INT UNSIGNED NOT NULL PRIMARY KEY,
   storehouse_id INT UNSIGNED,
   product_id INT UNSIGNED,
   value INT UNSIGNED COMMENT 'value products',
   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'value products on storehouses';

Создаём таблицы:
- catalogs --> [id, name]
- users --> [id, name, birthday_at, created_at, updated_at]
- products --> [id, name, discription, price, catalog_id, created_at, updated_at]
- orders --> [id, user_id, created_at, updated_at]
- orders_products --> [id, order_id, product_id, total, created_at, updated_at]
- discounts --> [id, order_id, product_id, discount, started_at, finished_at, created_at, updated_at]
- storehouses --> [id, name, created_at, updated_at]
- storehouses_products --> [id, nstorehouses_id, product_id, value, created_at, updated_at]

***

Индексы. Объявление первиного ключа. PRIMARY KEY

DROP TABLE IF EXISTS catalogs;
CREATE TABLE catalogs (
    id INT UNSIGNED NOT NULL PRIMARY KEY,
    name VARCHAR(255) COMMENT 'name BD categories'
) COMMENT = 'categories internet shop';

***

DROP TABLE IF EXISTS products;
CREATE TABLE products (
   id SERIAL PRIMARY KEY,
   name VARCHAR(255) COMMENT 'name',
   discription TEXT COMMENT 'discription',
   price DECIMAL (11,2) COMMENT 'price' ,
   catalog_id INT unsigned,
   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
-> KEY index_of_catalog_id(catalog_id)
) COMMENT = 'Positions';

В таблице ptoducts снабдим индексом поле catalog_id

***

DROP TABLE IF EXISTS catalogs;
CREATE TABLE catalogs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) COMMENT 'name BD categories'
) COMMENT = 'categories internet shop';

INSERT INTO catalogs VALUES (NULL, 'Processors');

Мы вставляем в таблицу первую запись полю id мы присваиваем неопредлённое значение NULL, Полю name присваиваем значение 'Processors'

***

DROP TABLE IF EXISTS catalogs;
CREATE TABLE catalogs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) COMMENT 'name BD categories',
    UNIQUE unigue_name(name(10))
) COMMENT = 'categories internet shop';

mysql> INSERT IGNORE INTO catalogs VALUES (NULL, 'Processors');

добавим уникальный индекс на столбец name таблицы catalogs; тем самым мы запретим вставку разделов, которые уже вставлены в таблицу для того чтобы не раздувать индекс, проиндексируем только первые 10 символов UNIQUE unigue_name(name(10)) в случае вставки уже имеющихся значений, получим сообщение об ошибке Уникальный ключ не допускает нарушения целостности БД избежать такого поведения можно с помощью ключевого слова 

***
UPDATE
  catalogs
SET
  name = 'Processors (Intel)'
WHERE
  name = 'Processors';

команда UPDATE позволяет редактировать данные


***

INSERT INTO
      cat
  SELECT
      *
  FROM
      catalogs;

Специалиный оператор INSERT SELECT позволяет вставлять записи из одной таблицы в другую в том числе осуществляя преобразоваие над данными если таблицы имеют идентичные столбцы перемещаем все данные изтаблицы catalog в таблицу cat


```
