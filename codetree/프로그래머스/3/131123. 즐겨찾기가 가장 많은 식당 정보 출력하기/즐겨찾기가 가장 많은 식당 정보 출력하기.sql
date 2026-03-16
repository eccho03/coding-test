select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from REST_INFO as r
where FAVORITES in (
    select max(FAVORITES)
    from REST_INFO c
    where r.FOOD_TYPE = c.FOOD_TYPE
)
group by FOOD_TYPE
order by FOOD_TYPE desc
