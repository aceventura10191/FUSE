"""Generate print-ready QR codes pointing at the live menu site."""
from pathlib import Path

import segno

URL = "https://aceventura10191.github.io/FUSION/"
INK = "#211b16"
OUT = Path(__file__).parent

qr = segno.make(URL, error="h", micro=False)

# Vector for the printer (scales to any size without blurring)
qr.save(OUT / "menu-qr.svg", scale=10, border=4, dark=INK, light="#ffffff")

# High-res raster: roughly 2000px square, fine for print up to ~17cm at 300dpi
modules = qr.symbol_size(scale=1, border=4)[0]
qr.save(OUT / "menu-qr.png", scale=max(1, 2000 // modules), border=4, dark=INK, light="#ffffff")

print(f"QR version {qr.version}, error level {qr.error}, {modules} modules incl. border")
print("->", URL)
