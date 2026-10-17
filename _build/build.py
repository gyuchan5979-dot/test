import os, glob, datetime
from common import *
import p_index, p_cases, p_pages, p_blog

p_index.build(); p_cases.build(); p_pages.build(); p_blog.build(); p_blog.inquiry()

# 푸터 지역 링크 목록을 AREAS 에서 자동 생성
_inc = open(ROOT + "/js/includes.js", encoding="utf-8").read()
_a = _inc.index("var COMPLETED_AREAS = {"); _b = _inc.index("];", _inc.index("var ALL_AREAS = [")) + 2
_order = [a for r in ["서울", "경기", "인천"] for a in AREAS if a["region"] == r]
_comp = "var COMPLETED_AREAS = {\n" + ",\n".join(f'  "{a["key"]}": "{a["file"]}"' for a in _order) + "\n};"
_all = "var ALL_AREAS = [\n  " + ",".join(f'"{a["key"]}"' for a in _order) + "\n];"
_mid = "\n\n/* 푸터에 노출할 전체 지역 순서 (서울 → 경기 → 인천) */\n"
open(ROOT + "/js/includes.js", "w", encoding="utf-8").write(_inc[:_a] + _comp + _mid + _all + _inc[_b:])

today = datetime.date.today().isoformat()
pri = {"index.html": "1.0", "gallery.html": "0.9", "inquiry.html": "0.9", "products.html": "0.8", "areas.html": "0.8"}
files = sorted(os.path.basename(f) for f in glob.glob(ROOT + "/*.html") if not f.endswith("thanks.html"))
order = ["index.html","gallery.html","products.html","areas.html","blog.html","about.html","faq.html","inquiry.html"]
files = order + [f for f in files if f not in order]
urls = "\n".join(f"""  <url>
    <loc>{SITE}/{'' if f=='index.html' else f}</loc>
    <lastmod>{today}</lastmod>
    <priority>{pri.get(f, '0.7' if f.startswith(('case-','area-')) else '0.6')}</priority>
  </url>""" for f in files)
open(ROOT + "/sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
open(ROOT + "/robots.txt", "w").write(f"User-agent: *\nAllow: /\nDisallow: /thanks.html\n\nSitemap: {SITE}/sitemap.xml\n")
open(ROOT + "/images/favicon.svg", "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#1A1917"/><text x="32" y="44" font-family="serif" font-size="34" fill="#FAF9F6" text-anchor="middle">결</text></svg>\n')
print(len(files), "pages:", files)

# 파일 주소에 버전 표시 (브라우저에 저장된 옛 파일 대신 새 파일을 받게 함) — 배포할 때마다 VER 변경
import re
VER = datetime.datetime.now().strftime("%Y%m%d%H%M")
pat = re.compile(r'((?:css|js|images)/[\w/.-]+\.(?:css|js|jpg|svg))(\?v=[\w]+)?(?=["\'\)])')
for f in glob.glob(ROOT + "/*.html") + [ROOT + "/js/includes.js"]:
    s = open(f, encoding="utf-8").read()
    open(f, "w", encoding="utf-8").write(pat.sub(lambda m: m.group(1) + "?v=" + VER, s))
