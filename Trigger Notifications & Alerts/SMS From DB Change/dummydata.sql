CREATE TABLE order_summary(
   id serial PRIMARY KEY,
   product VARCHAR (50) NOT NULL,
   quantity INT
);



INSERT INTO order_summary (product, quantity)
    VALUES  ( 'A', 50 ),
            ( 'B', 70 ),
            ( 'C', 25 ),
            ( 'A', 47 ),
            ( 'A', 26 ),
            ( 'B', 97 ),
            ( 'C', 38 ),
            ( 'A', 67 ),
            ( 'C', 75 ),
            ( 'A', 80 ),
            ( 'B', 48 ),
            ( 'A', 67 ),
            ( 'B', 74 ),
            ( 'B', 80 ),
            ( 'C', 68 ),
            ( 'A', 37 ),
            ( 'A', 58 ),
            ( 'B', 59 ),
            ( 'B', 46 ),
            ( 'A', 37 ),
            ( 'C', 20 ),
            ( 'A', 48 );
