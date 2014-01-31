# InfluxDB POC

A simple test for evaluating [influxdb](http://influxdb.org)

The site can be visited at: http://duego.github.io/influxdb/  
Influxdb interface at: http://influxdb.lan:8083

Cluster admin: **root** / **root**  
Database admin: **test** / **test** / **test**

## Examples

To see the last few seconds of mock data that was inserted, issue this query in the admin interface:

```sql
select * from test.requests where time > now() - 2s
```