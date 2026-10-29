// Configuration centralisée : URL et identifiants viennent du .env (non versionné)
// ou des variables d'environnement. Aucune valeur secrète par défaut.
const fs = require('fs');
const path = require('path');

function loadDotEnv() {
  const envPath = path.resolve(__dirname, '..', '.env');
  if (!fs.existsSync(envPath)) return;
  for (const rawLine of fs.readFileSync(envPath, 'utf8').split(/\r?\n/)) {
    const line = rawLine.trim();
    if (!line || line.startsWith('#')) continue;
    const separator = line.indexOf('=');
    if (separator === -1) continue;
    const key = line.slice(0, separator).trim();
    let value = line.slice(separator + 1).trim();
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }
    if (process.env[key] === undefined) process.env[key] = value;
  }
}

loadDotEnv();

const env = {
  baseUrl: process.env.BASE_URL || '',
  credentials: {
    username: process.env.APP_USERNAME || '',
    password: process.env.APP_PASSWORD || '',
  },
  isConfigured() {
    return Boolean(this.baseUrl && this.credentials.username && this.credentials.password);
  },
};

module.exports = env;
