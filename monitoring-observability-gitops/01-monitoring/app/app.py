"""
High-Performance Observability & Monitoring Demo Microservice
Student: Srividya Ponnaganti (24BCS10350)
Session 20: Monitoring, Observability & GitOps
"""

import time
import os
import psutil
import json
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler

# Setup Structured JSON Logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("ObservabilityApp")

REQUEST_COUNT = 0
START_TIME = time.time()

class MonitoringHandler(BaseHTTPRequestHandler):
    def _log_structured(self, status, path, duration_ms):
        log_entry = {
            "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            "service": "observability-demo-api",
            "environment": "production",
            "method": self.command,
            "path": path,
            "status_code": status,
            "duration_ms": round(duration_ms, 2),
            "client_ip": self.client_address[0],
            "trace_id": f"trace-{int(time.time()*1000)}-{os.getpid()}"
        }
        logger.info(json.dumps(log_entry))

    def do_GET(self):
        global REQUEST_COUNT
        start_req = time.time()
        REQUEST_COUNT += 1

        if self.path == "/" or self.path == "/healthz":
            # Application Health Endpoint
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            uptime_seconds = round(time.time() - START_TIME, 1)
            response = {
                "status": "HEALTHY",
                "app": "observability-demo-api",
                "version": "v1.0.0",
                "uptime_seconds": uptime_seconds,
                "student": "Srividya Ponnaganti (24BCS10350)"
            }
            self.wfile.write(json.dumps(response, indent=2).encode("utf-8"))
            self._log_structured(200, self.path, (time.time() - start_req) * 1000)

        elif self.path == "/metrics":
            # Prometheus Metrics Scrape Endpoint
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; version=0.0.4; charset=utf-8")
            self.end_headers()

            cpu_pct = psutil.cpu_percent(interval=0.1)
            mem = psutil.virtual_memory()
            uptime = time.time() - START_TIME

            metrics_data = f"""# HELP http_requests_total Total number of HTTP requests received.
# TYPE http_requests_total counter
http_requests_total{{service="observability-demo",handler="all"}} {REQUEST_COUNT}

# HELP process_cpu_utilization_percent Current CPU utilization percentage.
# TYPE process_cpu_utilization_percent gauge
process_cpu_utilization_percent{{service="observability-demo"}} {cpu_pct}

# HELP process_memory_utilization_bytes Current memory usage in bytes.
# TYPE process_memory_utilization_bytes gauge
process_memory_utilization_bytes{{service="observability-demo"}} {mem.used}

# HELP process_memory_total_bytes Total available system memory in bytes.
# TYPE process_memory_total_bytes gauge
process_memory_utilization_total_bytes{{service="observability-demo"}} {mem.total}

# HELP process_uptime_seconds Application uptime in seconds.
# TYPE process_uptime_seconds counter
process_uptime_seconds{{service="observability-demo"}} {uptime:.2f}

# HELP app_health_status Application health flag (1=Healthy, 0=Unhealthy).
# TYPE app_health_status gauge
app_health_status{{service="observability-demo"}} 1
"""
            self.wfile.write(metrics_data.encode("utf-8"))
            self._log_structured(200, "/metrics", (time.time() - start_req) * 1000)

        elif self.path == "/api/data":
            # Simulated Business Logic Endpoint
            time.sleep(0.05)  # Simulate 50ms compute latency
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data_response = {
                "message": "Data retrieved successfully",
                "items_count": 42,
                "server_time": time.strftime('%Y-%m-%d %H:%M:%S')
            }
            self.wfile.write(json.dumps(data_response).encode("utf-8"))
            self._log_structured(200, self.path, (time.time() - start_req) * 1000)

        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"error": "Endpoint Not Found"}')
            self._log_structured(404, self.path, (time.time() - start_req) * 1000)

def run():
    server = HTTPServer(("0.0.0.0", 8080), MonitoringHandler)
    logger.info(json.dumps({"event": "server_started", "port": 8080, "status": "listening"}))
    server.serve_forever()

if __name__ == "__main__":
    run()
