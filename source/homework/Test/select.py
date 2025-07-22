import psycopg2


def select_db(connect):
    with psycopg2.connect(**connect) as connect:
        with connect.cursor() as cursor:
            query = (
                """SELECT
            	customer.name as customer,
            	project.title as project,
            	project_manager.name as manager,
            	task.description as task,
            	programmer.name as programmer,
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
                print(" | ".join(str(element) for element in line))

