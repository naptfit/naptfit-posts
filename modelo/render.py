"""Renderiza os slides de um post em PNG 1080x1350.

Uso: python3 modelo/render.py <pasta-do-post>
A pasta deve conter slides.html com elementos id="s1", "s2", ... (um por slide).
Gera <pasta>/naptfit-<slug>-N.png. Rode a partir da raiz do repositório,
depois de `npm install` (fonte Montserrat).
"""
import pathlib
import sys
from playwright.sync_api import sync_playwright

folder = pathlib.Path(sys.argv[1]).resolve()
slug = folder.name.split("-", 3)[-1]
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350})
    pg.goto((folder / "slides.html").as_uri())
    pg.wait_for_timeout(600)
    n = pg.locator("[id^=s].s").count()
    for i in range(1, n + 1):
        pg.locator(f"#s{i}").screenshot(path=str(folder / f"naptfit-{slug}-{i}.png"))
    b.close()
print(f"{n} slides renderizados em {folder}")
