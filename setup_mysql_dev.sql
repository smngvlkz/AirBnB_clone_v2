-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_dev' @'localhost' IDENTIFIED BY
    'hbnb_dev_pwd';

-- Grant all privileges on the hbnb_dev_db to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev' @'localhost';

-- Grant SELECT privilege on performance_schema to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev' @'localhost';

-- Apply the changes
FLUSH PRIVILEGES;

