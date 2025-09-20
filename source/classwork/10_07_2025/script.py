import psycopg2 as PyPG


connectBD = PyPG.connect(
    dbname = "project",
    user = "postgres",
    password = "123",
    host = "localhost",
    port = 5432


)

cursor = connectBD.cursor()
query = (
    """SELECT
	customer.name as customer,
	customer.price as price,
	project.title as project,
	project_manager.name as manager,
	project_manager.salary as salary,
	task.description as task,
	programmer.name as programmer,
	programmer.salary as salary,
	programmer.phone as phone
FROM project
	JOIN customer ON project.customer_id = customer.id
	LEFT JOIN project_manager ON project.manager_id = project_manager.id
	JOIN task ON task.project_id = project.id
	JOIN taskprogrammer ON taskprogrammer.task_id = task.id
	JOIN programmer ON taskprogrammer.programmer_id = programmer.id"""
)



cursor.execute(query)

table = cursor.fetchall()
for line in table:
    for element in line:
        print(element, end= " - ")
    print()

cursor.close()
connectBD.close()