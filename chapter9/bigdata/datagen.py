import json
import csv
from google.cloud import pubsub_v1

project_name = 'nifty-matrix-463401-p'
topic_name = 'sales'
file = 'Sales-1.csv'

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_name, topic_name)

with open(file) as filehandle:
    rd = csv.DictReader(filehandle, delimiter=',')
    for row in rd:
        data = json.dumps(dict(row))
        print(f"Publishing: {data}")
        publisher.publish(topic_path, data=data.encode('utf-8'))
