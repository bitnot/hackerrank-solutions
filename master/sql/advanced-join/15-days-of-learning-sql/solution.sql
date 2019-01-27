;with 
daily_hackers as (
    select distinct hacker_id, submission_date
    from submissions ss
    where hacker_id in (
        select hacker_id 
        from (
            select distinct hacker_id, submission_date
            from submissions
        ) s
        where s.submission_date <= ss.submission_date
        group by s.hacker_id
        having count(*) = datediff(day, '2016-02-29', ss.submission_date)
    )
),
daily_count_cte as (
    select count(1) nr_hackers, submission_date
    from daily_hackers
    group by submission_date
),
max_subs_cte as (
    select hacker_id, submission_date, count(*) nr_subs
    from submissions ss
    group by hacker_id, submission_date
)
select c.submission_date, c.nr_hackers, n.hacker_id, n.name
from daily_count_cte c
cross apply (
    select h.hacker_id, h.name
    from hackers h
    where h.hacker_id = (
        select top 1 hacker_id
        from max_subs_cte ss
        where ss.submission_date = c.submission_date
        order by nr_subs desc, hacker_id asc
    )
) n
order by c.submission_date