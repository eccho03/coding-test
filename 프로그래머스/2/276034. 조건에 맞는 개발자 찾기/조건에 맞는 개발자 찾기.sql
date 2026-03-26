select ID, EMAIL, FIRST_NAME, LAST_NAME
from DEVELOPERS
where SKILL_CODE & (
    select sum(SKILLCODES.CODE)
    from SKILLCODES
    where name='Python' or name='C#'
) != 0
order by ID asc