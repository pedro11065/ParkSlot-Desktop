create table parkslot_now
(id uuid primary key,
plate varchar(7) unique,
custumer_name varchar(225),
entry_time time,
entry_date date);

create table parkslot_historic
(id uuid primary key,
plate varchar(7) unique,
custumer_name varchar(225),
entry_time time,
entry_date date,
exit_time time,
exit_date date);
