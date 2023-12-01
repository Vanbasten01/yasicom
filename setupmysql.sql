-- prepares a MySQL server for the project
-- Run Command:
--	cat setupmysql.sql | mysql -hlocalhost -uroot -p

CREATE DATABASE IF NOT EXISTS yasicom;
CREATE USER IF NOT EXISTS 'yasin'@'localhost' IDENTIFIED BY 'nador';
GRANT ALL PRIVILEGES ON `yasicom`.* TO 'yasin'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'yasin'@'localhost';
FLUSH PRIVILEGES;
