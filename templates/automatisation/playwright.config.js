const { defineConfig, devices } = require('@playwright/test');
const env = require('./config/env');

module.exports = defineConfig({
  testDir: './tests',
  fullyParallel: false,
  forbidOnly: Boolean(process.env.CI),
  retries: process.env.CI ? 1 : 0,
  workers: 1,
  timeout: 90_000,
  expect: { timeout: 15_000 },
  reporter: [
    ['list'],
    ['allure-playwright', { outputFolder: 'allure-results', detail: true, screenshots: true }],
    ['./utils/evidence-reporter.js', { outputFolder: 'evidence' }],
  ],
  use: {
    baseURL: env.baseUrl,
    locale: 'fr-FR',
    trace: 'retain-on-failure',
    // Chaque test garde une capture de son état final comme preuve d'exécution.
    screenshot: { mode: 'on', fullPage: true },
    video: 'retain-on-failure',
    actionTimeout: 20_000,
    navigationTimeout: 45_000,
  },
  projects: [{ name: 'chromium', use: { ...devices['Desktop Chrome'] } }],
});
