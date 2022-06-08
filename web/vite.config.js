import * as path from 'path';
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  base: '/app/',
  build: {
    emptyOutDir: true,
    outDir: path.join('..', 'static'),
  },
  resolve: {
    alias: {
      app: path.join(process.cwd(), 'src'),
    },
  },
  plugins: [vue()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:4000',
        changeOrigin: true,
      },
    },
  },
});
