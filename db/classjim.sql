DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS gymclasses;
DROP TABLE IF EXISTS schedules;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255),
    experience_level VARCHAR(255)
);

CREATE TABLE gymclasses (
    id SERIAL PRIMARY KEY,
    gymclass_name VARCHAR(255),
    duration INT,
    difficulty_level VARCHAR(255),
    capacity INT
);

CREATE TABLE schedules (
    id SERIAL PRIMARY KEY,
    member_id SERIAL REFERENCES members(id),
    gymclass_id SERIAL REFERENCES gymclasses(id)
);