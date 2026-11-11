"""드리움 워터마크: 가운데 반투명 로고 + 하단 DEURIUM / @deurium.

인스타 · 네이버 블로그 · 드리움 홈페이지 사진에만 쓴다 (결앤빛 사진에는 넣지 않음).
드리움 홈페이지 시공후기 사진은 _blog 사진을 그대로 가져가므로 블로그 사진에 넣으면 같이 적용된다.

사용: python3 _build/watermark.py 파일1.jpg 파일2.jpg ...  (제자리 덮어쓰기, 한 번만 실행)
"""
import sys
from PIL import Image, ImageChops, ImageDraw, ImageFont

LOGO = "/home/user/---/images/logo.png"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"

_mask = None


def _logo_mask():
    global _mask
    if _mask is None:
        g = Image.open(LOGO).convert("L")
        _mask = ImageChops.invert(g).point(lambda v: min(255, int(v * 1.8)))
    return _mask


def _spaced(d, text, font, y, W, track, alpha):
    widths = [d.textlength(ch, font=font) for ch in text]
    total = sum(widths) + track * (len(text) - 1)
    x = (W - total) / 2
    for ch, w in zip(text, widths):
        d.text((x, y), ch, font=font, fill=(255, 255, 255, alpha))
        x += w + track


def apply(im):
    im = im.convert("RGBA")
    W, H = im.size
    base = min(W, H * 4 / 3)
    lay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    mask = _logo_mask()
    lw = int(base * 0.28)
    m = mask.resize((lw, round(lw * mask.height / mask.width)))
    logo = Image.new("RGBA", m.size, (255, 255, 255, 0))
    logo.putalpha(m.point(lambda v: int(v * 0.40)))
    lay.alpha_composite(logo, ((W - lw) // 2, (H - m.height) // 2))
    d = ImageDraw.Draw(lay)
    f1 = ImageFont.truetype(FONT, int(base * 0.030))
    f2 = ImageFont.truetype(FONT, int(base * 0.019))
    _spaced(d, "DEURIUM", f1, H - base * 0.096, W, base * 0.030 * 0.22, 120)
    _spaced(d, "@deurium", f2, H - base * 0.057, W, 0, 110)
    im.alpha_composite(lay)
    return im.convert("RGB")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        apply(Image.open(p)).save(p, "JPEG", quality=86, optimize=True, progressive=True)
        print("watermarked", p)
