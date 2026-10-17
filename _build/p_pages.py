from common import *

def products():
    nav = "\n".join(f'<a href="#{p["id"]}" class="filter-btn">{p["name"]}</a>' for p in PRODUCTS)
    related = {}
    for c in CASES:
        for p in PRODUCTS:
            if p["name"].startswith(c["tag"].split()[0]):
                related.setdefault(p["id"], c)
    blocks = []
    for p in PRODUCTS:
        rc = related.get(p["id"])
        link = f'<a href="case-{rc["id"]}.html" class="btn btn-outline">관련 시공사례 보기 <span class="arrow">→</span></a>' if rc else '<a href="gallery.html" class="btn btn-outline">시공사례 보기 <span class="arrow">→</span></a>'
        blocks.append(f'''<article class="product-block" id="{p["id"]}">
    <div class="split-img"><img src="images/products/{p["id"]}.jpg" alt="{p["alt"]}" loading="lazy"></div>
    <div>
        <h2>{p["name"]}</h2>
        <span class="en">{p["en"]}</span>
        <p class="prose">{p["desc"]}</p>
        <dl class="spec-list">
            <dt>특징</dt><dd>{p["feature"]}</dd>
            <dt>추천 공간</dt><dd>{p["space"]}</dd>
            <dt>함께 쓰면</dt><dd>{p["pair"]}</dd>
            <dt>관리</dt><dd>{p["care"]}</dd>
        </dl>
        {link}
    </div>
</article>''')
    body = f'''
<section class="page-hero" data-hero="products">
    <div class="container">
        <h1>제품 안내</h1>
        <p class="lead">같은 창도 원단과 방식에 따라 전혀 다른 공간이 됩니다.<br>8가지 제품을 실제 시공 사진과 함께 비교해 보세요.</p>
    </div>
</section>

<section class="section">
    <div class="container">
        <nav class="product-nav" aria-label="제품 바로가기">
{textwrap.indent(nav, "            ")}
        </nav>
{textwrap.indent(chr(10).join(blocks), "        ")}
    </div>
</section>

<section class="section bg-sand">
    <div class="container">
        <div class="section-head">
            <div>
                <p class="section-tag">BY ROOM</p>
                <h2 class="section-title">공간별 추천</h2>
                <p class="section-sub">어떤 종류를 골라야 할지 모르겠다면 공간부터 정해 보세요.</p>
            </div>
        </div>
        <div class="table-wrap">
            <table>
                <thead><tr><th>공간</th><th>추천</th><th>가이드</th></tr></thead>
                <tbody>
                    <tr><td>거실</td><td>쉬폰 + 겉커튼, 콤비 · 우드 블라인드</td><td><a href="blog-4-blind-types.html">블라인드 종류 총정리</a></td></tr>
                    <tr><td>안방 · 침실</td><td>암막 커튼, 암막 롤스크린 · 허니콤</td><td><a href="blog-6-bedroom-blackout-blind.html">안방 암막 블라인드 vs 암막 커튼</a></td></tr>
                    <tr><td>자녀방</td><td>암막 롤스크린(줄 안전), 콤비 블라인드</td><td><a href="blog-5-kids-room-blind.html">자녀방 블라인드 고르는 법</a></td></tr>
                    <tr><td>주방 · 드레스룸</td><td>롤스크린, 허니콤 블라인드</td><td><a href="blog-2-blind-by-window.html">창 종류별 블라인드</a></td></tr>
                    <tr><td>서재 · 사무실</td><td>우드 블라인드, 선스크린 롤스크린</td><td><a href="blog-7-blind-color.html">블라인드 색상 고르는 법</a></td></tr>
                </tbody>
            </table>
        </div>
    </div>
</section>
'''
    ld = [{
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "결앤빛 커튼·블라인드 제품",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": p["name"], "url": f'{SITE}/products.html#{p["id"]}'} for i, p in enumerate(PRODUCTS)]
    }]
    page("products.html",
         "커튼 종류 · 블라인드 종류 비교 | 린넨·암막커튼, 콤비·우드·허니콤 블라인드 | 결앤빛",
         "결앤빛 커튼·블라인드 제품 안내. 린넨커튼, 쉬폰커튼, 암막커튼, 콤비블라인드, 우드블라인드, 허니콤블라인드, 롤스크린, 전동커튼의 특징과 추천 공간, 관리법을 실제 시공 사진과 함께 비교하세요.",
         "린넨커튼, 쉬폰커튼, 암막커튼, 콤비블라인드, 우드블라인드, 허니콤블라인드, 롤스크린, 전동커튼, 전동블라인드, 커튼 종류, 블라인드 종류",
         body, ld=ld)


