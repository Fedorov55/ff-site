const esbuild = require('esbuild');
const fs = require('fs');

const files = [
  { in: 'style.css', out: 'dist/style.min.css' },
  { in: 'critical.css', out: 'dist/critical.min.css' },
  { in: 'script.js', out: 'dist/script.min.js' },
  { in: 'calculator.js', out: 'dist/calculator.min.js' },
  { in: 'search.js', out: 'dist/search.min.js' },
];

async function build() {
  if (!fs.existsSync('dist')) fs.mkdirSync('dist');
  for (const f of files) {
    if (!fs.existsSync(f.in)) { console.log('skip (not found):', f.in); continue; }
    await esbuild.build({
      entryPoints: [f.in],
      outfile: f.out,
      minify: true,
      bundle: false,
      logLevel: 'info',
    });
    const orig = fs.statSync(f.in).size;
    const min = fs.statSync(f.out).size;
    console.log(f.in, '->', f.out, '|', orig, '->', min, 'bytes', '(' + Math.round((1 - min/orig)*100) + '% reduction)');
  }
  console.log('Build complete.');
}

build().catch(function(e){ console.error(e); process.exit(1); });