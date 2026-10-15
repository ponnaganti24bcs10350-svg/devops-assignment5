const request = require('supertest');
const app = require('../src/app');
const { hashPassword, verifyPassword, generateSecureToken } = require('../src/auth');

describe('Security Unit Tests: Cryptographic Authentication Engine', () => {
  test('hashPassword: generates salt and 128-char hex sha512 hash', () => {
    const { salt, hash } = hashPassword('MySecretPassword123!');
    expect(salt).toBeDefined();
    expect(hash.length).toBe(128);
  });

  test('verifyPassword: validates password matches salt and hash', () => {
    const password = 'CorrectPassword999!';
    const { salt, hash } = hashPassword(password);
    expect(verifyPassword(password, salt, hash)).toBe(true);
    expect(verifyPassword('WrongPassword123!', salt, hash)).toBe(false);
  });

  test('generateSecureToken: generates cryptographically strong random token', () => {
    const token1 = generateSecureToken();
    const token2 = generateSecureToken();
    expect(token1.length).toBe(64);
    expect(token1).not.toBe(token2);
  });
});

describe('DevSecOps Integration Tests: REST API & Security Headers', () => {
  test('GET / returns hardened security headers', async () => {
    const res = await request(app).get('/');
    expect(res.statusCode).toBe(200);
    expect(res.headers['x-content-type-options']).toBe('nosniff');
    expect(res.headers['x-frame-options']).toBe('DENY');
    expect(res.headers['x-xss-protection']).toBe('1; mode=block');
    expect(res.body.securityStatus).toBe('HARDENED');
  });

  test('GET /health returns 200 and status HEALTHY', async () => {
    const res = await request(app).get('/health');
    expect(res.statusCode).toBe(200);
    expect(res.body.status).toBe('HEALTHY');
  });

  test('POST /api/auth/register enforces minimum password length (8 chars)', async () => {
    const res = await request(app)
      .post('/api/auth/register')
      .send({ username: 'alice', password: '123' });
    expect(res.statusCode).toBe(400);
    expect(res.body.error).toContain('at least 8 characters');
  });

  test('POST /api/auth/register successfully hashes valid password', async () => {
    const res = await request(app)
      .post('/api/auth/register')
      .send({ username: 'bob', password: 'StrongPassword123!' });
    expect(res.statusCode).toBe(201);
    expect(res.body.username).toBe('bob');
    expect(res.body.hashLength).toBe(128);
  });
});
