#!/usr/bin/env python3
"""Genera un Short vertical (1080x1920) del Pichichi a partir de data/primera-pichichi.json.
Uso: python3 tools/short_pichichi.py AUDIO.mp3|SEGUNDOS out/short-pichichi.mp4
Los gráficos salen de los datos del repo; el audio es la locución de ElevenLabs."""
import json, sys, subprocess, collections, tempfile, os
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
BG, FG, ACC, MUT = (14, 22, 38), (240, 244, 250), (255, 196, 0), (120, 135, 160)
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
f = lambda s: ImageFont.truetype(FONT, s)

rows = json.load(open(os.path.join(os.path.dirname(__file__), "..", "data", "primera-pichichi.json")))["rows"]
titles = collections.Counter(r["person"] for r in rows).most_common(6)
record = max(rows, key=lambda r: r["goals"])

def dur(path):
    return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",path]).strip())

def center(d, y, text, font, fill):
    w = d.textlength(text, font=font); d.text(((W-w)/2, y), text, font=font, fill=fill)

def frame(t, total):
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    p = t / total
    if p < 0.62:  # barras de títulos de Pichichi
        center(d, 140, "PICHICHI", f(110), ACC)
        center(d, 270, "Títulos en Primera División", f(44), MUT)
        mx = titles[0][1]
        for i, (name, n) in enumerate(titles):
            y = 430 + i * 215
            appear = min(1, max(0, (p - 0.04 * i) / 0.10))
            short = name.split()[-1] if name != "Alfredo Di Stéfano" else "Di Stéfano"
            d.text((70, y), short, font=f(54), fill=FG)
            L = int((W - 260) * n / mx * appear)
            d.rounded_rectangle((70, y + 80, 70 + max(L, 1), y + 150), 14, fill=ACC if i == 0 else (70, 110, 190))
            if appear > 0.9: d.text((70 + L + 18, y + 82), str(n), font=f(60), fill=FG)
    else:  # récord
        center(d, 420, "RÉCORD ABSOLUTO", f(70), MUT)
        k = min(1, (p - 0.62) / 0.15)
        center(d, 600, str(int(record["goals"] * k)), f(420), ACC)
        center(d, 1090, "goles", f(80), FG)
        center(d, 1280, record["person"], f(78), FG)
        center(d, 1380, f'{record["club"]} · {record["season"]}', f(48), MUT)
    center(d, 1780, "Fútbol Histórico · Liga española", f(40), MUT)
    return im

def main(audio, out):
    silent = not os.path.exists(audio)  # si no hay audio, el argumento es la duración en segundos
    total = (float(audio) if silent else dur(audio)) + 0.5
    n = int(total * FPS)
    with tempfile.TemporaryDirectory() as tmp:
        for i in range(n):
            frame(i / FPS, total).save(f"{tmp}/f{i:05d}.png")
        cmd = ["ffmpeg","-y","-loglevel","error","-framerate",str(FPS),"-i",f"{tmp}/f%05d.png"]
        cmd += ([] if silent else ["-i",audio]) + ["-c:v","libx264","-pix_fmt","yuv420p"]
        cmd += ([] if silent else ["-c:a","aac","-shortest"]) + [out]
        subprocess.check_call(cmd)
    print("OK", out, f"{total:.1f}s")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
