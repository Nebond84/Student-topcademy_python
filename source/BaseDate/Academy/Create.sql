-- DROP TABLE Faculties,Departaments,Teachers,Groupss
-- CREATE TABLE Faculties
-- (
-- 	id int NOT NULL,
-- 	Name text UNIQUE NOT NULL,
-- 	Dean text NOT NULL,

-- 	PRIMARY KEY(ID)
-- )

-- select * from Faculties;

-- CREATE TABLE Departaments
-- (
-- 	id int NOT NULL,
-- 	Name text UNIQUE NOT NULL,
-- 	Financing INT NOT NULL CHECK(Financing >= 0),
-- 	fac int,
	
-- 	PRIMARY KEY(id),
-- 	FOREIGN KEY (fac)
-- 	REFERENCES Faculties (id)
	
	
-- )

-- select * from Departaments;


-- DROP TABLE Teachers
-- CREATE TABLE Teachers
-- (
-- 	id int NOT NULL,
-- 	EmploymentDate date NOT NULL CHECK(EmploymentDate > '01-01-1990'),
-- 	IsAssistant bit NOT NULL DEFAULT('0'),
-- 	IsProfessor bit NOT NULL DEFAULT('0'),
-- 	Name text NOT NULL,
-- 	Position text NOT NULL,
-- 	Premium money NOT NULL CHECK(Premium >= '0') DEFAULT('0'),
-- 	Salary money NOT NULL CHECK(Salary > '0'),
-- 	Surname text NOT NULL,
-- 	dep int,

-- 	PRIMARY KEY(id),
-- 	FOREIGN KEY (dep)
-- 	REFERENCES Departaments(id)
	
-- )

-- select * from Teachers;


CREATE TABLE Groupss
(
	id int NOT NULL,
	Name text NOT NULL UNIQUE,
	Rating int NOT NULL CHECK(Rating >= 0 AND  Rating <= 5),
	Year int NOT NULL CHECK(Year >= 1 AND Year <= 5),
	dep int,

	PRIMARY KEY(id),
	FOREIGN KEY (dep)
	REFERENCES Departaments(id)
)

-- select * from Groupss
