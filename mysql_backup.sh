#!/bin/bash
# -*- coding:utf-8 -*-
# mysql_backup.sh
# This is a shell script of mysql backup

bak_dir=/home/moon1223/mysql_backup/`date +%Y-%m-%d-%H-%M-%S`
mysqldb=test
mysql_user=root
mysql_pw=root
mysql_command=/usr/bin/mysqldump

#判断是不是root用户登录
if [ $UID -ne 0 ];then
	echo "Must to be use root for execute "
	exit
eles
fi

#判断有没有目录
if [ ! -d $bak_dir ];then
	mkdir -p $bak_dir
	echo "The $bak_dir create successfully..."
else
	echo "This $bak_dir is exists..."
fi

#备份
$mysql_command -u$mysql_user -p$mysql_pw  -d $mysqldb > $bak_dir/$mysqldb.sql
if [ $? -eq 0 ];then
	echo "The mysql backup $mysqldb successfully..."
else
	echo "The mysql backup $mysqldb failed..."
fi
