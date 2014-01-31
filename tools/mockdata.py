"""
Creates mock requests to play with in influxdb.
The events are put into test.requests
"""

import time
import random
import itertools
import influxdb.client

influx = influxdb.client.InfluxDBClient('localhost', 8086, 'test', 'test', 'test')

# Create 1000 users and cycel ranomly between them
users = itertools.imap(random.choice, itertools.repeat([
	{
		'id': ''.join([random.choice(list('abcdef0123456789')) for _ in xrange(24)]),
		'gender': random.choice(['male', 'female']),
		'age': random.randint(18,40)
	} for _ in xrange(1000)]))

# Url generator
urls = itertools.imap(random.choice, itertools.repeat([
	'/users/nearby', '/conversations/<id>', '/counters', '/users/<id>']))

# Codes more probable of 200's
codes = itertools.imap(random.choice, itertools.repeat((200,)*10 + (404, 401, 500)))

methods = itertools.imap(random.choice, itertools.repeat(["POST", "GET", "PUT"]))


# Generate 100-300 requests per second between 1000 active users
while True:
	requests = xrange(random.randint(100, 300))
	influxes = []
	for code, url, method, user, _ in itertools.izip(codes, urls, methods, users, requests):
		influxes.append({
			"points": [
				[int(time.time()), code, url, method, user['id'], user['gender'], user['age']]
			],
			"name": "test.requests",
			"columns": ["time", "code", "url", "method", "user_id", "gender", "age"]
		})
	influx.write_points_with_precision(influxes)
	print influxes[0]['points'][0]
	time.sleep(1)
