create table users (
	id serial,
	email varchar(255) unique,
	username varchar(255) unique,
	hashed_password varchar(80),
	primary key (id)
)