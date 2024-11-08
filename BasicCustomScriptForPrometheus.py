# Demo for Integrating Prometheus to output on a grafana dashboard
from prometheus_client import start_http_server, Summary, Counter, Gauge
import random
import time

# Create Prometheus metric types
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUEST_COUNTER = Counter('app_requests_total', 'Total number of requests')
IN_PROGRESS = Gauge('inprogress_requests', 'Number of in-progress requests')

# A function to process a request
@REQUEST_TIME.time()
def process_request():
    IN_PROGRESS.inc()  # Increment in-progress requests
    time.sleep(random.uniform(0.1, 0.5))  # Simulate processing time
    IN_PROGRESS.dec()  # Decrement in-progress requests
    REQUEST_COUNTER.inc()  # Increment total requests


if __name__ == '__main__':
    # Start up the server to expose the metrics
    start_http_server(8000)
    print("Prometheus metrics server running on port 9090")

    # Generate requests indefinitely
    while True:
        process_request()