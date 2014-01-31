#!/usr/bin/env python
"""
Simple sink script to be used with statsite for proxying statsd metrics
"""

import sys
import influxdb.client

if __name__ == "__main__":
	influx = influxdb.client.InfluxDBClient(*sys.argv[1:])
	lines = sys.stdin.read().split("\n")

	metrics = [l.split("|") for l in lines if l]

	influxes = []
	for key, value, timestamp in metrics:
		influxes.append({
			"points": [[int(timestamp), value]],
			"name": key,
			"columns": ["time", "value"]
		})

	influx.write_points(influxes)