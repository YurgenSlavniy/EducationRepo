# УРОК 3
# Введение в проектирование БД

Открыли Dbreaver, развернем рабочее окружение

### Тема: DDL = Data Detintion Language (Язык определения данных)

Команды:
- `CREATE` - создать ,
- `ALTER` - изменить ,
- `DROP` - удалить объект в базе

### Задача: спроектировать базу данных соцсети
определиться с табличками, столбцами, полями, типами данных


`Dbreaver:` Если он меняет регистр при ножатии ентер с верхнего на нижний:
- ВП -> Window (окна) -> preferensice (настройка) -> Frmating (форматирование)  |регистр ключевых слов - UPPER выбрать. по умолчанию default|

```
>>> DROP DATABASE IF EXISTS socialnet;
```
 - удаляем на случай если эта база уже есть. `IF EXISTS` - если база существует, если не существует ошибки не будет
```
>>> CREATE DATABASE socialnet;
```
 - создаём БД
 
```
>>> USE socialnet;
```
 - используем созданную БД. подключаймся к ней.

# Таблицы:
Начнём с пользователей. Эта таблица самостоятельная и центральная, в нашей бд хорошо иметь столбец - идентификатор каждого пользователя, это поле сделаем ключом. чтобы можно было к каждой строке обратиться по ай ди: 
- тип данных целочисленный `INT` 
- избегаем отрицательных значений `UNSIGNET`
- `NOT NULL` - запрещаем отсутствие значения в этом поле
- `AUTOINCREMENT` - присваивть уникальное значени ай ди (+1 к предыдущему значению)
- чтобы номера не повторялись и были уникальными - `PRIMARY KEY` первичный ключ создаёт кластиризованный индекс. Индекс важен для данных которые часто ищем. Индекс ускоряет чтение замедляет изменение данных. `колонка firstname(100)` 100 символов максимально
- `UNIQUE` ключ уникальности который создаёт индекс
- `UNSIGNET` - чтобы гне было отрицательных номеров телефонов
```
>>> DROP TABLE IF EXISTS users;#
>>> CREATE TABLE users(
      id INT UNSIGNET NOT NULL AUTO_INCREMENT PRIMARY KEY,
       firstname VARCHAR(100),
       lastname VARCHAR(100),
       email VARCHAR(100) UNIQUE,
       password VARCHAR(100),
       phone BIGINT UNSIGNET UNIQUE
       );
```

`ALT + X` исполняем код - БД и таблица создались
`Dbreaver:` ЛП -> обновить. появилась наша БД. можем видить структуру.

socialnet -> таблицы -> users  -> индексы

У нас три индекса есть: 
1) id, 
2) email, 
3) phone

т.к мы использовали `PRIMARY KEY UNIQUE UNIQUE` Можно добавлять метаданные коментарием к таблице.

- `COMMENT '...'` - сохраница в метаданных базы
```
phone BIGINT UNSIGNET UNIQUE COMMENT '.комментарий.'
```

 Можем индексировать какое нибудь поле или поля
```
INDEX(firstname, lastname)`
```
```
INDEX idx_first_name (firstname, lastname)
```
дали имя нашему индексу idx_first_name

```
   >>> DROP TABLE IF EXISTS users;#
   >>> CREATE TABLE users(
       id INT UNSIGNET NOT NULL AUTO_INCREMENT PRIMARY KEY,
       firstname VARCHAR(100),
       lastname VARCHAR(100),
       email VARCHAR(100) UNIQUE,
       password VARCHAR(100),
       phone BIGINT UNSIGNET UNIQUE

       INDEX(firstname, lastname)
       INDEX idx_first_name (firstname, lastname)
       );
```

###  Таблица информация о пользователях 

Теперь создадим отдельную таблицу куда выделим всю информацию о пользователях. Эта таблица будет соотноситься с нашеми юзерами отношением 1 Х 1 . Cоздадиммтаблицу ###profils### и должны указать поле которое строго совпадает с полем таблицы `users` - id.

`user_id` поле будет ссылаться на поле id
- `AUTO_INCREMENT` - исключим, чтобы сама не считала

Добавляем остальные поля
- `gender CHAR(1)` - пол,
- `hometown VARCHAR(100)` - город ,
- `create_date` - дата создания профиля. Хотим чтобы в это поле прописывалось текущее время на сервере - NOW()

```
create_date DATETIME DEFAULT NOW()
```
```
>>> DROP TABLE IF EXISTS profiles;
>>> CREATE TABLE profiles(
       user_id INT UNSIGNET NOT NULL PRIMARY KEY,
       gender CHAR(1),
       hometown VARCHAR(100),
       create_date DATETIME DEFAULT NOW()
   );
