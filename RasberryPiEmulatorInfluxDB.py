import os
import time

from influxdb_client_3 import InfluxDBClient3, Point

token = os.environ.get("INFLUXDB_TOKEN")

org = "InfluxDB Stand Up Demo"
host = "https://us-east-1-1.aws.cloud2.influxdata.com"

client = InfluxDBClient3(host=host, token=token, org=org)

database = "PythonScriptBucket"

data = {
    "point1": {
        "location": "Klamath",
        "species": "bees",
        "count": 23,
    },
    "point2": {
        "location": "Portland",
        "species": "ants",
        "count": 30,
    },
    "point3": {
        "location": "Klamath",
        "species": "bees",
        "count": 28,
    },
    "point4": {
        "location": "Portland",
        "species": "ants",
        "count": 32,
    },
    "point5": {
        "location": "Klamath",
        "species": "bees",
        "count": 29,
    },
    "point6": {
        "location": "Portland",
        "species": "ants",
        "count": 40,
    },
}

for key in data:
    point = (
        Point("census")
        .tag("location", data[key]["location"])
        .field(data[key]["species"], data[key]["count"])
    )
    client.write(database=database, record=point)
    time.sleep(1)  # separate points by 1 second

print("Complete")

# This is a basic SQL query you can test, which displays the data in a terminal
'''
query = """SELECT *
FROM 'census'
WHERE time >= now() - interval '24 hours'
AND ('bees' IS NOT NULL OR 'ants' IS NOT NULL)"""

# Execute the query
table = client.query(query=query, database="my-bucket", language='sql') )

# Convert to dataframe
df = table.to_pandas().sort_values(by="time")
print(df)
'''