def areas():
    groups = {}
    for a in AREAS:
        groups.setdefault(a["region"], []).append(a)
    pending = {"서울": [], "경기": [], "인천": []}
    html = []
    for region in ["서울", "경기", "인천"]:
        items = [f'<a href="{a["file"]}">{a["key"]}<small>{len(a["dongs"])}개 동 →</small></a>' for a in groups.get(region, [])]
        items += [f'<span>{n}</span>' for n in pending[region]]
        html.append(f'<h2 class="area-group-title">{region}</h2>\n<div class="area-index">\n' + "\n".join("    " + x for x in items) + "\n</div>")
    body = f'''
<section class="page-hero" data-hero="areas">
    <div class="container">
        <h1>시공 지역</h1>
        <p class="lead">서울 · 경기 · 인천 어디든 무료 방문 실측.<br>지역을 누르면 동네별 시공 안내와 사례를 볼 수 있어요.</p>
    </div>
</section>

<!-- 지역 페이지를 새로 만들면 아래 목록에 링크를 추가하고 js/includes.js 의 COMPLETED_AREAS 에도 한 줄 추가하세요. -->
<section class="section">
    <div class="container">
{textwrap.indent(chr(10).join(html), "        ")}
        <p class="section-sub mt-48">목록에 없는 지역도 방문 가능합니다. 전화나 카카오톡으로 문의해 주세요.</p>
    </div>
</section>
'''
    page("areas.html",
         "시공 지역 | 서울·경기·인천 커튼·블라인드 무료 방문 실측 | 결앤빛",
         "결앤빛 커튼·블라인드 시공 지역 안내. 서울 강남·서초·송파·마포, 경기 분당·판교·일산, 인천 송도 등 서울·경기·인천 전 지역 무료 방문 실측.",
         "서울 커튼, 경기 커튼, 인천 커튼, 서울 블라인드, 경기 블라인드, 인천 블라인드, 커튼 출장, 커튼 방문 견적",
         body)

    for ai, a in enumerate(AREAS):
        k, full = a["key"], a["full"]
        kd = {"인천서구": "인천 서구"}.get(k, k)
        dongs = "\n".join(f"<li>{d}</li>" for d in a["dongs"])
        picks = "\n".join(
            f'<li><a href="products.html#{product_by_name(n)["id"]}">{n}</a> — {product_by_name(n)["short"]}</li>' for n in a["picks"])
        # 지역별로 다른 사례가 보이도록 돌아가며 3개 선택
        local = [c for c in CASES if c.get("area") == k]
        rest = [CASES[(ai * 3 + j) % len(CASES)] for j in range(6)]
        picked = (local + [c for c in rest if c not in local])[:3]
        cards = "\n".join(case_card(c) for c in picked)
        main_img = picked[0]["id"]
        body = f'''
<section class="page-hero" data-hero="area" data-crumb="{k}">
    <div class="container">
        <h1>{full} 커튼 · 블라인드<br>방문 실측 · 맞춤 시공</h1>
        <p class="lead">{full} 전 지역 무료 방문 실측. 원단 샘플을 들고 찾아가 창에 직접 대 보며 상담합니다.</p>
        <div class="hero-buttons">
            <a href="inquiry.html" class="btn btn-light">{k} 방문 견적 신청 <span class="arrow">→</span></a>
            <a href="tel:{PHONE}" class="btn btn-outline-white">전화 상담</a>
        </div>
    </div>
</section>

<section class="section">
    <div class="container split">
        <div class="split-img reveal"><img src="images/cases/case-{main_img}.jpg" alt="{picked[0]["place"]} {picked[0]["tag"]} 시공 사진" loading="lazy"></div>
        <div class="split-text prose reveal d1">
            <p class="section-tag">{k.upper() if k.isascii() else "LOCAL NOTE"}</p>
            <h2>{k}의 집들을 다니며<br>알게 된 것</h2>
            <p>{a["intro"]}</p>
            <p>{a["tip"]}</p>
            <h3>{kd}에서 많이 찾는 제품</h3>
            <ul>
{textwrap.indent(picks, "                ")}
            </ul>
            <p>고르기 전에 읽어 보세요: <a href="blog-4-blind-types.html">블라인드 종류 총정리</a> · <a href="blog-6-bedroom-blackout-blind.html">안방 암막 블라인드</a> · <a href="blog-5-kids-room-blind.html">자녀방 블라인드</a></p>
        </div>
    </div>
</section>

<section class="section bg-sand">
    <div class="container">
        <div class="section-head reveal">
            <div>
                <p class="section-tag">COVERAGE</p>
                <h2 class="section-title">{full} 방문 가능 지역</h2>
                <p class="section-sub">아래 동네 외에도 {full} 전 지역 방문 실측이 가능합니다.</p>
            </div>
        </div>
        <ul class="dong-list">
{textwrap.indent(dongs, "            ")}
        </ul>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="section-head reveal">
            <div>
                <p class="section-tag">WORKS</p>
                <h2 class="section-title">결앤빛 시공 사례</h2>
            </div>
            <a href="gallery.html" class="link-more">전체 사례 보기 →</a>
        </div>
        <div class="case-grid is-even">
{textwrap.indent(cards, "            ")}
        </div>
    </div>
</section>
'''
        ld = [{
            "@context": "https://schema.org",
            "@type": "HomeAndConstructionBusiness",
            "name": f"{BRAND} - {full}",
            "url": f'{SITE}/{a["file"]}',
            "image": f'{SITE}/images/og-image.jpg',
            "telephone": PHONE,
            "description": f"{full} 커튼·블라인드 맞춤 제작 및 시공, 무료 방문 실측",
            "areaServed": {"@type": "Place", "name": full}
        }]
        kw = [f"{k} 커튼", f"{k} 블라인드", f"{k} 커튼 시공", f"{k} 블라인드 시공", f"{k} 암막커튼", f"{k} 린넨커튼",
              f"{k} 콤비블라인드", f"{k} 우드블라인드", f"{k} 전동커튼"] + [f"{d} 커튼" for d in a["dongs"][:4]]
        page(a["file"],
             f"{kd} 커튼·블라인드 시공 | {'·'.join(d.rstrip('동') if d.endswith('동') and len(d) > 2 else d for d in a['dongs'][:3])} 무료 실측 | 결앤빛",
             f"{kd} 커튼 · {kd} 블라인드 · {kd} 암막커튼 시공. {', '.join(a['dongs'][:4])} 등 {full} 전 지역 무료 방문 실측, 원단 샘플을 들고 찾아가 실제 시공 사례로 상담합니다.",
             ", ".join(kw), body, og_image=f'images/cases/case-{main_img}.jpg', ld=ld)


