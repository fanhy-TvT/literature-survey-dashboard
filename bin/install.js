#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const sourceDir = path.join(__dirname, '..');
// Install to .trae/skills/literature-survey-dashboard in the user's current working directory
const targetDir = path.join(process.cwd(), '.trae', 'skills', 'literature-survey-dashboard');

function copyDirectory(src, dest) {
  if (!fs.existsSync(dest)) {
    fs.mkdirSync(dest, { recursive: true });
  }

  const entries = fs.readdirSync(src, { withFileTypes: true });

  for (let entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);

    // Ignore unnecessary files for the skill installation
    if (['node_modules', '.git', 'bin', 'package.json', 'package-lock.json'].includes(entry.name)) {
      continue;
    }

    if (entry.isDirectory()) {
      copyDirectory(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

console.log(`\n🚀 Installing literature-survey-dashboard skill...`);
console.log(`📂 Target directory: ${targetDir}`);

try {
  copyDirectory(sourceDir, targetDir);
  console.log('\n✅ Skill installed successfully!');
  console.log('You can now prompt your AI agent to use the "literature-survey-dashboard" skill.\n');
} catch (error) {
  console.error('\n❌ Error installing skill:', error.message);
  process.exit(1);
}
