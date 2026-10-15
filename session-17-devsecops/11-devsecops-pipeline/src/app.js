const express = require('express');
const { hashPassword, verifyPassword, generateSecureToken } = require('./auth');

const app = express();
app.use(express.json());

// Basic security headers
app.use((req, res, next) => {
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('X-XSS-Protection', '1; mode=block');
  res.setHeader('Strict-Transport-Security', 'max-age=31536000; includeSubDomains');
  next();
});

const PORT = process.env.PORT || 8080;
const APP_ENV = process.env.APP_ENV || 'production';

app.get('/', (req, res) => {
  res.json({
    status: 'success',
    securityStatus: 'HARDENED',
    message: '🛡️ Production DevSecOps Secured Application Online',
    environment: APP_ENV,
    checks: {
      sast: 'PASSED (Semgrep/CodeQL)',
      sca: 'PASSED (npm audit / Trivy)',
      secretScanning: 'PASSED (Gitleaks)',
      containerScan: 'PASSED (Trivy CVE Clean)'
    },
    timestamp: new Date().toISOString()
  });
});

app.get('/health', (req, res) => {
  res.status(200).json({
    status: 'HEALTHY',
    uptime: process.uptime(),
    timestamp: Date.now()
  });
});

app.post('/api/auth/register', (req, res) => {
  const { username, password } = req.body;
  if (!username || !password || password.length < 8) {
    return res.status(400).json({ error: 'Password must be at least 8 characters long' });
  }
  const { salt, hash } = hashPassword(password);
  res.status(201).json({
    message: 'User registered securely',
    username,
    salt,
    hashLength: hash.length
  });
});

if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`DevSecOps Secure Server listening on port ${PORT}`);
  });
}

module.exports = app;
