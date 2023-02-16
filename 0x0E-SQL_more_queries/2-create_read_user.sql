-- Create an user if missing and grant it a reader privilege on a specific database
-- User creation
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Giving acces to user 2
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
-- Reload and apply changes
FLUSH PRIVILEGES;