```

Внешние ключи. Ограничитель целостности данных в нашем случае чтобы user_id всегда ссылался на существующий id в таблице users

```
>>> ALTER TABLE profiles ADD CONSTRAINT fk_profile_user_id
>>> FOREIGN KEY (user_id) REFERENCES users(id)
```

### команда `ALTER TABLE (имя_таблицы)`

Нам нужно дабивить столбец в уже существующую таблицу
```
>>> ALTER TABLE profiles ADD COLUMN birthday DATETIME;
```
Решили изменить колонку
```
>>> ALTER TABLE profiles MODIFY COLUMN birthday DATE;
```
Решили переименовать колонку
```
>>> ALTER TABLE profiles RENAME COLUMN birthday TO bday DATE;
```
Решили удалить колонку
```
>>> ALTER TABLE profiles DROP COLUMN bday;
```

# Таблица сообщений
Только личные сообщения, 
- id - идентификатор каждой записи, 
- надо знать отправителя кто отправил ай ди, 
- ай ди получателя, 
- текст который написали - body
-  и дату - create_date

```
to_user_id INT UNSIGNET NOT NULL
```
У получателя и отправителя будут ссылаться на `user_id`.
Повторяем тип данных как в `user_id` столбце `from_user_id` и `to_user_id` должны бвть внешними ключами
```
FOREION KEY (from_user_id) REFERENCES users(id);
```
```
>>> DROP TABLE IF EXISTS messeges;
>>> CREATE TABLE messeges(
 	id SERIAL,
 	from_user_id INT UNSIGNET NOT NULL,
 	to_user_id INT UNSIGNET NOT NULL,
 	body TEXT,
   create_date DATETIME DEFAULT NOW()

   FOREION KEY (from_user_id) REFERENCES users(id);
   FOREION KEY (to_user_id) REFERENCES users(id);

 	);
```

# Следующая табличка про друзей

 `1 сценарий`: я пользователь соц сети и маша пользователь соц. сети я зашёл на страничку маши и отправил ей запрос в друзья. В этот момент в базу должны были уйти какие то данные, через неделю маша зашла в сеть, увидела мой запрос в друзья и всё это время мой запрос где то хронился в базе и нажала на кнопочку подтвердить. В этот момент информация о дружбе с машей должна как то обновиться
 
`2 сценарий`: Отправлен запрос васе. Вася через пару дней зашёл в соц. сеть и нажал отклонить значит информация об этом должна как то хронится

`3 сценарий`: с машей поссорились она нажала удалить из друзей информация о дружбе с машей должна храниться поновому.

Поля таблицы про друзей:
- кто отправил запрос - `init_user_id`
- кому отправил запрос - `target_user_id`

оба поля будут внешними ключами

```
FOREIGN KEY (initiator_user_id) REFERENCES users(id),
FOREIGN KEY (target_user_id) REFERENCES users(id)
```
- Должна быть дата создания записи - `create_at`
- дата обновления информации о дружбе - `update_at`
```
 ON UPDATE NOW() - информация присвоится при апдейте
```
- статус дружбы - status
Тип данных `ENUM` - перечисление в скобках указываем значения
```
status ENUM('requested', 'approved', 'deslined', 'unfriended')
```
Можем добавить  `PRIMARY KEY` первичный ключ будет контролировать уникальность пары инициатор-таргет. Чтобы в базе не было двух строк о том, что я отправлял запрос маше. Запрет на отправку запроса в друзья самому себе. проверка CHECK (init_user_id != target_user_id) инициатор не равен тагет. Для каждой записи при каждом обновлении это условие будет проверяться альтернативно добавить `CHECK ALTER TABLE friend_requests`
```
ADD CHECK (initiator_user_id <> target_user_id);
```
` <> это тоже что != - не рвно`

```
>>> DROP TABLE IF EXISTS friend_request;
>>> CREATE TABLE friend_requests(
       init_user_id INT UNSIGNED NOT NULL,
 	target_user_id INT UNSIGNED NOT NULL,
       create_at DATETIME DEFAULT NOW(),
       update_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
       status ENUM('requested', 'approved', 'deslined', 'unfriended'),

       PRIMARY KEY(init_user_id, target_user_id),
 	    FOREIGN KEY (initiator_user_id) REFERENCES users(id),
    	FOREIGN KEY (target_user_id) REFERENCES users(id),
    	CHECK (init_user_id != target_user_id)
   );
