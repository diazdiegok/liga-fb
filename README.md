# Liga FB — sitio estático (Astro)

Sitio nuevo de academiapadelfb.com. Sin WordPress. Ranking, fotos y textos extraídos del WP actual.

## Desarrollo

```bash
npm install
npm run dev
```

## Publicar en Hostinger

```bash
npm run build
```

Subí el contenido de `dist/` a `public_html`. Hacé backup de WordPress antes. El `.htaccess` ya redirige las URLs viejas de Elementor.

## Configurar

- WhatsApp: `src/data/site.ts` → `whatsapp` (hoy placeholder `5493430000000`; el sitio original no tenía número público).
- Ranking: `src/data/ranking.json` (989 filas, T1–T4). Después se puede apuntar a un Google Sheet.

## Extraído del sitio viejo

- 77 imágenes de la biblioteca
- Rankings T1 (individual), T2, T3 y T4 (parejas)
- Sedes: Palermo, Open/Talleres, Américas + complejos mencionados
- Copy de la liga y horarios de academia
