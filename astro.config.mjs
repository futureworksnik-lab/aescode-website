// @ts-check
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://aescode.nexus',
  build: {
    format: 'file',  // Generates /about.html not /about/index.html — preserves existing URLs
  },
  vite: {
    css: {
      devSourcemap: true,
    },
  },
});
