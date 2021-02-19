/*CREATE TABLE convert_users(
   id serial PRIMARY KEY,
   email VARCHAR (50) NOT NULL,
   name VARCHAR (50) NOT NULL,
   account_usage INT
);*/

/*
INSERT INTO convert_users (email, name, account_usage)
    VALUES  ('derrick@wayscript.com', 'derrick', 90),
            ('name@gmail.com', 'name', 70 ),
            ('name2@gmail.com', 'name2', 0 ),
            ('name3@gmail.com', 'name3', 10 ),
            ('name4@gmail.com', 'name4', 85),
            ('name5@gmail.com', 'name5', 93),
            ('name6@gmail.com', 'name6' , 0);
*/

SELECT * FROM convert_users WHERE account_usage <30;
