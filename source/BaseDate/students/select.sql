-- SELECT name, age, grade from students where age>29;
-- select students.name, age, grade, groups.name as group from students, groups
-- 	where students.gr = groups.id and groups.name = 'Py42';

-- select students.name as student, age, grade, groups.name as group from groups,students
-- 	where groups.id = students.gr;
select * from students;

select students.name as student, age, grade, groups.name as group 
	from groups FULL OUTER JOIN students ON groups.id = students.gr; 


select students.name as student, age, grade, groups.name as group 
	from groups INNER JOIN students ON groups.id = students.gr; 

select students.name as student, age, grade, groups.name as group 
	from groups FULL OUTER JOIN students ON groups.id = students.gr
	where students.gr IS null OR groups.id IS null ;

select students.name as student, age, grade, groups.name as group 
	from groups LEFT JOIN students ON groups.id = students.gr;

select students.name as student, age, grade, groups.name as group 
	from students LEFT JOIN groups ON groups.id = students.gr;

select students.name as student, age, grade, groups.name as group 
	from groups LEFT JOIN students ON groups.id = students.gr
	where students.gr IS NULL;

select students.name as student, age, grade, groups.name as group 
	from groups RIGHT JOIN students ON groups.id = students.gr
	where students.gr IS NULL;

select students.name as student, age, grade, groups.name as group 
	from students RIGHT JOIN groups ON groups.id = students.gr;

select students.name as student, age, grade, groups.name as group 
	from groups RIGHT JOIN students ON groups.id = students.gr;

