import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://www.aescode.nexus',
  output: 'static',
  build: {
    assets: 'assets'
  }
});
