select s.name
from Students s
inner join Friends f
    on f.id = s.id
inner join Packages fp
    on fp.id = f.friend_id
inner join Packages p
    on p.id = s.id
where p.salary < fp.salary
order by fp.salary 