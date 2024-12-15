CREATE TABLE table_user(
user_id UUID primary key,
fullname varchar(40),
email varchar(50),
birthdate date,
password varchar(150),
terms bool,
creation_date date,
creation_time time
);
