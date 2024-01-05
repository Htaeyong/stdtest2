CREATE DATABASE stdtest2;
CREATE USER 'stdtest2'@'%' IDENTIFIED BY 'Qwe123///';
GRANT ALL PRIVILEGES ON stdtest2.* TO 'stdtest2'@'%';
FLUSH PRIVILEGES;

CREATE TABLE Users (
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
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;;




INSERT INTO `stdtest2`.`Users` (`username`, `password`, `department`, `email`, `phone`, `role`) VALUES ('manager', '1234', '전체', 'manager@test.com', '010-1111-1111', 'admin');