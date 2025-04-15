SELECT FIRST_HALF.FLAVOR 
FROM ICECREAM_INFO, FIRST_HALF
WHERE FIRST_HALF.TOTAL_ORDER>3000 AND ICECREAM_INFO.INGREDIENT_TYPE="fruit_based" AND FIRST_HALF.FLAVOR=ICECREAM_INFO.FLAVOR
ORDER BY TOTAL_ORDER DESC;