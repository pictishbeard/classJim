DROP TABLE IF EXISTS schedules;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS gymclasses;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255),
    experience_level VARCHAR(255)
);

CREATE TABLE gymclasses (
    id SERIAL PRIMARY KEY,
    lesson_name VARCHAR(255),
    duration INT,
    difficulty_level VARCHAR(255),
    capacity INT,
    day VARCHAR(255)
);

CREATE TABLE schedules (
    id SERIAL PRIMARY KEY,
    member_id SERIAL REFERENCES members(id) ON DELETE CASCADE,
    gymclass_id SERIAL REFERENCES gymclasses(id) ON DELETE CASCADE
);