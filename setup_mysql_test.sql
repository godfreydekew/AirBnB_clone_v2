-- Creates database hbnb_test_db
-- Creates new user hbnb_test (in localhost)
-- Grants  hbnb_test all privilege on hbnb_test_pwd
-- Grants hbnb_test SELECT privilege on performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS
	'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
