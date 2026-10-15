const request = require('supertest');
const { app } = require('../src/server');

describe('Final DevOps Application Integration Tests', () => {
  it('GET / - should return 200 with application metadata', async () => {
    const res = await request(app).get('/');
    expect(res.statusCode).toEqual(200);
    expect(res.body).toHaveProperty('status', 'HEALTHY');
    expect(res.body).toHaveProperty('student', 'Srividya Ponnaganti (24BCS10350)');
  });

  it('GET /healthz - should return 200 UP status', async () => {
    const res = await request(app).get('/healthz');
    expect(res.statusCode).toEqual(200);
    expect(res.body.status).toEqual('UP');
  });

  it('GET /ready - should return 200 READY status', async () => {
    const res = await request(app).get('/ready');
    expect(res.statusCode).toEqual(200);
    expect(res.body.status).toEqual('READY');
  });

  it('GET /metrics - should return Prometheus metrics text', async () => {
    const res = await request(app).get('/metrics');
    expect(res.statusCode).toEqual(200);
    expect(res.text).toContain('http_requests_total');
  });

  it('GET /api/v1/items - should return list of cloud items', async () => {
    const res = await request(app).get('/api/v1/items');
    expect(res.statusCode).toEqual(200);
    expect(res.body.data.length).toBeGreaterThan(0);
  });

  it('GET /api/v1/items/1 - should return specific item', async () => {
    const res = await request(app).get('/api/v1/items/1');
    expect(res.statusCode).toEqual(200);
    expect(res.body.name).toEqual('VPC-Networking-Stack');
  });

  it('GET /api/v1/items/999 - should return 404 for missing item', async () => {
    const res = await request(app).get('/api/v1/items/999');
    expect(res.statusCode).toEqual(404);
  });
});
