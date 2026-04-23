/**
 * AesCode Image Optimizer
 * Converts PNG/JPEG images to WebP with quality optimization.
 * Run: node scripts/optimize-images.mjs
 * 
 * Strategy:
 * - Judge/Mentor PNGs (3-4MB each) → WebP at quality 80 → ~150-300KB
 * - Archive JPEGs (2-4MB each) → WebP at quality 75 → ~100-200KB
 * - Originals are preserved as .bak files
 */

import sharp from 'sharp';
import { readdir, stat, rename } from 'fs/promises';
import { join, extname, basename } from 'path';

const PUBLIC = 'public/images';

const TARGETS = [
  { dir: 'judges',  quality: 80, maxWidth: 800 },
  { dir: 'mentors', quality: 80, maxWidth: 600 },
  { dir: 'archive', quality: 75, maxWidth: 1200 },
  { dir: 'team',    quality: 80, maxWidth: 800 },
  { dir: 'special', quality: 80, maxWidth: 800 },
];

async function optimizeDir({ dir, quality, maxWidth }) {
  const fullDir = join(PUBLIC, dir);
  const files = await readdir(fullDir);
  
  let totalBefore = 0;
  let totalAfter = 0;
  
  for (const file of files) {
    const ext = extname(file).toLowerCase();
    if (!['.png', '.jpeg', '.jpg'].includes(ext)) continue;
    
    const filePath = join(fullDir, file);
    const fileStats = await stat(filePath);
    const sizeBefore = fileStats.size;
    totalBefore += sizeBefore;
    
    const webpName = basename(file, ext) + '.webp';
    const webpPath = join(fullDir, webpName);
    
    // Convert to WebP
    await sharp(filePath)
      .resize({ width: maxWidth, withoutEnlargement: true })
      .webp({ quality })
      .toFile(webpPath);
    
    const webpStats = await stat(webpPath);
    totalAfter += webpStats.size;
    
    // Backup original
    await rename(filePath, filePath + '.bak');
    
    const reduction = ((1 - webpStats.size / sizeBefore) * 100).toFixed(1);
    console.log(`  ${file} → ${webpName}  (${formatSize(sizeBefore)} → ${formatSize(webpStats.size)}, -${reduction}%)`);
  }
  
  return { before: totalBefore, after: totalAfter };
}

function formatSize(bytes) {
  if (bytes < 1024) return bytes + 'B';
  if (bytes < 1048576) return (bytes / 1024).toFixed(0) + 'KB';
  return (bytes / 1048576).toFixed(1) + 'MB';
}

async function main() {
  console.log('🖼️  AesCode Image Optimizer\n');
  
  let grandBefore = 0;
  let grandAfter = 0;
  
  for (const target of TARGETS) {
    console.log(`\n📁 ${target.dir}/`);
    const { before, after } = await optimizeDir(target);
    grandBefore += before;
    grandAfter += after;
  }
  
  console.log(`\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`);
  console.log(`Total: ${formatSize(grandBefore)} → ${formatSize(grandAfter)}`);
  console.log(`Savings: ${formatSize(grandBefore - grandAfter)} (-${((1 - grandAfter / grandBefore) * 100).toFixed(1)}%)`);
  console.log(`\n✅ Originals preserved as .bak files.`);
  console.log(`   Delete backups when satisfied: find public/images -name "*.bak" -delete`);
}

main().catch(console.error);
