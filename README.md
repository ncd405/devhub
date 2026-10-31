# devhub

Web cá nhân cho dev: dự án, blog, form liên hệ. Astro (tĩnh) + CSS thuần. Deploy miễn phí.

## Chạy thử trên máy
    npm install
    cp .env.example .env   # điền PUBLIC_FORM_ENDPOINT
    npm run dev

## Thêm nội dung
- Bài blog: file `.md` trong `src/content/blog/`
- Dự án: file `.md` trong `src/content/projects/`
- Từ Colab: File > Save a copy in GitHub, chọn thư mục `notebooks/` -> Action tự đổi thành bài blog

## Deploy (Cloudflare Pages)
Framework preset: Astro | Build command: `npm run build` | Output: `dist` | Node: 20
Thêm biến môi trường `PUBLIC_FORM_ENDPOINT` trong phần Settings của Pages.
Mỗi lần `git push` lên `main`, web tự build và deploy.
(Vercel: import repo, preset Astro, cấu hình tương tự.)

## Cloudflare (giao diện Workers Builds)
Build command: `npm run build` | Deploy command: `npx wrangler deploy` (đã có `wrangler.jsonc` trỏ tới `dist`)
Biến build: `PUBLIC_FORM_ENDPOINT`