def about():
    body = '''
<section class="page-hero" data-hero="about">
    <div class="container">
        <h1>원단의 결,<br>창가의 빛</h1>
        <p class="lead">결앤빛은 꾸민 이미지 대신 실제로 시공한 집을 기록하는 커튼 · 블라인드 브랜드입니다.</p>
    </div>
</section>

<section class="section">
    <div class="container split">
        <div class="split-img reveal"><img src="images/about/about-01.jpg" alt="겉커튼과 쉬폰 원단 디테일" loading="lazy"></div>
        <div class="split-text reveal d1">
            <p class="section-tag">OUR STORY</p>
            <h2>사진보다 실제가<br>더 좋아야 합니다</h2>
            <p>커튼을 고를 때 가장 어려운 건, 화면 속 사진과 우리 집 창이 다르다는 점입니다. 빛의 방향, 바닥과 벽의 색, 창의 높이에 따라 같은 원단도 전혀 다르게 보이니까요.</p>
            <p>결앤빛은 그래서 <strong>직접 시공한 현장 사진</strong>만 보여드립니다. 상담할 때는 고객님 집과 비슷한 구조의 사례를 먼저 찾아 보여드리고, 원단 샘플을 실제 창에 대어 보며 결정합니다.</p>
        </div>
    </div>
</section>

<section class="section bg-sand">
    <div class="container">
        <div class="section-head reveal">
            <div>
                <p class="section-tag">PROMISE</p>
                <h2 class="section-title">결앤빛의 네 가지 약속</h2>
            </div>
        </div>
        <div class="process-list reveal">
            <div class="process-item"><span class="step">01</span><h3>실제 사례만</h3><p>홈페이지와 상담에 쓰는 사진은 모두 직접 시공한 현장입니다.</p></div>
            <div class="process-item"><span class="step">02</span><h3>무료 방문 실측</h3><p>서울 · 경기 · 인천 어디든 원단 샘플을 들고 찾아갑니다.</p></div>
            <div class="process-item"><span class="step">03</span><h3>정직한 견적</h3><p>필요 없는 옵션은 권하지 않고, 공간에 맞는 만큼만 제안합니다.</p></div>
            <div class="process-item"><span class="step">04</span><h3>1년 무상 A/S</h3><p>시공 후 불편한 점이 생기면 끝까지 책임지고 확인합니다.</p></div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container split reverse">
        <div class="split-img reveal"><img src="images/about/about-02.jpg" alt="화이트 쉬폰 커튼 디테일" loading="lazy"></div>
        <div class="split-text reveal d1">
            <p class="section-tag">CRAFT</p>
            <h2>1cm의 차이를<br>재는 사람들</h2>
            <p>커튼이 바닥에 끌리는지, 블라인드가 창틀에 부딪히는지는 실측 단계에서 결정됩니다. 결앤빛은 창마다 폭과 높이를 여러 지점에서 재고, 커튼박스 깊이와 콘센트 위치까지 확인한 뒤 제작에 들어갑니다.</p>
            <p>시공이 끝나면 주름을 정리하고 사용법을 알려드린 뒤, 동의해 주신 현장만 사진으로 남겨 다음 고객님의 상담에 씁니다.</p>
            <a href="gallery.html" class="btn btn-outline">시공사례 보기 <span class="arrow">→</span></a>
        </div>
    </div>
</section>
'''
    page("about.html",
         "브랜드 소개 | 실제 시공으로 증명하는 커튼·블라인드 | 결앤빛",
         "결앤빛은 꾸민 이미지 대신 직접 시공한 실제 현장을 기록하는 커튼·블라인드 브랜드입니다. 서울·경기·인천 무료 방문 실측, 정직한 견적, 1년 무상 A/S.",
         "결앤빛, 커튼 업체, 블라인드 업체, 커튼 맞춤제작, 커튼 시공 업체, 블라인드 시공 업체",
         body)


