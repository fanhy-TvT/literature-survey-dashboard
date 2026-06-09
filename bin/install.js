#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const readline = require('readline');
const os = require('os');

const sourceDir = path.join(__dirname, '..');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const question = (query) => new Promise((resolve) => rl.question(query, resolve));

function copyDirectory(src, dest) {
  if (!fs.existsSync(dest)) {
    fs.mkdirSync(dest, { recursive: true });
  }

  const entries = fs.readdirSync(src, { withFileTypes: true });

  for (let entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);

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

async function main() {
  console.log(`\n🚀 Installing literature-survey-dashboard skill...\n`);

  // 1. Choose Base Directory
  console.log(`Where would you like to install the skill?`);
  console.log(`1) Current Project (${process.cwd()})`);
  console.log(`2) System Home Directory (${os.homedir()})`);
  
  let baseChoice = '';
  while (!['1', '2'].includes(baseChoice)) {
    baseChoice = (await question(`Enter 1 or 2: `)).trim();
  }
  const baseDir = baseChoice === '1' ? process.cwd() : os.homedir();

  // 2. Choose Agent Folder
  console.log(`\nWhich agent folder should it be installed to?`);
  console.log(`1) .agents`);
  console.log(`2) .trae`);
  console.log(`3) Custom (e.g., .claude, .cursor)`);
  
  let folderChoice = '';
  while (!['1', '2', '3'].includes(folderChoice)) {
    folderChoice = (await question(`Enter 1, 2, or 3: `)).trim();
  }

  let agentFolder = '';
  if (folderChoice === '1') {
    agentFolder = '.agents';
  } else if (folderChoice === '2') {
    agentFolder = '.trae';
  } else {
    while (!agentFolder) {
      agentFolder = (await question(`Enter custom folder name (e.g., .claude): `)).trim();
    }
  }

  // 3. Construct Target Directory and Copy
  const targetDir = path.join(baseDir, agentFolder, 'skills', 'literature-survey-dashboard');

  try {
    console.log(`\n📂 Target directory: ${targetDir}`);
    copyDirectory(sourceDir, targetDir);
    console.log('\n✅ Skill installed successfully!');
    console.log('You can now prompt your AI agent to use the "literature-survey-dashboard" skill.\n');
  } catch (error) {
    console.error('\n❌ Error installing skill:', error.message);
    process.exit(1);
  } finally {
    rl.close();
  }
}

main();
