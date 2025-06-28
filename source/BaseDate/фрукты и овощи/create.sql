drop table public.vegetables_and_fruits;

create table public.vegetables_and_fruits
(
	id uuid not null,
	name text,
	type text check(type in ('овощ','фрукт')),
	color text default('None'),
	caloric int,
	description text,

	primary key(id)
)


