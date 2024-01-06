-- sites_tab id값 생성
DELIMITER $$

CREATE TRIGGER before_sites_tab_insert
BEFORE INSERT ON sites_tab FOR EACH ROW
BEGIN
    SET NEW.id = CONCAT('SITE', LPAD(IFNULL((SELECT MAX(CAST(SUBSTRING(id, 5) AS UNSIGNED)) FROM sites_tab), 0) + 1, 10, '0'));
END$$

DELIMITER ;

-- products_tab id값 생성
DELIMITER $$

CREATE TRIGGER before_products_tab_insert
BEFORE INSERT ON products_tab FOR EACH ROW
BEGIN
    SET NEW.id = CONCAT('PROD', LPAD(IFNULL((SELECT MAX(CAST(SUBSTRING(id, 5) AS UNSIGNED)) FROM products_tab), 0) + 1, 10, '0'));
END$$

DELIMITER ;


-- product_files_tab id값 생성
DELIMITER $$

CREATE TRIGGER before_product_files_tab_insert
BEFORE INSERT ON product_files_tab FOR EACH ROW
BEGIN
    SET NEW.id = CONCAT('PDFL', LPAD(IFNULL((SELECT MAX(CAST(SUBSTRING(id, 5) AS UNSIGNED)) FROM product_files_tab), 0) + 1, 10, '0'));
END$$

DELIMITER ;
