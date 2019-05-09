select eventname, useridentity.username, sourceIPAddress, eventtime, requestparameters from cloud_trail.cloudtrail_logs_for_events
where (eventname like '%AuthorizeSecurity%')
and eventtime > '2019-02-15T00:00:00Z'
order by eventtime asc