CREATE DATABASE IF NOT EXISTS db;

CREATE TABLE IF NOT EXISTS contacts(
    id INT AUTO-INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL UNIQUE)

INSERT INTO contacts(first_name, last_name, phone_number)
VALUES('batya', 'berman', '0583294115')