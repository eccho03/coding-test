select MCDP_CD as '진료과코드', count(MCDP_CD) as '5월예약건수'
from APPOINTMENT
where SUBSTRING(APNT_YMD, 6, 2)='05'
group by MCDP_CD
order by count(MCDP_CD) asc, MCDP_CD asc