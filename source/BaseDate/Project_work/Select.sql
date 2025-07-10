SELECT
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
	JOIN programmer ON taskprogrammer.programmer_id = programmer.id
	-- where customer.name = 'ООО МБШ' and programmer.name = 'Москалев Дмитрий'


