select (PRICE div 10000)*10000 as PRICE_GROUP, count(PRICE) as PRODUCTS
from PRODUCT
group by PRICE_GROUP
order by PRICE_GROUP asc