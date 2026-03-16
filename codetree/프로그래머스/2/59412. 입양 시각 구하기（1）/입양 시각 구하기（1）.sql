select hour(DATETIME) as HOUR, count(hour(DATETIME)) as COUNT
from ANIMAL_OUTS
where hour(DATETIME)>=9 and hour(DATETIME)<=19
group by HOUR
order by HOUR asc