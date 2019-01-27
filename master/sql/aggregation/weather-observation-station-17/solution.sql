SELECT TOP 1 CAST(LONG_W as decimal(6,4))
from station
where LAT_N > 38.7780
order by LAT_N asc