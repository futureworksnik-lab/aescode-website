// Generates public/images/og-default.jpg (1200x630) — the default social-share card.
// Run: node scripts/generate-og.mjs
import sharp from 'sharp';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const out = join(__dirname, '..', 'public', 'images', 'og-default.jpg');

const NAVY = '#021934';
const CYAN = '#0891B2';

const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <rect width="1200" height="630" fill="${NAVY}"/>
  <rect x="0" y="0" width="1200" height="6" fill="${CYAN}"/>
  <text x="80" y="150" font-family="sans-serif" font-size="26" font-weight="700" letter-spacing="6" fill="${CYAN}">AESCODE CO.</text>
  <text x="78" y="320" font-family="serif" font-size="86" font-style="italic" fill="#FFFFFF">India's Clinical AI</text>
  <text x="78" y="420" font-family="serif" font-size="86" font-style="italic" fill="#FFFFFF">Validation Infrastructure</text>
  <line x1="80" y1="500" x2="240" y2="500" stroke="${CYAN}" stroke-width="3"/>
  <text x="80" y="560" font-family="sans-serif" font-size="28" fill="#9FB3C8">MedTech research, clinically grounded · www.aescode.nexus</text>
</svg>`;

await sharp(Buffer.from(svg)).jpeg({ quality: 90 }).toFile(out);
console.log('Wrote', out);
