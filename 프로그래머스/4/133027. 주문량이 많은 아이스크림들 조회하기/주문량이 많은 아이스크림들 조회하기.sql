select H.FLAVOR
from FIRST_HALF as H
join JULY as J
on H.FLAVOR=J.FLAVOR
group by H.FLAVOR
order by sum(H.TOTAL_ORDER+J.TOTAL_ORDER) desc
limit 3
