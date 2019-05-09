select count (*) as TotalEvents, useridentity.username, eventname
from cloud_trail.cloudtrail_logs_for_events
where eventtime >= '2019-01-01T00:00:00Z' 
and useridentity.type = 'IAMUser'
group by useridentity.username, eventname
order by TotalEvents desc;