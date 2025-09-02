-- Schema for PLP demo
CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, course TEXT);
CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY, title TEXT, instructor TEXT);
