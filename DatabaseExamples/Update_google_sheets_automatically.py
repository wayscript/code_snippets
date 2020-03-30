CREATE TABLE survey(
   id serial PRIMARY KEY,
   name VARCHAR (50) NOT NULL,
   score INT NOT NULL
);


INSERT INTO survey (name, score)
    VALUES ('Derrick', 85),
            ('Mike', 100),
            ('Kelsey', 54),
            ('Henry', 95),
            ('Samual', 65),
            ('Tim', 89),
            ('Savanah', 56);


SELECT * FROM survey
