-- Assignment: Movie Database Challenge
-- Author: Hack-Ibrah

-- 1. Create Actors table
CREATE TABLE Actors (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);

-- 2. Create Movies table
CREATE TABLE Movies (
    id INT PRIMARY KEY,
    title VARCHAR(100),
    year INT
);

-- 3. Insert sample actors
INSERT INTO Actors (id, name, age) VALUES
(1, 'Leonardo DiCaprio', 48),
(2, 'Scarlett Johansson', 38),
(3, 'Denzel Washington', 67);

-- 4. Insert sample movies
INSERT INTO Movies (id, title, year) VALUES
(1, 'Inception', 2010),
(2, 'Lucy', 2014),
(3, 'Fences', 2016);

-- 5. Example query: List all actors
SELECT * FROM Actors;

-- 6. Example query: List all movies
SELECT * FROM Movies;
