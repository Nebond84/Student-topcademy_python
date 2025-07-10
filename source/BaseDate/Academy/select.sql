select departaments.name as Кафедра,Financing as Финансирование,Faculties.name as факультет
	from departaments,Faculties where faculties.id = departaments.fac and departaments.fac = 3;

select departaments.name as Кафедра,Financing as Финансирование,Faculties.name as факультет
	from departaments,Faculties where faculties.id = departaments.fac;


select faculties.name as Факультет, departaments.name as Кафедра,Dean as Декан,Financing as Финансирование
	from departaments,Faculties where faculties.id = departaments.fac and departaments.fac = 4;

select faculties.name as Факультет, departaments.name as Кафедра,Dean as Декан,Financing as Финансирование
	from departaments,Faculties where faculties.id = departaments.fac;