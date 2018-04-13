SELECT City
    , len
FROM (
    SELECT City
        ,LENGTH(City) len
    FROM STATION
    ORDER BY LENGTH(City) ASC
        , City
    LIMIT 1
)mn

UNION ALL

SELECT City
    , len
FROM (
    SELECT City
        ,LENGTH(City) len
    FROM STATION
    ORDER BY LENGTH(City) DESC
        , City
    LIMIT 1
)mx