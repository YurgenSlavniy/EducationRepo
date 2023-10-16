# Добавление пути mysql в системную переменную Path

Добавить путь к исполняемым программам mysql в переменную кружения `Path` на `windows` после установки mysql

Для проверки подключения к консольным клиентам откром приложение командной строки (могу попробывать через `GIT BASH`), через `mysql commandline`
```
>>> mysql -u root -p
```
Если получаем ошибку нам надо указать путь к этой команде в системную переменную окружения `Path`. Скопируем в буфер обмена необходимый путь `C:\Program Files\MySQL\MySQL Server 8.0\bin` исполняемые файлы лежат в папке `bin` `ПКМ по адресной строке -> копировать адрес как текст`

Заходим в контрольную панель `Панель управления\Все элементы панели управления\Система -> дополнительные параметры системы -> кнопка Переменные среды в нижнем окне - системные переменные` находим переменную `Path`
```
C:\Program Files (x86)\Intel\iCLS Client\;
C:\Program Files\Intel\iCLS Client\;%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;
C:\Program Files\Intel\Intel(R) Management Engine Components\DAL;
C:\Program Files\Intel\Intel(R) Management Engine Components\IPT;
C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\IPT;
C:\Program Files (x86)\Intel\OpenCL SDK\2.0\bin\x86;
C:\Program Files (x86)\Intel\OpenCL SDK\2.0\bin\x64;
C:\Program Files\Intel\WiFi\bin\;
C:\Program Files\Common Files\Intel\WirelessCommon\;
C:\Program Files (x86)\Common Files\Acronis\SnapAPI\;
C:\Program Files (x86)\Brackets\command;
C:\Program Files\Git\cmd
```
Нажимаем Изменить... `(edit...)` и вставляем из буфера обмена адрес, добавляем к уже существующим, разделяя от последней записи символом ';' не стирая то что у нас есть, перезапускаем командную строку и всё работает
```
>>> mysql -u root -p
```
