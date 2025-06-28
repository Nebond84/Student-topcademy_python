select * from vegetables_and_fruits;

select name,type,color, caloric,description from vegetables_and_fruits where type='овощ' ;

select name,type,color, caloric,description from vegetables_and_fruits where type='фрукт' ;

select name from vegetables_and_fruits;

select color from vegetables_and_fruits;

select name,type,color, caloric,description from vegetables_and_fruits where color = 'зеленый'  and type = 'овощ';

select name,type,color, caloric,description from vegetables_and_fruits where color = 'красный'  and type = 'овощ';

select name,type,color, caloric,description from vegetables_and_fruits where color = 'зеленый'  and type = 'фрукт';

select name,type,color, caloric,description from vegetables_and_fruits where color = 'красный'  and type = 'фрукт';

select  count(*) as "кол-во овощей"  from vegetables_and_fruits where type='овощ';

select  count(*) as "кол-во фруктов"  from vegetables_and_fruits where type='фрукт';

select color, count(*) as "овощи и фрукты"  from vegetables_and_fruits where color='зеленый' group by color;

select color as "цвет", count(*) as "овощи и фрукты каждого цвета"  from vegetables_and_fruits group by color;

select color as "цвет", count(*) as "мин кол-во овощей и фруктов"  from vegetables_and_fruits
	group by color order by "мин кол-во овощей и фруктов" asc limit 1;

select color as "цвет", count(*) as "макс кол-во овощей и фруктов"  from vegetables_and_fruits
	group by color order by "макс кол-во овощей и фруктов" desc limit 1;

select name, caloric as "мин. колорийность"  from vegetables_and_fruits
	group by name, caloric order by caloric asc limit 1;

select name, caloric as "макс. колорийность"  from vegetables_and_fruits
	group by name, caloric order by caloric desc limit 1;

select avg(caloric) as "Средняя каллорийность" from vegetables_and_fruits;

select name, caloric as "мин. колорийность"  from vegetables_and_fruits where type = 'фрукт'
	group by name, caloric order by caloric asc limit 1;

select name, caloric as "мин. колорийность"  from vegetables_and_fruits where type = 'фрукт'
	group by name, caloric order by caloric desc limit 1;
