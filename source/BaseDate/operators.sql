DELETE FROM personal WHERE id = '7b047f4a-ff68-4183-8e09-d0c9227dcbf5';

INSERT INTO personal (id,name,age) VALUES
	('7b047f4a-ff68-4183-8e09-d0c9227dcbf5','Иванов Иван', 89)
	ON CONFLICT (ID)
	DO UPDATE SET age = EXCLUDED.age;

UPDATE personal SET name = 'Пример Примеров' WHERE name = 'Петров Петр';

SELECT * FROM personal;