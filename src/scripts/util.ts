export const $ = <T extends HTMLElement>(id: string) => document.getElementById(id) as T;

export function toast(msg: string) {
  const t = document.getElementById('toast');
  if (!t) return;
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2200);
}

export async function copy(text: string) {
  try { await navigator.clipboard.writeText(text); toast('Đã sao chép'); }
  catch { toast('Không sao chép được, hãy chọn và sao chép thủ công'); }
}
