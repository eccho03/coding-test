select 
    p.PRODUCT_CODE, 
    p.PRICE*sum(s.SALES_AMOUNT) AS SALES
from PRODUCT p
join OFFLINE_SALE s
    on p.PRODUCT_ID = s.PRODUCT_ID
group by p.PRODUCT_ID
order by SALES desc, p.PRODUCT_CODE asc