```
Табличка  сообщества в которые пользователи добавляются `admin_user_id` - ссылочка на админа этот админ должен будет быть внешним ключом, хорошо добавить индекс на поле name чтобы бысто можно было найти


```
 >>> DROP TABLE IF EXISTS community;
     CREATE TABLE community(
 	        id SERIAL,
 	        name VARCHAR(155),
 	        admin_user_id INT UNSIGNED NOT NULL,

 	        INDEX (name),
 	        FOREIGN KEY (admin_user_id) REFERENCES users(id)
 );
```
Как хронить информацию о том кто в какое сообщество добавился? реализация связи многи еко многим реализуется отдельной таблицей там будутт ссылки на айдишники предыдущих таблиц
```
>>>DROP TABLE IF EXISTS users_community;
      CREATE TABLE users_community(
        user_id INT UNSIGNED NOT NULL,
        community_id BIGINT UNSIGNED NOT NULL,

        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (community_id) REFERENCES community(id)
 );
```
Я добавился в 50 групп. В таблице 50 записей user_id мой, community_id - 50 разных, в группе 60 пользователей в таблице 60 записей user_id  60 разных community_id - одно и тоже

# Таблица контента который генерируют наши пользователи.
В эту таблицу сохроняем все новости все посты 
- `id`  - чтобы иметь номер нашей новости
- `user_id` - ссылка на пользователя который запостил
- `body` - текст новости
- `BLOB` - преобразует файл в байты и хронит в БД.
- `filename VARCHAR(255)` - хронит ссылку на файл на жёстком диске
- если есть файл у него есть метаданные - `metadata` используем JSON
- `created_at` - дата создания
- `updated_at` - дата обновления поста
- `type_media` - тип медиазаписи

```
>>>DROP TABLE IF EXISTS content;
      CREATE TABLE content(
           id SERIAL,
           user_id INT UNSIGNED NOT NULL,
           type_media ENUM('text', 'video', 'music', 'image')
           body VARCHAR(333),
           # file BLOB,
           filename VARCHAR(255),
           metadata JSON,
           created_at DATETIME DEFAULT NOW(),
           updated_at DATETIME CURRENT_TIMESTAMP,

           FOREIGN KEY (user_id) REFERENCES users(id),
      );
```

Альтернативный вариант реализации `type_media ENUM('text', 'video', 'music', 'image')` создадим отдельную таблицу справочник мдиатипов создадим выше нашей таблицы, чтбы создалась раньше `name` - в поле name будет 4 значения `('text', 'video', 'music', 'image')`
```
>>>DROP TABLE IF EXISTS media_type;
      CREATE TABLE contentmedia_type(
           id SERIAL,
           name VARCHAR(255)
      );
```

 Так как есть таблица медиатипов можем создать колонку в таблице `content` `media_type_id` которая будет ссылаться внешним ключом на айдишник медиатипов

```
>>>DROP TABLE IF EXISTS content;
      CREATE TABLE content(
          id SERIAL,
          user_id INT UNSIGNED NOT NULL,
          type_media ENUM('text', 'video', 'music', 'image'),
          # media_type_id BIGINT UNSIGNED NOT NULL,
          body VARCHAR(333),
          # file BLOB,
          filename VARCHAR(255),
          metadata JSON,
          created_at DATETIME DEFAULT NOW(),
          updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,

          FOREIGN KEY (user_id) REFERENCES users(id)
          FOREIGN KEY (media_type_id) REFERENCES content(id),
 );
```
# табличка лайков
- `user_id` - ссылка на пользователя, котрый поставил лайк
- `media_id` - ссылка на запись которую лайкнули

```
>>>DROP TABLE IF EXISTS likes;
      CREATE TABLE likes(
           id SERIAL,
           user_id INT UNSIGNED NOT NULL,
           # media_id BIGINT UNSIGNED NOT NULL,
           created_at DATETIME DEFAULT NOW(),

           FOREIGN KEY (user_id) REFERENCES users(id)
       );
```

В `DBeaver` если 2 раза щёлкнуть ЛКМ по БД откроются свойства и диаграмма таблицы на диаграмме видно как таблицы связаны между собой

`Домашнее задание` : добавить три своих таблицы
