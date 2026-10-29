// Step screenshots taken during a test. They are attached to the test result,
// so Allure shows them and utils/evidence-reporter.js copies them to evidence/.
function slugify(text) {
  return text
    .toLowerCase()
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '')
    .slice(0, 80);
}

async function captureStep(page, testInfo, step, { mask = [] } = {}) {
  const index = testInfo.attachments.filter((a) => a.name.startsWith('step ')).length + 1;
  const file = testInfo.outputPath(`step-${String(index).padStart(2, '0')}-${slugify(step)}.png`);
  await page.screenshot({ path: file, fullPage: true, mask });
  await testInfo.attach(`step ${String(index).padStart(2, '0')} - ${step}`, {
    path: file,
    contentType: 'image/png',
  });
}

module.exports = { captureStep, slugify };
