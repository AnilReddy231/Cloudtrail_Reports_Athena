select count (*) as TotalEvents, eventname, errorcode, errormessage 
from cloud_trail.cloudtrail_logs_for_events
where errorcode is not null
and eventtime >= '2019-05-01T00:00:00Z' 
group by eventname, errorcode, errormessage
order by TotalEvents desc
limit 10;