select
    ID,
    case NTILE(4) OVER (order by SIZE_OF_COLONY desc)
        when 1 then 'CRITICAL'
        when 2 then 'HIGH'
        when 3 then 'MEDIUM'
        when 4 then 'LOW'
    end as COLONY_NAME
    
from ECOLI_DATA
order by ID asc