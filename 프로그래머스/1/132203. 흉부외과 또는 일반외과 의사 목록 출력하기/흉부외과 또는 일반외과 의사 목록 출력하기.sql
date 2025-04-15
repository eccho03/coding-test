select DR_NAME, DR_ID, MCDP_CD, LEFT(HIRE_YMD,10)
from doctor
where MCDP_CD="CS" or MCDP_CD="GS"
order by HIRE_YMD desc, DR_NAME asc;