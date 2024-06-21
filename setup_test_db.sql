-- Create the test database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Switch to the test database
USE hbnb_test_db;

-- Create the 'states' table if it doesn't already exist
-- This table will store state information with an auto-incrementing primary key
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255) NOT NULL
);
