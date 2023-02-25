-- Create a user if missing
-- Create statement
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- grant all access
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- Reload all databases and apply the change
FLUSH PRIVILEGES;