FAQ = [
    ("상담 · 견적", [
        ("방문 실측과 상담은 정말 무료인가요?", ["네. 서울 · 경기 · 인천 지역은 출장비와 상담비 없이 방문해 실측하고 견적을 드립니다. 견적만 받아 보시고 결정하지 않으셔도 괜찮습니다."]),
        ("방문 전에 미리 대략적인 가격을 알 수 있나요?", ["창문 사진과 대략의 가로 · 세로 길이를 카카오톡으로 보내주시면 예상 견적 범위를 먼저 안내해 드립니다. 정확한 금액은 실측 후 원단과 방식이 정해지면 확정됩니다."]),
        ("원단은 어떻게 고르나요?", ["방문할 때 원단 샘플을 가져가 실제 창에 대어 보며 고르실 수 있습니다. 같은 색도 빛의 방향에 따라 달라 보이기 때문에, 비슷한 집의 실제 시공 사진과 함께 비교해 드려요."]),
        ("저녁이나 주말에도 방문 가능한가요?", ["가능합니다. 원하시는 날짜와 시간을 견적 신청서에 남겨 주시면 일정을 맞춰 연락드립니다."]),
    ]),
    ("제작 · 시공", [
        ("주문 후 시공까지 얼마나 걸리나요?", ["맞춤 제작에 보통 5~7일이 걸립니다. 시공 자체는 일반 가정 기준 2~3시간 정도이며, 창이 많거나 전동 제품이 있으면 조금 더 걸릴 수 있습니다."]),
        ("신축 아파트 입주 전에 시공할 수 있나요?", ["네. 사전 점검일에 실측하고 입주 일정에 맞춰 시공하는 경우가 많습니다. 입주 3~4주 전에 연락 주시면 여유 있게 준비할 수 있어요."]),
        ("전세집이라 벽에 구멍을 뚫기 어려워요.", ["창틀이나 커튼박스를 활용한 무타공 시공을 먼저 검토합니다. 창 구조에 따라 가능 여부가 달라 실측 때 정확히 안내해 드립니다."]),
        ("기존 커튼 철거도 해 주시나요?", ["새 제품 시공 시 기존 커튼 · 블라인드 철거를 함께 진행해 드립니다. 철거품 처리 방법은 상담 시 안내해 드려요."]),
    ]),
    ("제품", [
        ("암막 커튼을 달면 빛이 완전히 차단되나요?", ["원단 자체는 빛을 대부분 막지만, 커튼 위와 옆, 아래 틈으로 빛이 들어올 수 있습니다. 레일을 창보다 넓게 연장하고 기장을 맞추는 방식으로 빛샘을 최대한 줄여 드립니다."]),
        ("커튼과 블라인드 중 무엇이 좋을까요?", ["거실처럼 분위기가 중요한 공간은 커튼, 주방이나 서재처럼 깔끔함과 빛 조절이 중요한 공간은 블라인드를 많이 선택하십니다. 두 가지를 함께 쓰는 구성도 많아요. <a href='blog-2-blind-by-window.html'>창 종류별 블라인드 고르는 법</a>도 참고해 보세요."]),
        ("전동 커튼은 나중에 바꿀 수 있나요?", ["수동 레일을 전동으로 바꾸려면 레일 교체와 전원 공사가 필요할 수 있습니다. 처음부터 고민되신다면 실측 때 전원 위치를 미리 확인해 두는 것을 권해 드려요. <a href='blog-3-motorized-curtain.html'>전동 커튼 설치 전 확인할 3가지</a>"]),
    ]),
    ("A/S", [
        ("A/S 기간은 얼마나 되나요?", ["시공일로부터 1년간 무상 A/S를 제공합니다. 전화나 카카오톡으로 사진과 함께 증상을 알려주시면 빠르게 확인 후 방문합니다."]),
        ("이사할 때 커튼을 가져가서 다시 달 수 있나요?", ["가능합니다. 새 집의 창 크기에 맞는지 확인한 뒤 재시공하며, 크기가 다르면 수선이나 레일 교체를 함께 안내해 드립니다."]),
    ]),
]

