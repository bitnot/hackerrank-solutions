SELECT COUNT(*) - (
        SELECT COUNT(*)
        FROM (
            SELECT DISTINCT City
            FROM STATION
        ) dst
    )
FROM STATION