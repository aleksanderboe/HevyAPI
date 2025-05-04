// Frontend/vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  base: '/', // Set to '/subpath/' if deployed in a subdirectory
  resolve: {
    alias: {
      vue: 'vue/dist/vue.esm-bundler.js', // Ensure Vue is bundled correctly
    },
  },
  build: {
    outDir: 'dist', // Output to Frontend/dist
    assetsDir: 'assets',
    rollupOptions: {
      // Ensure external modules are bundled
      external: [],
    },
  },
})
