import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000, // forzamos el puerto 3000
    strictPort: true, // si está ocupado, falla en vez de cambiar
  },
});
