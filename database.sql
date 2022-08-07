CREATE DATABASE IF NOT EXISTS 'datatest'
USE 'datatest'

CREATE TABLE atmosphere(
    time varchar(5),
    temperature INT,
    humidite varchar(3),
    pressure decimal(2,1)
);