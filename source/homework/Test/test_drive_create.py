import psycopg2


# connect = psycopg2.connect(
#     user = 'postgres',
#     password = '123',
#     host = 'localhost',
#     port = 5432,
#     dbname = 'test'
# )
#
# if connect:
#     print(f"Подключено")
#
# cursor = connect.cursor()
#
# cursor.close()
# connect.close()

connect ={
    "user" : 'postgres',
    "password" : '123',
    "host" : 'localhost',
    "port" : 5432,
    "dbname" : 'test'
}

with psycopg2.connect(**connect) as connect:
    with connect.cursor() as cursor:
        uuid = """CREATE EXTENSION IF NOT EXISTS "uuid-ossp";"""
        cursor.execute(uuid)
        proj_manager = """
                    CREATE TABLE Project_manager
                    (
                        id uuid DEFAULT uuid_generate_v4(),     
                        name text NOT NULL,
                        birthdate DATE NOT NULL,
                        phone TEXT NOT NULL CHECK (length(phone) = 12),
                    
                        PRIMARY KEY(id)
                    )
                    """
        customer = """
                CREATE TABLE Customer
                (
                    id uuid DEFAULT uuid_generate_v4(),
                    name text NOT NULL,
                    contact text NOT NULL,
                    telephone_number TEXT NOT NULL CHECK (length(telephone_number) = 12),
                
                    PRIMARY KEY(id)
                )
                """
        project = """
                CREATE TABLE Project
                (
                    id uuid DEFAULT uuid_generate_v4(),
                    title text NOT NULL,
                    start_project DATE NOT NULL,
                    end_project DATE,
                    customer_id uuid,
                    manager_id uuid,
                
                    PRIMARY KEY(id),
                    FOREIGN KEY(customer_id)
                    REFERENCES Customer(id) ON DELETE CASCADE,
                    FOREIGN KEY (manager_id)
                    REFERENCES Project_manager
                )
                """
        programmer = """
                    CREATE TABLE Programmer
                    (
                        id uuid DEFAULT uuid_generate_v4(),
                        name text NOT NULL,
                        birthdate DATE NOT NULL,
                        skill_level TEXT CHECK(skill_level IN('junior', 'middle', 'senior')),
                        phone TEXT NOT NULL CHECK(length(phone) = 12),
                    
                        PRIMARY KEY(ID)
                    
                    )
                    """
        task = """
                CREATE TABLE Task
                (
                    id uuid DEFAULT uuid_generate_v4(),
                    description text NOT NULL,
                    start_task DATE NOT NULL,
                    end_task DATE,
                    project_id uuid,
                
                    PRIMARY KEY(id),
                    FOREIGN KEY(project_id)
                    REFERENCES Project(id) ON DELETE CASCADE
                    
                )
                """
        task_programmer = """
                        CREATE TABLE TaskProgrammer
                        (
                            task_id uuid,
                            programmer_id uuid,
                        
                            FOREIGN KEY (task_id)
                            REFERENCES Task(id) ON DELETE CASCADE,
                            FOREIGN KEY (programmer_id)
                            REFERENCES Programmer(id) ON DELETE CASCADE,
                            PRIMARY KEY(task_id,programmer_id)
                        )
                        """
        # cursor.execute(proj_manager)
        # cursor.execute(customer)
        # cursor.execute(project)
        # cursor.execute(programmer)
        # cursor.execute(task)
        # cursor.execute(task_programmer)

