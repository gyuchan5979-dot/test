from common import *

def build():
    _html = open(ROOT + '/index.html', encoding='utf-8').read()
    REVIEWS = textwrap.dedent(_html[_html.index('    <!-- ===== 고객 후기 ====='):_html.index('    <!-- ===== FAQ 미리보기')]).strip()
    cases = CASES
    case_html = "\n".join([
        case_card(cases[0], wide=True, cls=" reveal"),
        case_card(cases[3], cls=" reveal d1"),
        case_card(cases[1], cls=" reveal"),
        case_card(cases[5], cls=" reveal d1"),
        case_card(cases[6], cls=" reveal d2"),
    ])
    prod_html = "\n".join(f'''<a href="products.html#{p["id"]}" class="product-card">
    <div class="product-img"><img src="images/products/{p["id"]}.jpg" alt="{p["alt"]}" loading="lazy"></div>
    <h3>{p["name"]}</h3>
    <p>{p["short"]}</p>
</a>''' for p in PRODUCTS)
    _feat = ["blog-4-blind-types.html", "blog-6-bedroom-blackout-blind.html", "blog-5-kids-room-blind.html"]
    posts = "\n".join(post_card(next(p for p in POSTS if p["file"] == f), 0) for f in _feat)

    faqs = [
        ("방문 실측과 상담은 정말 무료인가요?", "네. 서울 · 경기 · 인천 지역은 출장비와 상담비 없이 원단 샘플을 가지고 방문해 실측과 견적을 드립니다. 견적만 받아 보셔도 괜찮아요."),
        ("주문하면 언제 달 수 있나요?", "실측 후 맞춤 제작에 보통 5~7일이 걸리고, 시공은 일반 가정 기준 2~3시간이면 끝납니다. 입주 날짜가 정해져 있다면 상담 때 알려주세요."),
        ("전세집이라 벽에 구멍을 뚫기 어려워요.", "창틀이나 커튼박스를 활용한 무타공 시공을 먼저 검토해 드립니다. 창 구조에 따라 가능 여부가 달라 실측 때 정확히 안내드려요."),
        ("시공 후 문제가 생기면요?", "시공일로부터 1년간 무상 A/S를 해 드립니다. 전화나 카카오톡으로 사진을 보내주시면 빠르게 확인 후 방문합니다."),
    ]
    faq_html = "\n".join(f'''<details class="faq-item">
    <summary>{q}</summary>
    <div class="answer"><p>{a}</p></div>
</details>''' for q, a in faqs)

    body = f'''
<!-- ===== 메인 히어로: 배경 사진은 js/includes.js 의 HOME_HERO_SLIDES 에서 관리 ===== -->
<section class="hero" data-hero="home">
    <div class="container hero-content">
        <p class="hero-eyebrow">GYEOL &amp; BIT · CURTAIN &amp; BLIND</p>
        <h1>빛의 결을<br>기록합니다</h1>
        <p class="hero-sub">꾸민 사진이 아닌, 직접 시공한 집들로 보여드립니다.<br>서울 · 경기 · 인천 무료 방문 실측</p>
        <div class="hero-buttons">
            <a href="inquiry.html" class="btn btn-light">무료 방문 견적 <span class="arrow">→</span></a>
            <a href="gallery.html" class="btn btn-outline-white">시공사례 보기</a>
        </div>
    </div>
</section>

<!-- ===== 약속 띠 ===== -->
<section class="promise">
    <div class="promise-grid">
        <div class="promise-item"><span class="num">01</span><strong>무료 방문 실측</strong><p>원단 샘플을 들고 찾아갑니다</p></div>
        <div class="promise-item"><span class="num">02</span><strong>실제 사례로 상담</strong><p>비슷한 집 시공 사진으로 비교</p></div>
        <div class="promise-item"><span class="num">03</span><strong>5~7일 맞춤 제작</strong><p>창 크기에 맞춰 직접 제작</p></div>
        <div class="promise-item"><span class="num">04</span><strong>1년 무상 A/S</strong><p>시공 후에도 책임지고 관리</p></div>
    </div>
</section>

<!-- ===== 최근 시공사례 (카드 추가: gallery.html 과 같은 형식) ===== -->
<section class="section">
    <div class="container">
        <div class="section-head reveal">
            <div>
                <p class="section-tag">RECENT WORKS</p>
                <h2 class="section-title">최근 시공 사례</h2>
                <p class="section-sub">모든 사진은 결앤빛이 직접 시공하고 촬영한 실제 현장입니다.</p>
            </div>
            <a href="gallery.html" class="link-more">전체 사례 보기 →</a>
        </div>
        <div class="case-grid">
{textwrap.indent(case_html, "            ")}
        </div>
    </div>
</section>

<!-- ===== 비포 & 애프터 (사진: images/before-after/before-slide.jpg, after-slide.jpg — 같은 크기 · 같은 구도) ===== -->
<section class="section bg-ink">
    <div class="container">
        <div class="section-head reveal">
            <div>
                <p class="section-tag">BEFORE &amp; AFTER</p>
                <h2 class="section-title">커튼 하나로 달라진 거실</h2>
                <p class="section-sub">가운데 선을 좌우로 움직여 비교해 보세요.</p>
            </div>
            <a href="case-02.html" class="link-more" style="color:#fff">이 사례 자세히 →</a>
        </div>
        <div class="ba-slider reveal">
            <img src="images/before-after/before-slide.jpg" alt="커튼 시공 전 빈 거실 창" loading="lazy">
            <img src="images/before-after/after-slide.jpg" alt="그레이 겉커튼과 화이트 쉬폰 시공 후 거실" class="ba-after" loading="lazy">
            <span class="ba-label before">BEFORE</span>
            <span class="ba-label after">AFTER</span>
            <div class="ba-handle"></div>
            <input type="range" min="0" max="100" value="50" class="ba-range" aria-label="시공 전후 비교 슬라이더">
        </div>
        <div class="ba-caption">
            <span>거실 창</span>
            <span>그레이 겉커튼 + 화이트 쉬폰 (이중 레일)</span>
        </div>
    </div>
</section>

<!-- ===== 제품 컬렉션 ===== -->
<section class="section">
    <div class="container">
        <div class="section-head reveal">
            <div>
                <p class="section-tag">COLLECTION</p>
                <h2 class="section-title">공간에 맞는 원단과 제품</h2>
                <p class="section-sub">옆으로 넘겨 8가지 제품을 확인하세요.</p>
            </div>
            <a href="products.html" class="link-more">제품 전체 보기 →</a>
        </div>
        <div class="product-rail reveal">
{textwrap.indent(prod_html, "            ")}
        </div>
    </div>
</section>

<!-- ===== 브랜드 이야기 ===== -->
<section class="section bg-sand">
    <div class="container split">
        <div class="split-img reveal"><img src="images/about/about-01.jpg" alt="겉커튼과 쉬폰 원단 디테일" loading="lazy"></div>
        <div class="split-text reveal d1">
            <p class="section-tag">WHY GYEOL &amp; BIT</p>
            <h2>잘 만든 이미지보다<br>잘 달린 커튼을 보여드립니다</h2>
            <p>커튼과 블라인드는 사진보다 실제 집에서 훨씬 다르게 보입니다. 같은 화이트 린넨도 남향 거실과 북향 방에서 전혀 다른 색이 되니까요.</p>
            <p>그래서 결앤빛은 상담할 때 고객님 집과 비슷한 구조, 비슷한 방향의 <strong>실제 시공 사진</strong>을 먼저 보여드리고, 원단 샘플을 창에 직접 대 보며 결정하도록 돕습니다.</p>
            <a href="about.html" class="btn btn-outline">브랜드 이야기 <span class="arrow">→</span></a>
        </div>
    </div>
</section>

<!-- ===== 진행 과정 ===== -->
<section class="section">
    <div class="container">
        <div class="section-head reveal">
            <div>
                <p class="section-tag">PROCESS</p>
                <h2 class="section-title">상담부터 시공까지 4단계</h2>
            </div>
        </div>
        <div class="process-list reveal">
            <div class="process-item"><span class="step">STEP 01</span><h3>상담 신청</h3><p>전화 · 카톡 · 온라인으로 신청해 주세요. 창문 사진을 보내주시면 상담이 더 빨라집니다.</p></div>
            <div class="process-item"><span class="step">STEP 02</span><h3>방문 실측</h3><p>원단 샘플을 들고 방문해 창마다 정확히 재고, 빛의 방향을 보며 함께 고릅니다.</p></div>
            <div class="process-item"><span class="step">STEP 03</span><h3>맞춤 제작</h3><p>결정하신 원단과 치수로 5~7일 안에 제작합니다. 입주 일정에 맞춰 조율 가능해요.</p></div>
            <div class="process-item"><span class="step">STEP 04</span><h3>시공 · 기록</h3><p>깔끔하게 설치하고 정리한 뒤, 동의하신 경우 시공 사진을 사례로 기록합니다.</p></div>
        </div>
    </div>
</section>

{REVIEWS}

<!-- ===== FAQ 미리보기 ===== -->
<section class="section">
    <div class="container-narrow">
        <div class="section-head reveal">
            <div>
                <p class="section-tag">FAQ</p>
                <h2 class="section-title">자주 받는 질문</h2>
            </div>
            <a href="faq.html" class="link-more">질문 더 보기 →</a>
        </div>
        <div class="faq-list reveal">
{textwrap.indent(faq_html, "            ")}
        </div>
    </div>
</section>

<!-- ===== 매거진 (블로그 미리보기) ===== -->
<section class="section bg-paper">
    <div class="container">
        <div class="section-head reveal">
            <div>
                <p class="section-tag">MAGAZINE</p>
                <h2 class="section-title">고르기 전에 읽어 보세요</h2>
            </div>
            <a href="blog.html" class="link-more">매거진 전체 →</a>
        </div>
        <div class="post-grid reveal">
{textwrap.indent(posts, "            ")}
        </div>
    </div>
</section>
'''
    ld = [{
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "name": BRAND,
        "alternateName": "GYEOL & BIT",
        "legalName": "드리움커튼블라인드",
        "taxID": "210-42-66972",
        "url": SITE + "/",
        "image": SITE + "/images/og-image.jpg",
        "telephone": PHONE,
        "description": "서울·경기·인천 커튼·블라인드 맞춤 제작 및 시공. 실제 시공 사례로 상담하고 무료 방문 실측을 진행합니다.",
        "areaServed": ["서울특별시", "경기도", "인천광역시"],
        "openingHours": "Mo-Su 00:00-23:59",
        "sameAs": [KAKAO]
    }, {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": BRAND,
        "url": SITE + "/"
    }]
    head = '''    <!-- 네이버 서치어드바이저 / 구글 서치콘솔 인증 메타태그는 여기에 붙여넣기 -->
    <!-- <meta name="naver-site-verification" content=""> -->
    <!-- <meta name="google-site-verification" content=""> -->
'''
    page("index.html",
         "결앤빛 커튼&블라인드 | 실제 시공사례로 고르는 맞춤 커튼·블라인드",
         "서울·경기·인천 커튼·블라인드 시공 결앤빛. 직접 시공한 실제 사례 사진으로 상담하고, 원단 샘플을 들고 무료 방문 실측합니다. 린넨·암막커튼, 콤비·우드·허니콤 블라인드, 전동커튼.",
         "커튼, 블라인드, 커튼 시공, 블라인드 시공, 커튼 시공사례, 린넨커튼, 암막커튼, 콤비블라인드, 우드블라인드, 허니콤블라인드, 전동커튼, 서울 커튼, 경기 커튼, 인천 커튼",
         body, ld=ld, extra_head=head)
