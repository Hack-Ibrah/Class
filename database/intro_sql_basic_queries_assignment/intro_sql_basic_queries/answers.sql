-- Assignment: Introduction to SQL and Basic Queries
-- Author: Hack-Ibrah

-- 1. Retrieve checkNumber, paymentDate, and amount from payments table
SELECT checkNumber, paymentDate, amount
FROM payments;

-- 2. Retrieve orderDate, requiredDate, and status of orders that are 'In Process'
--    Sorted in descending order of orderDate
SELECT orderDate, requiredDate, status
FROM orders
WHERE status = 'In Process'
ORDER BY orderDate DESC;

-- 3. Display firstName, lastName, email of employees whose jobTitle is 'Sales Rep'
--    Ordered descending by employeeNumber
SELECT firstName, lastName, email
FROM employees
WHERE jobTitle = 'Sales Rep'
ORDER BY employeeNumber DESC;

-- 4. Retrieve all columns and records from offices table
SELECT *
FROM offices;

-- 5. Fetch productName and quantityInStock from products table
--    Sorted ascending by buyPrice, limit to 5 records
SELECT productName, quantityInStock
FROM products
ORDER BY buyPrice ASC
LIMIT 5;
