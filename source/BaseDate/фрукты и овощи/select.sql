select * from vegetables_and_fruits;

select name,type,color, caloric,description from vegetables_and_fruits where type='овощ' ;

select name,type,color, caloric,description from vegetables_and_fruits where type='фрукт' ;

select name from vegetables_and_fruits;

select color from vegetables_and_fruits;

select name,type,color, caloric,description from vegetables_and_fruits where color = 'зеленый'  and type = 'овощ';

select name,type,color, caloric,description from vegetables_and_fruits where color = 'красный'  and type = 'овощ';

select name,type,color, caloric,description from vegetables_and_fruits where color = 'зеленый'  and type = 'фрукт';

select name,type,color, caloric,description from vegetables_and_fruits where color = 'красный'  and type = 'фрукт';