def faq():
    groups = []
    for g, items in FAQ:
        qs = "\n".join(f'''<details class="faq-item">
    <summary>{q}</summary>
    <div class="answer">{"".join(f"<p>{x}</p>" for x in a)}</div>
</details>''' for q, a in items)
        groups.append(f'<h2 class="faq-group-title">{g}</h2>\n<div class="faq-list">\n{textwrap.indent(qs, "    ")}\n</div>')
    import re
    ld = [{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", " ".join(a))}}
                       for _, items in FAQ for q, a in items]
    }]
    body = f'''
<section class="page-hero is-short" data-hero="faq">
    <div class="container">
        <h1>자주 묻는 질문</h1>
        <p class="lead">상담 전에 가장 많이 물어보시는 질문을 모았습니다.</p>
    </div>
</section>

<!-- 질문 추가: <details class="faq-item"> 블록을 복사해서 붙여넣기
     (head 안의 FAQPage 구조화 데이터에도 같은 질문을 추가하면 검색 노출에 도움이 됩니다) -->
<section class="section">
    <div class="container-narrow">
{textwrap.indent(chr(10).join(groups), "        ")}
    </div>
</section>
'''
    page("faq.html",
         "자주 묻는 질문 | 커튼·블라인드 견적, 시공 기간, A/S | 결앤빛",
         "커튼·블라인드 무료 방문 실측, 시공 기간, 신축 입주 시공, 전세집 무타공 시공, 암막커튼 빛샘, 전동커튼, A/S까지 자주 묻는 질문에 답했습니다.",
         "커튼 견적, 커튼 시공 기간, 커튼 무타공, 전세 커튼, 암막커튼 빛샘, 전동커튼 설치, 커튼 A/S, 블라인드 A/S",
         body, ld=ld)


def build():
    products(); areas(); about(); faq()
