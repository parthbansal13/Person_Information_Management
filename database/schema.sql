CREATE DATABASE IF NOT EXISTS person_information_management
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE person_information_management;

CREATE TABLE IF NOT EXISTS persons_person (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    person_name VARCHAR(120) NOT NULL,
    mobile_number VARCHAR(16) NOT NULL,
    age SMALLINT UNSIGNED NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    post_code VARCHAR(12) NOT NULL,
    full_address TEXT NOT NULL,
    created_at DATETIME(6) NOT NULL
);

INSERT INTO persons_person
(
    person_name,
    mobile_number,
    age,
    city,
    state,
    post_code,
    full_address,
    created_at
)
VALUES
(
    'Parth Bansal',
    '1234567890',
    21,
    'Harda',
    'Madhya Pradesh',
    '461331',
    'Baheti Colony,Harda,M.p',
    '2026-09-27 06:56:30.247141'
),
(
    'Rahul Sharma',
    '9876543210',
    22,
    'Ahmedabad',
    'Gujarat',
    '380015',
    'Satellite Road, Ahmedabad',
    '2026-09-27 13:43:42.761455'
),
(
    'Janvi Agrawal',
    '9123456780',
    20,
    'Indore',
    'Madhya Pradesh',
    '452001',
    'Vijay Nagar, Indore',
    '2026-09-27 13:46:30.970239'
),
(
    'Vasudev Shastri',
    '9988776655',
    25,
    'Jaipur',
    'Rajasthan',
    '302001',
    'Malviya Nagar, Jaipur',
    '2026-09-27 13:47:53.106146'
),
(
    'Anjali Mehta',
    '9345678901',
    27,
    'Mumbai',
    'Maharashtra',
    '400001',
    'Fort Area, Mumbai',
    '2026-09-27 13:49:58.341617'
);