select
    case 
        when substring(DIFFERENTIATION_DATE, 6, 2) between 1 and 3 then '1Q'
        when substring(DIFFERENTIATION_DATE, 6, 2) between 4 and 6 then '2Q'
        when substring(DIFFERENTIATION_DATE, 6, 2) between 7 and 9 then '3Q'
        when substring(DIFFERENTIATION_DATE, 6, 2) between 10 and 12 then '4Q'
    end as QUARTER,
    count(*) as ECOLI_COUNT
from ECOLI_DATA
group by QUARTER
order by QUARTER asc
