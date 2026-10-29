// Playwright reporter that keeps the screenshots of the current run under
// evidence/<run>/ and lists them in a manifest (test, step, time, result, file).
const fs = require('fs');
const path = require('path');
const { slugify } = require('./evidence');

function runStamp(date) {
  const pad = (n) => String(n).padStart(2, '0');
  return `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}_${pad(
    date.getHours(),
  )}-${pad(date.getMinutes())}-${pad(date.getSeconds())}`;
}

class EvidenceReporter {
  constructor(options = {}) {
    this.root = path.resolve(options.outputFolder || 'evidence');
    this.entries = [];
  }

  onBegin(config) {
    this.startedAt = new Date();
    this.rootDir = config.rootDir;
    this.runDir = path.join(this.root, runStamp(this.startedAt));
    fs.mkdirSync(this.runDir, { recursive: true });
  }

  onTestEnd(test, result) {
    const project = test.parent.project()?.name || 'default';
    const spec = path.relative(this.rootDir, test.location.file).replace(/\\/g, '/');
    const status = result.status === 'passed' ? 'PASS' : result.status.toUpperCase();
    const testDir = path.join(
      this.runDir,
      project,
      slugify(spec.replace(/\.spec\.js$/, '')),
      `${slugify(test.title)}__${status}`,
    );
    const images = result.attachments.filter(
      (a) => a.contentType === 'image/png' && a.path && fs.existsSync(a.path),
    );
    const files = [];
    for (const image of images) {
      fs.mkdirSync(testDir, { recursive: true });
      const target = path.join(testDir, path.basename(image.path));
      fs.copyFileSync(image.path, target);
      files.push({
        step: image.name === 'screenshot' ? 'final state' : image.name,
        file: path.relative(this.runDir, target).replace(/\\/g, '/'),
        bytes: fs.statSync(target).size,
      });
    }
    this.entries.push({
      project,
      spec,
      title: test.title,
      status,
      skipReason: result.annotations?.find((a) => a.type === 'skip')?.description
        || test.annotations.find((a) => a.type === 'skip')?.description
        || '',
      startTime: result.startTime.toISOString(),
      durationMs: result.duration,
      error: result.error ? (result.error.message || '').split('\n')[0].slice(0, 300) : '',
      screenshots: files,
    });
  }

  onEnd(result) {
    const manifest = {
      startedAt: this.startedAt.toISOString(),
      finishedAt: new Date().toISOString(),
      overallStatus: result.status,
      tests: this.entries,
    };
    fs.writeFileSync(path.join(this.runDir, 'manifest.json'), JSON.stringify(manifest, null, 2));

    const escape = (text) => String(text).replace(/\|/g, '\\|').replace(/\r?\n/g, ' ');
    const lines = [
      `# Evidence manifest - run ${path.basename(this.runDir)}`,
      '',
      `Started: ${manifest.startedAt} - finished: ${manifest.finishedAt} - overall: ${result.status}`,
      '',
      '| Project | Spec | Test | Result | Step | Time | Screenshot | Bytes |',
      '|---|---|---|---|---|---|---|---|',
    ];
    for (const entry of this.entries) {
      const shots = entry.screenshots.length
        ? entry.screenshots
        : [{ step: entry.status === 'SKIPPED' ? `none (skipped: ${entry.skipReason})` : 'none', file: '', bytes: '' }];
      for (const shot of shots) {
        lines.push(
          `| ${entry.project} | ${entry.spec} | ${escape(entry.title)} | ${entry.status} | ${escape(
            shot.step,
          )} | ${entry.startTime} | ${shot.file ? `[${shot.file}](${shot.file})` : '-'} | ${shot.bytes} |`,
        );
      }
    }
    fs.writeFileSync(path.join(this.runDir, 'manifest.md'), `${lines.join('\n')}\n`);
    fs.writeFileSync(path.join(this.root, 'latest.txt'), `${path.basename(this.runDir)}\n`);
  }
}

module.exports = EvidenceReporter;
