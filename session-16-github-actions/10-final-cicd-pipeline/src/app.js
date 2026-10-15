const express = require('express');
const { add, subtract, multiply, divide } = require('./calculator');

const app = express();
app.use(express.json());

const PORT = process.env.PORT || 3000;
const APP_ENV = process.env.APP_ENV || 'production';

app.get('/', (req, res) => {
  res.json({
    status: 'success',
    message: '🚀 CI/CD Automated Deployment Online via GitHub Actions',
    environment: APP_ENV,
    version: '1.0.0',
    timestamp: new Date().toISOString()
  });
});

app.get('/health', (req, res) => {
  res.status(200).json({
    status: 'UP',
    uptime: process.uptime(),
    timestamp: Date.now()
  });
});

app.post('/api/calculate', (req, res) => {
  const { operation, a, b } = req.body;
  
  if (typeof a !== 'number' || typeof b !== 'number') {
    return res.status(400).json({ error: 'Operands a and b must be valid numbers' });
  }

  try {
    let result;
    switch (operation) {
      case 'add':
        result = add(a, b);
        break;
      case 'subtract':
        result = subtract(a, b);
        break;
      case 'multiply':
        result = multiply(a, b);
        break;
      case 'divide':
        result = divide(a, b);
        break;
      default:
        return res.status(400).json({ error: `Invalid operation: ${operation}` });
    }
    res.json({ operation, a, b, result });
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`Server listening on http://localhost:${PORT}`);
  });
}

module.exports = app;
