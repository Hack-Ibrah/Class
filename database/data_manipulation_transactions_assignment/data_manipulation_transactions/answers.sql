-- Assignment: Data Manipulation and Transactions
-- Author: Hack-Ibrah

-- Question 1: Create table named student
CREATE TABLE student (
    id INT PRIMARY KEY,
    fullName VARCHAR(100),
    age INT
);

-- Question 2: Insert at least 3 records into student table
INSERT INTO student (id, fullName, age) VALUES
(1, 'Alice Johnson', 19),
(2, 'Bob Smith', 18),
(3, 'Charlie Brown', 21);

-- Question 3: Update age of student with ID 2 to 20
UPDATE student
SET age = 20
WHERE id = 2;
