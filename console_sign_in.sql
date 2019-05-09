select eventname, useridentity.username, sourceipaddress, eventtime, additionaleventdata
from cloud_trail.cloudtrail_logs_for_events
where eventname = 'ConsoleLogin'
and eventtime >= '2019-02-17T00:00:00Z'
and eventtime < '2019-04-30T00:00:00Z';