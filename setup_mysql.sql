-- Drop existing user if needed
DROP USER IF EXISTS 'hbnb_test'@'localhost';

-- Create a new MySQL user 'hbnb_test' with password 'hbnb_test_pwd'
CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the database 'hbnb_test_db' to 'hbnb_test' user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
