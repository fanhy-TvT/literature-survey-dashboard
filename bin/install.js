#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

// 1. Parse command line arguments
const args = process.argv.slice(2);
const customTarget = args[0];

const sourceDir = path.join(__dirname, '..');

// 2. Determine target directory
// If the user provides a path, use it. Otherwise, default to `.trae/skills/literature-survey-dashboard` in their current working directory.
let targetDir;
if (customTarget) {
  targetDir = path.resolve(process.cwd(), customTarget);
} else {
  targetDir = path.join(process.cwd(), '.trae', 'skills', 'literature-survey-dashboard');
}

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

if (!customTarget) {
  console.log(`\n💡 Tip: You are installing to the default Trae directory.`);
  console.log(`If you want to install it elsewhere, you can pass a custom path:`);
  console.log(`   npx @fanhy-tvt/literature-survey-dashboard ./my-agent-folder/skills/literature-survey-dashboard`);
}

try {
  copyDirectory(sourceDir, targetDir);
  console.log('\n✅ Skill installed successfully!');
  console.log('You can now prompt your AI agent to use the "literature-survey-dashboard" skill.\n');
} catch (error) {
  console.error('\n❌ Error installing skill:', error.message);
  process.exit(1);
}
