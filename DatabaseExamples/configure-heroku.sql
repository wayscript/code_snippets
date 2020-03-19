/* Create the table that will store your data - doesn't have to be done on
WayScript, but can be. */
CREATE TABLE website(
   id serial PRIMARY KEY,
   url VARCHAR (50) UNIQUE NOT NULL,
   name VARCHAR (50) NOT NULL
);

/* Inserting information into the created table */
INSERT INTO website (url, name)
    VALUES ('www.wayscript.com', 'WayScript'),
            ('www.w3schools.com', 'W3 Schools');

/* Verifying the number of rows created in the table */
SELECT COUNT(*) FROM table_name

/* Selecting all data from the database */
SELECT * FROM website
