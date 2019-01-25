SELECT cast(name as varchar(max)) + '(' + cast(occupation as varchar(1)) + ')'
FROM OCCUPATIONS
ORDER BY name
                                                                     
;with cnts as(
    SELECT occupation
        , count(*) AS cnt
    FROM OCCUPATIONS
    GROUP BY occupation
) 
SELECT 'There are a total of ' + CAST(cnt AS VARCHAR(MAX)) + ' ' + LOWER(occupation) + 's.'
FROM cnts
ORDER BY cnt, occupation