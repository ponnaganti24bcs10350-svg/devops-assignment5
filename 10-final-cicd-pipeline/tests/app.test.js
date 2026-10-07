const request = require('supertest');
const app = require('../src/app');
const { add, subtract, multiply, divide } = require('../src/calculator');

describe('Unit Tests: Calculator Math Engine', () => {
  test('add: correctly sums two numbers', () => {
    expect(add(10, 5)).toBe(15);
    expect(add(-3, 8)).toBe(5);
  });

  test('subtract: correctly computes difference', () => {
    expect(subtract(20, 7)).toBe(13);
  });

  test('multiply: correctly computes product', () => {
    expect(multiply(6, 7)).toBe(42);
  });

  test('divide: correctly divides two numbers', () => {
    expect(divide(100, 4)).toBe(25);
  });

  test('divide: throws error when dividing by zero', () => {
    expect(() => divide(10, 0)).toThrow('Division by zero is not allowed');
  });
});

describe('Integration Tests: REST API Endpoints', () => {
  test('GET / returns 200 and success status', async () => {
    const res = await request(app).get('/');
    expect(res.statusCode).toBe(200);
    expect(res.body.status).toBe('success');
    expect(res.body.message).toContain('CI/CD Automated Deployment Online');
  });

  test('GET /health returns 200 and status UP', async () => {
    const res = await request(app).get('/health');
    expect(res.statusCode).toBe(200);
    expect(res.body.status).toBe('UP');
  });

  test('POST /api/calculate adds numbers correctly', async () => {
    const res = await request(app)
      .post('/api/calculate')
      .send({ operation: 'add', a: 15, b: 25 });
    expect(res.statusCode).toBe(200);
    expect(res.body.result).toBe(40);
  });

  test('POST /api/calculate returns 400 on division by zero', async () => {
    const res = await request(app)
      .post('/api/calculate')
      .send({ operation: 'divide', a: 50, b: 0 });
    expect(res.statusCode).toBe(400);
    expect(res.body.error).toBe('Division by zero is not allowed');
  });
});
