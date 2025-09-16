select substring(START_DATE, 6,2)+0 as MONTH, CAR_ID, count(CAR_ID) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where left(START_DATE, 7)='2022-08' or left(START_DATE, 7)='2022-09' or left(START_DATE, 7)='2022-10'
group by MONTH, CAR_ID
having count(CAR_ID)>0 and
    CAR_ID in (
        select CAR_ID
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        where left(START_DATE, 7)='2022-08' or left(START_DATE, 7)='2022-09' or left(START_DATE, 7)='2022-10'
        group by CAR_ID
        having count(CAR_ID)>=5
    )
order by MONTH asc, CAR_ID desc