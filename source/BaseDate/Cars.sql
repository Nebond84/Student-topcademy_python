DROP TABLE public.cars;

CREATE TABLE public.cars
(
	id uuid   NOT NULL,
	name text DEFAULT('Ford'),
	vin text  UNIQUE,
	year int  DEFAULT(1900),
	color text DEFAULT('Red'),
	model text DEFAULT('None'),
	PRIMARY KEY(vin)
)

