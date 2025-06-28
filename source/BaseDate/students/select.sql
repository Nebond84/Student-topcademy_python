-- SELECT name, age, grade from students where age>29;
-- select students.name, age, grade, groups.name as group from students, groups
-- 	where students.gr = groups.id and groups.name = 'Py42';

select students.name as student, age, grade, groups.name as group from groups,students
	where groups.id = students.gr;