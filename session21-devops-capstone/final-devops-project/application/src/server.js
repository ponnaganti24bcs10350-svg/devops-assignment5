/**
 * Enterprise Cloud-Native Application Server
 * Student: Srividya Ponnaganti (24BCS10350)
 * Session 21: Final DevOps Capstone Project
 */

const express = require('express');
const client = require('prom-client');
const winston = require('winston');

const app = express();
app.use(express.json());

const PORT = process.env.PORT || 8080;
const ENVIRONMENT = process.env.NODE_ENV || 'production';
const APP_NAME = process.env.APP_NAME || 'Final-DevOps-Enterprise-App';

// Setup Winston Structured JSON Logger
const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  defaultMeta: {
    service: 'final-devops-api',
    environment: ENVIRONMENT,
    student: 'Srividya Ponnaganti (24BCS10350)'
  },
  transports: [
    new winston.transports.Console()
  ]
});

// Setup Prometheus Metrics Collection
const collectDefaultMetrics = client.collectDefaultMetrics;
collectDefaultMetrics({ register: client.register });

const httpRequestCounter = new client.Counter({
  name: 'http_requests_total',
  help: 'Total count of HTTP requests handled',
  labelNames: ['method', 'route', 'status_code']
});

const httpRequestDurationHistogram = new client.Histogram({
  name: 'http_request_duration_seconds',
  help: 'Histogram of HTTP request durations in seconds',
  labelNames: ['method', 'route', 'status_code'],
  buckets: [0.01, 0.05, 0.1, 0.5, 1, 2, 5]
});

// Request Duration & Metric Middleware
app.use((req, res, next) => {
  const start = process.hrtime();
  res.on('finish', () => {
    const diff = process.hrtime(start);
    const durationSeconds = diff[0] + diff[1] / 1e9;
    const route = req.route ? req.route.path : req.path;
    
    httpRequestCounter.inc({ method: req.method, route, status_code: res.statusCode });
    httpRequestDurationHistogram.observe({ method: req.method, route, status_code: res.statusCode }, durationSeconds);

    logger.info({
      event: 'http_request_finished',
      method: req.method,
      path: req.path,
      statusCode: res.statusCode,
      duration_ms: Math.round(durationSeconds * 1000 * 100) / 100,
      client_ip: req.ip || req.connection.remoteAddress
    });
  });
  next();
});

// 1. Root & Health Probes
app.get('/', (req, res) => {
  res.status(200).json({
    message: 'Welcome to Final DevOps Enterprise Platform',
    app: APP_NAME,
    version: '2.0.0',
    status: 'HEALTHY',
    student: 'Srividya Ponnaganti (24BCS10350)',
    session: 'Session 21 - Capstone Project'
  });
});

app.get('/healthz', (req, res) => {
  res.status(200).json({
    status: 'UP',
    timestamp: new Date().toISOString(),
    uptime_seconds: process.uptime()
  });
});

app.get('/ready', (req, res) => {
  res.status(200).json({
    status: 'READY',
    checks: {
      database_connection: 'CONNECTED',
      cache_cluster: 'READY',
      storage_volume: 'MOUNTED'
    }
  });
});

// 2. Prometheus Metrics Scrape Endpoint
app.get('/metrics', async (req, res) => {
  try {
    res.set('Content-Type', client.register.contentType);
    res.end(await client.register.metrics());
  } catch (err) {
    logger.error('Error rendering metrics', { error: err.message });
    res.status(500).end(err.message);
  }
});

// 3. Application Business API
const databaseItems = [
  { id: 1, name: 'VPC-Networking-Stack', tier: 'Infrastructure', status: 'Active' },
  { id: 2, name: 'EKS-Kubernetes-Cluster', tier: 'Compute', status: 'Active' },
  { id: 3, name: 'ArgoCD-GitOps-Engine', tier: 'Delivery', status: 'Active' },
  { id: 4, name: 'Prometheus-Grafana-Stack', tier: 'Observability', status: 'Active' }
];

app.get('/api/v1/items', (req, res) => {
  res.status(200).json({
    count: databaseItems.length,
    data: databaseItems
  });
});

app.get('/api/v1/items/:id', (req, res) => {
  const item = databaseItems.find(i => i.id === parseInt(req.params.id));
  if (!item) {
    return res.status(404).json({ error: 'Item not found' });
  }
  res.status(200).json(item);
});

// Export server application for Jest testing
let server;
if (process.env.NODE_ENV !== 'test') {
  server = app.listen(PORT, () => {
    logger.info(`Server started and listening on port ${PORT}`);
  });
}

module.exports = { app, server };
