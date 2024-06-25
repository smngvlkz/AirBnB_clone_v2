-- Drop existing user if needed
DROP USER IF EXISTS 'hbnb_test' @'localhost';

-- Create user if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_test' @'localhost' IDENTIFIED BY
    'hbnb_test_pwd';

-- Grant USAGE on *.* to the user (allowing basic operations like SHOW DATABASES)
GRANT USAGE ON *.* TO 'hbnb_test' @'localhost';

-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Grant all privileges on the hbnb_test_db to the user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test' @'localhost';

-- Grant SELECT privilege on performance_schema to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_test' @'localhost';

-- Apply the changes
FLUSH PRIVILEGES;
