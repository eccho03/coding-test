select 
    HISTORY_ID, 
    CAR_ID, 
    left(START_DATE, 12) as START_DATE, 
    left(END_DATE, 12) as END_DATE,
    case
        when datediff(END_DATE, START_DATE)+1>=30 
        then '장기 대여' 
        else '단기 대여' 
    end as RENT_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where left(START_DATE, 7)='2022-09'
order by HISTORY_ID desc