-- Table structure private key and foreign key from states table
-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use hbtn_0d_usa
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS cities (
	id INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);
