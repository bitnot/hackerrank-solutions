SELECT DISTINCT City
FROM STATION
WHERE City REGEXP '^[^aeiou].*$'
    OR City REGEXP '^.*[^aeiou]$'