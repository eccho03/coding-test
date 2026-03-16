select ANIMAL_ID, NAME, left(DATETIME, 10) as '날짜'
from ANIMAL_INS
order by ANIMAL_ID