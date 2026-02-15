select year(e1.DIFFERENTIATION_DATE) AS YEAR, (m.MAX_SIZE-e1.SIZE_OF_COLONY) as YEAR_DEV, e1.ID
from ECOLI_DATA as e1
join (
    select year(DIFFERENTIATION_DATE) as YEAR, max(SIZE_OF_COLONY) as MAX_SIZE
    from ECOLI_DATA as e2
    group by YEAR
) m on YEAR(e1.DIFFERENTIATION_DATE) = m.YEAR
order by YEAR asc, YEAR_DEV asc