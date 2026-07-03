import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const base = path.resolve(here, '..');
const source = path.join(base, 'app');
const target = path.join(base, 'dist', 'analysis2-app');
const files = ['index.html', 'styles.css', 'formatting.js', 'data.js', 'exam-data.js', 'exam-logic.js', 'app.js'];
const directories = ['vendor', 'exam-pdfs'];

fs.mkdirSync(target, {recursive: true});
for (const file of files) {
  const sourcePath = path.join(source, file);
  if (!fs.existsSync(sourcePath)) throw new Error(`Quelldatei fehlt: ${sourcePath}`);
  fs.copyFileSync(sourcePath, path.join(target, file));
}
for (const directory of directories) {
  const sourcePath = path.join(source, directory);
  if (!fs.existsSync(sourcePath)) throw new Error(`Quellverzeichnis fehlt: ${sourcePath}`);
  fs.cpSync(sourcePath, path.join(target, directory), {recursive: true});
}
fs.writeFileSync(
  path.join(target, 'build-info.json'),
  JSON.stringify({builtAt: new Date().toISOString(), files, directories}, null, 2),
  'utf8'
);
console.log(`Produktionsausgabe erstellt: ${target}`);
