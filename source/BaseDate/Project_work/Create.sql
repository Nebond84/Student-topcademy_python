-- CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- CREATE TABLE Project_manager
-- (
-- 	id uuid DEFAULT uuid_generate_v4(),
-- 	name text NOT NULL,
-- 	birthdate DATE NOT NULL,
-- 	phone TEXT NOT NULL CHECK (length(phone) = 12),

-- 	PRIMARY KEY(id)
-- )

-- select * from Project_manager;


-- CREATE TABLE Customer
-- (
-- 	id uuid DEFAULT uuid_generate_v4(),
-- 	name text NOT NULL,
-- 	contact text NOT NULL,
-- 	telephone_number TEXT NOT NULL CHECK (length(telephone_number) = 12),

-- 	PRIMARY KEY(id)
-- )

-- select * from Customer;

-- CREATE TABLE Project
-- (
-- 	id uuid DEFAULT uuid_generate_v4(),
-- 	title text NOT NULL,
-- 	start_project DATE NOT NULL,
-- 	end_project DATE,
-- 	customer_id uuid,
-- 	manager_id uuid,

-- 	PRIMARY KEY(id),
-- 	FOREIGN KEY(customer_id)
-- 	REFERENCES Customer(id) ON DELETE CASCADE,
-- 	FOREIGN KEY (manager_id)
-- 	REFERENCES Project_manager
-- )

-- select * from Project;

-- CREATE TABLE Programmer
-- (
-- 	id uuid DEFAULT uuid_generate_v4(),
-- 	name text NOT NULL,
-- 	birthdate DATE NOT NULL,
-- 	skill_level TEXT CHECK(skill_level IN('junior', 'middle', 'senior')),
-- 	phone TEXT NOT NULL CHECK(length(phone) = 12),

-- 	PRIMARY KEY(ID)

-- )

-- select * from Programmer;


-- CREATE TABLE Task
-- (
-- 	id uuid DEFAULT uuid_generate_v4(),
-- 	description text NOT NULL,
-- 	start_task DATE NOT NULL,
-- 	end_task DATE,
-- 	project_id uuid,

-- 	PRIMARY KEY(id),
-- 	FOREIGN KEY(project_id)
-- 	REFERENCES Project(id) ON DELETE CASCADE
	
-- )

-- select * from Task;

-- CREATE TABLE TaskProgrammer
-- (
-- 	task_id uuid,
-- 	programmer_id uuid,

-- 	FOREIGN KEY (task_id)
-- 	REFERENCES Task(id) ON DELETE CASCADE,
-- 	FOREIGN KEY (programmer_id)
-- 	REFERENCES Programmer(id) ON DELETE CASCADE,
-- 	PRIMARY KEY(task_id,programmer_id)
-- )

-- select * from TaskProgrammer;



