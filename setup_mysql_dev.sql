-- Create a new user and database

CREATE DATABASE IF NOT EXISTS hbtn_dev_db;

CREATE USER IF NOT EXISTS 'hbtn_dev'@'localhost' IDENTIFIED BY 'hbtn_dev_pwd';

FLUSH PRIVILEGES;

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
