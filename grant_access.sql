CREATE DATABASE blog;
update mysql.user set host = ' '  where user = 'root';
flush privileges;