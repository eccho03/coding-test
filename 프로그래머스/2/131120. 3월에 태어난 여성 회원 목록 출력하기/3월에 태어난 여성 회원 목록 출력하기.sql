select MEMBER_ID, MEMBER_NAME, GENDER, left(DATE_OF_BIRTH, 10) as DATE_OF_BIRTH
from MEMBER_PROFILE
where substring(DATE_OF_BIRTH, 6, 2)='03' and TLNO is not NULL and GENDER='W'
order by MEMBER_ID asc;