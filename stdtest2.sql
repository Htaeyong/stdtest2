CREATE DATABASE stdtest2;
CREATE USER 'stdtest2'@'%' IDENTIFIED BY 'Qwe123///';
GRANT ALL PRIVILEGES ON stdtest2.* TO 'stdtest2'@'%';
FLUSH PRIVILEGES;

CREATE TABLE users_tab (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL,
    department VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    role ENUM('admin', 'group_manager', 'user') NOT NULL,
    memo TEXT,
    password_fail_count INT DEFAULT 0,
    last_password_fail_date DATETIME,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status BOOLEAN DEFAULT TRUE
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE products_tab (
    id VARCHAR(15) NOT NULL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    manufacturer VARCHAR(100),
    eos DATE,  -- End Of Support
    eol DATE,  -- End Of Life
    product_category VARCHAR(100),
    product_specifications TEXT,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE sites_tab (
    id VARCHAR(15) NOT NULL PRIMARY KEY,
    site_name VARCHAR(100) NOT NULL,
    customer_contact_info VARCHAR(255),
    technical_support_contact VARCHAR(255),
    contract_file_path VARCHAR(255),
    contract_file_name VARCHAR(255),
    status BOOLEAN DEFAULT TRUE,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_modified_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE product_files_tab (
    id VARCHAR(15) NOT NULL PRIMARY KEY,
    product_id VARCHAR(15) NOT NULL,
    file_path VARCHAR(255),
    file_name VARCHAR(255),
    FOREIGN KEY (product_id) REFERENCES products_tab(id)
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;




INSERT INTO `stdtest2`.`users_tab` (`username`, `password`, `department`, `email`, `phone`, `role`) VALUES ('manager', '1234', '전체', 'manager@test.com', '010-1111-1111', 'admin');