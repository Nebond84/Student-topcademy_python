-- INSERT INTO Customer (name,contact,telephone_number) VALUES
-- 	('ООО МБШ','Широгоров С.Г.','+79245367458'),
-- 	('Мехсталькомплект','Кочнев В.Н.','+79803333442'),
-- 	('Ростелеком','Свердлов Л.В','+79312343223'),
-- 	('ЯрЭнерго','Субботина В.Г.','+79567655745')

-- SELECT * FROM Customer

-- INSERT INTO programmer (name,birthdate,skill_level,phone) VALUES
-- 	('Шеин Иван','12-04-1993','junior','+79567655945'),
-- 	('Калугин Сергей','11-07-1989','junior','+79527655945'),
-- 	('Москалев Дмитрий','24-10-1984','middle','+79567655915'),
-- 	('Москалева Кристина','12-03-2000','middle','+79567455945'),
-- 	('Блузман Дмитрий','17-11-1991','senior','+79567605945')

-- SELECT * FROM programmer


-- INSERT INTO project_manager (name,birthdate,phone) VALUES
-- 	('Москалева Анна','09-05-1985','+79813333442'),
-- 	('Коротков Степан','09-10-1995','+79812333442'),
-- 	('Степанов Игорь','23-05-1998','+79813353442'),
-- 	('Чижанов Антон','09-09-1989','+79813333452'),
-- 	('Пушкин Сергей','23-04-1985','+79816667442')

-- SELECT * FROM project_manager

-- INSERT INTO project (title,start_project,end_project,customer_id,manager_id) VALUES
-- 	('Интернет платформа','12-02-2025','01-10-2025',(select id from customer where name = 'ООО МБШ'),
-- 	(select id from project_manager where name = 'Москалева Анна')),
-- 	('Клиентура','10-01-2025','30-09-20025',(select id from customer where name ='Ростелеком'),
-- 	(select id from project_manager where name ='Пушкин Сергей')),
-- 	('Веб сайт','22-04-2025','14-08-2025',(select id from customer where name ='Мехсталькомплект'),
-- 	(select id from project_manager where name ='Чижанов Антон')),
-- 	('Электронные квитанции','25-09-2025','31-12-2025',(select id from customer where name ='ЯрЭнерго'),
-- 	(select id from project_manager where name ='Коротков Степан'))
	
-- select * from project;

-- INSERT INTO task (description,start_task,end_task,project_id) VALUES
-- 	('Фронтэнд разработка','12-02-2025','30-04-2025',
-- 		(select id from project where title = 'Интернет платформа')),
-- 	('Бэкэнд разработка','01-03-2025','30-05-2025',
-- 		(select id from project where title = 'Интернет платформа' )),
-- 	('Тестирование','01-06-2025','30-08-2025',
-- 		(select id from project where title = 'Интернет платформа' )),
-- 	('Развертывание','02-08-2025','30-09-2025',
-- 		(select id from project where title = 'Интернет платформа' )),


-- 	('Фронтэнд разработка','10-01-2025','30-03-2025',
-- 		(select id from project where title = 'Клиентура' )),
-- 	('БД','12-03-2025','30-04-2025',
-- 		(select id from project where title = 'Клиентура' )),
-- 	('Тестирование','01-06-2025','30-08-2025',
-- 		(select id from project where title = 'Клиентура' )),
-- 	('Развертывание','02-08-2025','30-09-2025',
-- 		(select id from project where title = 'Клиентура' ))

-- select * from task;



-- INSERT INTO taskprogrammer (task_id,programmer_id) VALUES
-- 	((select id from task where description = 'Фронтэнд разработка'
-- 		and project_id = (select id from project where title = 'Интернет платформа') LIMIT 1),
-- 			(select id from programmer where name = 'Москалев Дмитрий')),
-- 	((select id from task where description = 'Бэкэнд разработка'
-- 		and project_id = (select id from project where title = 'Интернет платформа') LIMIT 1),
-- 			(select id from programmer where name = 'Москалева Кристина')),
-- 	((select id from task where description = 'Тестирование'
-- 		and project_id = (select id from project where title = 'Интернет платформа') LIMIT 1),
-- 			(select id from programmer where name = 'Шеин Иван')),
-- 	((select id from task where description = 'Развертывание'
-- 		and project_id = (select id from project where title = 'Интернет платформа') LIMIT 1),
-- 			(select id from programmer where name = 'Блузман Дмитрий')),


-- 	((select id from task where description = 'Фронтэнд разработка'
-- 		and project_id = (select id from project where title = 'Клиентура') LIMIT 1),
-- 			(select id from programmer where name = 'Москалев Дмитрий')),
-- 	((select id from task where description = 'БД'
-- 		and project_id = (select id from project where title = 'Клиентура') LIMIT 1),
-- 			(select id from programmer where name = 'Калугин Сергей')),
-- 	((select id from task where description = 'Тестирование'
-- 		and project_id = (select id from project where title = 'Клиентура') LIMIT 1),
-- 			(select id from programmer where name = 'Шеин Иван')),
-- 	((select id from task where description = 'Развертывание'
-- 		and project_id = (select id from project where title = 'Клиентура') LIMIT 1),
-- 			(select id from programmer where name = 'Блузман Дмитрий'))


-- select from taskprogrammer;
			
			
			




