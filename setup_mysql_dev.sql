-- Creates database hbnb_dev_db
-- Creates new user hbnb_dev (in localhost)
-- Grants  hbnb_dev all privilege on hbnb_dev_db
-- Grants hbnb_dev SELECT privilege on performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS
	'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
