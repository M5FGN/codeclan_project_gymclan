DROP TABLE bookings;
DROP TABLE members;
DROP TABLE gymsessions;

CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    member_type VARCHAR,
    member_status VARCHAR
);

CREATE TABLE gymsessions (
    id SERIAL PRIMARY KEY,
    gs_title VARCHAR,
    gs_description TEXT,
    gs_type VARCHAR,
    ability_level VARCHAR,
    gs_day VARCHAR,
    gs_date VARCHAR,
    gs_time VARCHAR,
    duration VARCHAR,
    gs_plan VARCHAR,
    gs_location VARCHAR,
    cost DECIMAL,
    capacity INT,
    instructor VARCHAR
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY, 
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    gymsession_id INT REFERENCES gymsessions(id) ON DELETE CASCADE,
    attended BOOLEAN
);





