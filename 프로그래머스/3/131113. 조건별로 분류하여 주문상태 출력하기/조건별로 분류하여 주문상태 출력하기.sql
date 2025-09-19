select 
    ORDER_ID, 
    PRODUCT_ID,
    left(OUT_DATE, 12) as OUT_DATE,
    case when OUT_DATE is NULL 
        then '출고미정'
        else
        case when datediff(left(OUT_DATE, 12), '2022-05-01')<=0
            then '출고완료'
            else '출고대기'
            end
    end as 출고여부
            
from FOOD_ORDER