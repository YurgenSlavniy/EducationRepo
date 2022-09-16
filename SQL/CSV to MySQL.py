# Как можно данные из CSV-файла загрузить в БД MySQL.

# Для сего это нужно? Разные бывают ситуации,
# иногда клиенты из экселя дают нам данные и просят их занести в БД,
# а как это сделать???? Не будем же мы подключать массивные скрипты
# для обработки этого файла
# и потом еще наступим на грабли с кодировкой…
# Есть пути куда проще.

# Имеется содержимое файла:

# "id";"login";"pass"
# "3";"superadmin";"da1c42eb9cec3336fa8e996832fcbc90"
# "4";"admin";"21232f297a57a5a743894a0e4a801fc3"
# "5";"Fabian_Admin";"60f8ffb1f0d1d30a3d4a5909452da58d"

# Первое что делаем, убираем первую строку — аля название поля в БД.
# Именно тут эта строка не влияет ни на что.
# Далее создаем таблицу в БД с соот полями:

#   1) CREATE TABLE `user` (
#   2) `id` INT(10) NOT NULL AUTO_INCREMENT,
#   3) `login` VARCHAR(200) NULL DEFAULT NULL COLLATE 'utf8_unicode_ci',
#   4) `pass` VARCHAR(200) NULL DEFAULT NULL COLLATE 'utf8_unicode_ci',
#   5) PRIMARY KEY (`id`)
#   6) )
#   7) COLLATE='utf8_unicode_ci'
#   8) ENGINE=MyISAM
#   9) ROW_FORMAT=DEFAULT

# Теперь просто используя запрос:
#   1) LOAD DATA INFILE 'd:\\user.csv'
#   2) INTO TABLE `user`
#   3) FIELDS TERMINATED BY ';' ENCLOSED BY '"' ESCAPED BY '\\'
#   4) LINES STARTING BY '' TERMINATED BY '\r\n';

# - Конструкция LOAD DATA INFILE ‘d:\\user.csv’ говорит о том,
# помещен файл с данными по указанному пути, путь абсолютный.
# - Конструкция FIELDS TERMINATED BY ‘;’ ENCLOSED BY ‘»‘ ESCAPED BY ‘\r\n’
# говорит о том, что каждое поля в файле будут разделены знаком ;,
# также что каждое поле будет обернуто в знак «, если внутри поле будет соот знак,
# то БД позаботится об экранирования (ESCAPED BY)
# таких знаков (правила построения CSV файлов).
# - Конструкция LINES STARTING BY » TERMINATED BY ‘\r\n’
# говорит о том, что каждая строка начинается с указаного занчения
# в LINES STARTING BY, а заканчивается строка значением в TERMINATED BY,
# в данном примере, я ничего не присваиваю началу строки,
# просто написал чтобы был виден общий синтаксис.
# Т.к. я юзаю Windows, которому в качестве переноса строки необходимо указать \r\n,
# поэтому я это значение и поставил в TERMINATED BY,
# если Вы юзаете *nix подобные системы,
# то там значение конца строки \n

# В итоге выполнения запроса в таблицы БД будет следующее:
#   mysql> select * from user;
# +----+--------------+----------------------------------+
# | id | login        | pass                             |
# +----+--------------+----------------------------------+
# |  3 | superadmin   | da1c42eb9cec3336fa8e996832fcbc90 |
# |  4 | admin        | 21232f297a57a5a743894a0e4a801fc3 |
# |  5 | Fabian_Admin | 60f8ffb1f0d1d30a3d4a5909452da58d |
# +----+--------------+----------------------------------+
# 3 rows in set (0.00 sec)

# Я допустил неточность, сказав что из CSV файла
# необходимо вручную убрать первую строчку.
# Её можно убрать с помощью запроса.
# Строка IGNORE num LINES,
# гду num это кол-во строк которые надо пропустить.

# Вот полный запрос:
#   1) LOAD DATA INFILE 'd:\\user.csv'
#   2) INTO TABLE `user`
#   3) FIELDS TERMINATED BY ';' ENCLOSED BY '"' ESCAPED BY '\\'
#   4) LINES STARTING BY '' TERMINATED BY '\r\n'
#   5) IGNORE 1 LINES;

#  ***************************************************************

# Не забудьте изменить "\" на "/" при вводе адреса файла источника данных.

# LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/trade-history-2021-11-07.csv"
# INTO TABLE my_trade_history
# COLUMNS TERMINATED BY ','
# OPTIONALLY ENCLOSED BY '"'
# ESCAPED BY '"'
# LINES TERMINATED BY '\n'
# IGNORE 1 LINES;

#  ***************************************************************

# Была проблема:
# the mysql server is running with the --secure-file-priv option so it cannot execute this statement
# решалась проблема следующим образом:
# файл .csv поместил в папку,
# путь к которой нашёл с помощью команд
# он работает по назначению.
# Ваш сервер MySQL был запущен с --secure-file-priv опция,
# которая в основном ограничивает,
# из каких каталогов вы можете загружать файлы
# с помощью LOAD DATA INFILE.

# вы можете использовать SHOW VARIABLES LIKE "secure_file_priv";
# чтобы увидеть каталог, который был настроен.

# у вас есть два варианта:

# 1) переместить файл в каталог, указанный secure-file-priv.
# 2) отключить secure-file-priv. Это должно быть удалено из запуска
# и не может быть изменено динамически.
# Для этого проверьте параметры запуска MySQL
# (в зависимости от платформы) и my.ini

#   mysql> SHOW VARIABLES LIKE "secure_file_priv";

#   Variable_name	Value
# secure_file_priv	C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\
# также я заменил
# изменить "\" на "/" при вводе адреса файла#
