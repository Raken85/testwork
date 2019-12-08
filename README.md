# Тестовое задание для Carbon Soft.

<h2>Установка python-пакета:</h2>

<pre>
$ pip3 install git+https://github.com/Raken85/testwork.git
</pre>

<h2>Запуск сервера:</h2>

<pre>
$ testwork-run-server
</pre>

На странице / для пользователя наименования столбцов id и usage кликабельны, по ним возможна сортировка.

<h2>Запуск клиент-демона:</h2>

<b>1 при установленном python-пакете:</b>

<pre>
$ testwork-client-start
</pre>

или 

<pre>
$ testwork-client-start server_url:port
</pre>

<b>2 в других случаях:</b>

установить httpie
<pre>
$ apt install httpie
</pre>
создать файл в допустимой директории, например /home/user/client.sh

вставить в него скрипт

<pre>
#!/bin/bash

if [ -n "$1" ]
then
	url=$1'/api/cpu'
else
	url='http://127.0.0.1:8001/api/cpu'
fi

while(true)
do
	usage=`top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}'`
	http POST $url usage=$usage
	sleep 10
done
</pre>

и запустить на выполнение

<pre>
$ setsid /home/user/client.sh
</pre>

или 

<pre>
$ setsid /home/user/client.sh server_url:port
</pre>