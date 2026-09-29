create table products ( 
    name TEXT NOT NULL default 'Unknown',
    price INTEGER NOT NULL,
    quantity INTEGER DEFAULT 0
);





-- Do not modify below this line --
SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'products';
