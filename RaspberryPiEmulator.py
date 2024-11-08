import time
import random
from prometheus_client import start_http_server, Gauge, Histogram

# Define metrics
cpu_usage_gauge = Gauge('device_cpu_usage_percentage', 'Simulated CPU Usage in Percentage')
memory_usage_gauge = Gauge('device_memory_usage_percentage', 'Simulated Memory Usage in Percentage')
response_time_histogram = Histogram('device_response_time_seconds', 'Simulated Service Response Time in Seconds')
uptime_gauge = Gauge('device_uptime', 'Simulated Device Uptime (1=up, 0=down)')

# Start the Prometheus client HTTP server on port 8000
start_http_server(8000)


def simulate_cpu_usage():
    # Randomly simulate CPU usage between 10% and 90%
    cpu_usage = random.uniform(10, 90)
    cpu_usage_gauge.set(cpu_usage)
    print(f"CPU Usage: {cpu_usage:.2f}%")


def simulate_memory_usage():
    # Randomly simulate memory usage between 20% and 95%
    memory_usage = random.uniform(20, 95)
    memory_usage_gauge.set(memory_usage)
    print(f"Memory Usage: {memory_usage:.2f}%")


def simulate_response_time():
    # Randomly simulate response time in seconds, with a higher chance for smaller values
    response_time = random.expovariate(1.0 / 0.2)  # Average response time of ~0.2 seconds
    response_time_histogram.observe(response_time)
    print(f"Response Time: {response_time:.3f} seconds")


def simulate_uptime():
    # Assume device is up; for simulation, set uptime to 1 (up) or 0 (down) with 98% uptime probability
    is_up = 1 if random.random() < 0.98 else 0
    uptime_gauge.set(is_up)
    status = "Up" if is_up == 1 else "Down"
    print(f"Uptime Status: {status}")


if __name__ == "__main__":
    print("Starting metrics simulation...")
    while True:
        # Update each metric
        simulate_cpu_usage()
        simulate_memory_usage()
        simulate_response_time()
        simulate_uptime()

        # Sleep for 5 seconds before updating again
        time.sleep(5)
