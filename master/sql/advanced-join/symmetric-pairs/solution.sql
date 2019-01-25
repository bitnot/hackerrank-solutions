;with ff as (
    SELECT x, y, ROW_NUMBER() OVER(ORDER BY x,y) as id
    FROM Functions
)
SELECT x, y
FROM ff f1
WHERE EXISTS (
    SELECT 1
    FROM ff f2
    WHERE f2.y = f1.x
      AND f2.x = f1.y
      AND f2.id <> f1.id
      AND (f1.x <> f1.y OR f1.id < f2.id)
)
  AND x <= y
ORDER BY x, y