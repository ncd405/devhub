import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

// Sitemap tự viết, không cần thư viện ngoài
export const GET: APIRoute = async ({ site }) => {
  const base = (site?.toString() ?? '').replace(/\/$/, '');
  const posts = await getCollection('blog', (p) => !p.data.draft);
  const paths = ['/', '/projects/', '/blog/', '/tools/', '/tools/qr/', '/contact/', ...posts.map((p) => `/blog/${p.slug}/`)];
  const body = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${paths.map((u) => `  <url><loc>${base}${u}</loc></url>`).join('\n')}
</urlset>`;
  return new Response(body, { headers: { 'Content-Type': 'application/xml' } });
};
