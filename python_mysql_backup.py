#!/usr/bin/python
# -*- coding:utf-8 -*-
# This is python script about mysql backup

import os
import time


mysql_user = 'root'
mysql_pw = 'root'
mysql_db_name = 'test'
backup_dir = '/home/moon1223/mysql_backup/'
mysql_command = '/usr/bin/mysqldump'
 
backup_time = time.strftime('%Y-%m-%d-%H-%M-%S')
backup_dir_time = backup_dir + backup_time


# 判断是不是root用户登录
#def whether_root_user():
#	if os.geteuid() != 0:
#		print "Must to be use root for execute "
#		os.sys.exit() 


# 判断有没有目录
def whether_exist_dir():
	if os.path.exists(backup_dir_time):
		print " The {} is exists ... ".format(backup_dir_time)
	else:
		os.makedirs(backup_dir_time)


def main():
#	whether_root_user()
	whether_exist_dir()

	backup_command = "{0} -u{1} -p {2} -d {3} > {4}/{3}.sql".format(mysql_command, mysql_user, mysql_pw, mysql_db_name, backup_dir_time)
	if os.system(backup_command) == 0:   
		print ( "{} is backup success!").format(mysql_db_name) 
	else:   
		print ( "{} is backup failed!").format(mysql_db_name) 


if __name__ == '__main__':
    main()

























