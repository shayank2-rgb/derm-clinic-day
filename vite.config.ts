import { defineConfig } from 'vite';
export default defineConfig({base: process.env.GITHUB_ACTIONS === 'true' ? '/derm-clinic-day/' : '/', test: { environment: 'node' }});
