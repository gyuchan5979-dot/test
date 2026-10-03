/* =========================================================
   결앤빛 공통 영역 (한 곳에서 관리)
   -------------------------------------------------------
   ▸ 이 파일 하나로 [헤더 · 히어로 · 푸터 · 플로팅 버튼]을 관리합니다.
     수정하면 전 페이지에 바로 반영돼요.
   ▸ 연락처/카톡 주소는 js/config.js 에서 바꾸세요.
   ▸ 새 지역 페이지 완성 시 COMPLETED_AREAS 에 한 줄 추가.
      규칙: "지역명": "파일명.html",  ← 콜론(:)과 끝 쉼표(,) 꼭!
   ▸ 각 페이지의 제목(h1)·설명 문구는 SEO를 위해 HTML 안에 그대로 둡니다.
     이 파일은 배경 사진, 영문 소제목, 경로(홈 > 페이지)만 채워 줍니다.
   ========================================================= */

/* ✅ 메뉴 (헤더와 푸터에 같이 쓰임) */
var NAV_MENU = [
  { name: "시공사례", href: "gallery.html" },
  { name: "제품",     href: "products.html" },
  { name: "시공지역", href: "areas.html" },
  { name: "매거진",   href: "blog.html" },
  { name: "브랜드",   href: "about.html" },
  { name: "FAQ",      href: "faq.html" },
  { name: "견적문의", href: "inquiry.html" }
];

/* ✅ 메인 히어로 슬라이드 (사진만 바꾸려면 같은 파일명으로 FTP 업로드)
      caption: 사진 왼쪽 아래에 작게 표시되는 사례 설명 */
var HOME_HERO_SLIDES = [
  { img: "images/hero/hero-01.jpg?v=202610031654", caption: "거실 · 겉커튼 + 쉬폰", alt: "거실 베이지 겉커튼과 쉬폰 실제 시공 사진" },
  { img: "images/hero/hero-02.jpg?v=202610031654", caption: "매장 · 쉬폰 커튼",     alt: "벽돌 벽 매장 높은 창 쉬폰 커튼 실제 시공 사진" },
  { img: "images/hero/hero-03.jpg?v=202610031654", caption: "거실 · 쉬폰 커튼",     alt: "거실 화이트 쉬폰 커튼 실제 시공 사진" }
];

/* ✅ 서브 페이지 히어로 (HTML의 data-hero="키" 와 연결)
      img: 배경 사진 / eyebrow: 제목 위 영문 소제목 */
var PAGE_HEROES = {
  gallery:  { img: "images/hero/hero-gallery.jpg?v=202610031654",  eyebrow: "WORKS" },
  "case":   { img: "images/hero/hero-gallery.jpg?v=202610031654",  eyebrow: "CASE STUDY",  parent: { name: "시공사례", href: "gallery.html" } },
  products: { img: "images/hero/hero-products.jpg?v=202610031654", eyebrow: "PRODUCTS" },
  areas:    { img: "images/hero/hero-areas.jpg?v=202610031654",    eyebrow: "SERVICE AREA" },
  area:     { img: "images/hero/hero-areas.jpg?v=202610031654",    eyebrow: "SERVICE AREA", parent: { name: "시공지역", href: "areas.html" } },
  blog:     { img: "images/hero/hero-blog.jpg?v=202610031654",     eyebrow: "MAGAZINE" },
  post:     { img: "images/hero/hero-blog.jpg?v=202610031654",     eyebrow: "MAGAZINE",    parent: { name: "매거진", href: "blog.html" } },
  about:    { img: "images/hero/hero-about.jpg?v=202610031654",    eyebrow: "BRAND STORY" },
  faq:      { img: "images/hero/hero-faq.jpg?v=202610031654",      eyebrow: "FAQ" },
  inquiry:  { img: "images/hero/hero-inquiry.jpg?v=202610031654",  eyebrow: "CONTACT" },
  thanks:   { img: "images/hero/hero-inquiry.jpg?v=202610031654",  eyebrow: "THANK YOU" }
};

/* ✅ 완성된 지역 페이지만 등록 */
var COMPLETED_AREAS = {
  "강남": "area-gangnam.html",
  "서초": "area-seocho.html",
  "송파": "area-songpa.html",
  "마포": "area-mapo.html",
  "분당": "area-bundang.html",
  "판교": "area-pangyo.html",
  "일산": "area-ilsan.html",
  "송도": "area-songdo.html"
};

/* 푸터에 노출할 전체 지역 순서 (서울 → 경기 → 인천) */
var ALL_AREAS = [
  "강남","서초","송파","강동","강서","양천","영등포","마포","용산","성동",
  "광진","동작","관악","구로","금천","동대문","중랑","성북","강북","도봉",
  "노원","은평","서대문","종로","중구",
  "분당","판교","일산","광명","부천","안양","과천","산본","하남","위례",
  "송도","부평","인천서구","계양","남동"
];

/* ===================================================== */
/* 아래부터는 구조 코드입니다. 디자인 변경이 아니면 수정할 필요 없어요. */
/* ===================================================== */

var C = (typeof SITE_CONFIG !== "undefined") ? SITE_CONFIG : {};

var areaLinks = ALL_AREAS.map(function (name) {
  return COMPLETED_AREAS[name]
    ? '<a href="' + COMPLETED_AREAS[name] + '">' + name + '</a>'
    : '<span>' + name + '</span>';
}).join("");

var navItems = NAV_MENU.map(function (m) {
  return '<li><a href="' + m.href + '">' + m.name + '</a></li>';
}).join("");

/* ===== 공통 헤더 ===== */
var headerHTML = ''
+ '<header class="site-header" id="siteHeader">'
+ '  <div class="header-inner">'
+ '    <a href="index.html" class="logo" aria-label="' + C.companyName + ' 홈">'
+ '      <span class="logo-ko">결앤빛</span><span class="logo-en">GYEOL &amp; BIT</span>'
+ '    </a>'
+ '    <nav class="main-nav" id="mainNav" aria-label="주 메뉴"><ul>' + navItems + '</ul>'
+ '      <div class="nav-mobile-contact">'
+ '        <a href="tel:' + C.phone + '" class="btn btn-light">전화 ' + C.phone + '</a>'
+ '        <a href="' + C.kakaoUrl + '" class="btn btn-kakao">카카오톡 상담</a>'
+ '      </div>'
+ '    </nav>'
+ '    <a href="inquiry.html" class="header-cta">무료 견적</a>'
+ '    <button class="menu-toggle" id="menuToggle" aria-label="메뉴 열기" aria-expanded="false"><span></span><span></span><span></span></button>'
+ '  </div>'
+ '</header>';

/* ===== 공통 푸터 ===== */
var footerHTML = ''
+ '<footer class="site-footer">'
+ '  <div class="container">'
+ '    <div class="footer-top">'
+ '      <div class="footer-brand">'
+ '        <p class="footer-logo">결앤빛<span>GYEOL &amp; BIT</span></p>'
+ '        <p class="footer-slogan">원단의 결, 창가의 빛.<br>실제 시공으로 증명하는 커튼·블라인드</p>'
+ '      </div>'
+ '      <div class="footer-col">'
+ '        <h4>상담</h4>'
+ '        <p><a href="tel:' + C.phone + '">' + C.phone + '</a></p>'
+ '        <p><a href="mailto:' + C.email + '">' + C.email + '</a></p>'
+ '        <p>' + C.businessHours + '</p>'
+ '      </div>'
+ '      <div class="footer-col">'
+ '        <h4>바로가기</h4>'
+ '        <ul>' + navItems + '</ul>'
+ '      </div>'
+ '    </div>'
+ '    <div class="footer-areas">'
+ '      <h4><a href="areas.html">시공 지역 →</a></h4>'
+ '      <p class="footer-area-links">' + areaLinks + '</p>'
+ '    </div>'
+ '    <div class="footer-bottom">'
+ '      <p>' + C.companyName + (C.legalName ? ' (상호: ' + C.legalName + ')' : '') + ' · 대표 ' + C.ceo + (C.bizNumber ? ' · 사업자등록번호 ' + C.bizNumber : '') + ' · ' + C.address + '</p>'
+ '      <p>© ' + new Date().getFullYear() + ' ' + C.companyNameEn + '. All Rights Reserved.</p>'
+ '    </div>'
+ '  </div>'
+ '</footer>';

/* ===== 하단 상담 섹션 (푸터 위, <div id="site-cta"></div> 자리에 들어감) ===== */
var ctaHTML = ''
+ '<section class="contact-cta" id="contact">'
+ '  <div class="bg"><img src="images/hero/hero-cta.jpg?v=202610031654" alt="" aria-hidden="true" loading="lazy"></div>'
+ '  <div class="container">'
+ '    <div>'
+ '      <p class="section-tag" style="color:rgba(255,255,255,.6)">CONTACT</p>'
+ '      <h2>우리 집 창에 맞는 답,<br>방문해서 직접 보여드릴게요</h2>'
+ '      <p class="sub">원단 샘플을 들고 찾아가 실측부터 상담까지 무료로 진행합니다.<br>서울 · 경기 · 인천 어디든 연락 주세요.</p>'
+ '    </div>'
+ '    <div class="channel-list">'
+ '      <a href="tel:' + C.phone + '" class="channel"><div><strong>전화 상담</strong><span>' + C.phone + ' · ' + C.businessHours + '</span></div><span class="go">→</span></a>'
+ '      <a href="' + C.kakaoUrl + '" class="channel btn-kakao-link" data-link="kakao"><div><strong>카카오톡 상담</strong><span>창문 사진을 보내주시면 빠르게 안내해 드려요</span></div><span class="go">→</span></a>'
+ '      <a href="inquiry.html" class="channel"><div><strong>온라인 견적 신청</strong><span>원하는 날짜에 방문 실측 예약</span></div><span class="go">→</span></a>'
+ '    </div>'
+ '  </div>'
+ '</section>';

/* ===== 플로팅 버튼 (PC: 우측 하단 / 모바일: 하단 고정 바) ===== */
var floatingHTML = ''
+ '<div class="floating-buttons">'
+ '  <a href="tel:' + C.phone + '" class="float-btn float-phone" aria-label="전화 상담"><span class="float-icon">☎</span><span class="float-label">전화</span></a>'
+ '  <a href="' + C.kakaoUrl + '" class="float-btn float-kakao btn-kakao" aria-label="카카오톡 상담"><span class="float-icon">💬</span><span class="float-label">카톡</span></a>'
+ '  <a href="inquiry.html" class="float-btn float-inquiry" aria-label="견적 문의"><span class="float-icon">✎</span><span class="float-label">견적</span></a>'
+ '</div>';

(function () {
  /* 1) 헤더 · 푸터 · 플로팅 주입 */
  var headerMount = document.getElementById("site-header");
  if (headerMount) headerMount.outerHTML = headerHTML;

  var ctaMount = document.getElementById("site-cta");
  if (ctaMount) ctaMount.outerHTML = ctaHTML;

  var footerMount = document.getElementById("site-footer");
  if (footerMount) footerMount.outerHTML = footerHTML;

  if (!document.querySelector(".floating-buttons") && !document.body.hasAttribute("data-no-floating")) {
    document.body.insertAdjacentHTML("beforeend", floatingHTML);
  }

  /* 2) 메인 히어로 슬라이드 */
  var home = document.querySelector('[data-hero="home"]');
  if (home && HOME_HERO_SLIDES.length) {
    var slides = HOME_HERO_SLIDES.map(function (s, i) {
      return '<figure class="hero-slide' + (i === 0 ? ' is-active' : '') + '">'
        + '<img src="' + s.img + '" alt="' + s.alt + '"' + (i === 0 ? ' fetchpriority="high"' : ' loading="lazy"') + '>'
        + '<figcaption>' + s.caption + '</figcaption></figure>';
    }).join("");
    var dots = HOME_HERO_SLIDES.map(function (s, i) {
      return '<button class="hero-dot' + (i === 0 ? ' is-active' : '') + '" aria-label="' + (i + 1) + '번째 사진"></button>';
    }).join("");
    home.insertAdjacentHTML("afterbegin", '<div class="hero-slides">' + slides + '</div><div class="hero-scrim"></div>');
    home.insertAdjacentHTML("beforeend", '<div class="hero-dots">' + dots + '</div>');
  }

  /* 3) 서브 페이지 히어로 (배경 · 영문 소제목 · 경로) */
  document.querySelectorAll(".page-hero[data-hero]").forEach(function (hero) {
    var cfg = PAGE_HEROES[hero.getAttribute("data-hero")];
    if (!cfg) return;
    var img = hero.getAttribute("data-hero-img") || cfg.img;   // 페이지별 사진 지정 가능
    hero.insertAdjacentHTML("afterbegin",
      '<div class="page-hero-bg"><img src="' + img + '" alt="" aria-hidden="true"></div><div class="page-hero-scrim"></div>');

    var inner = hero.querySelector(".container") || hero;
    var h1 = inner.querySelector("h1");
    var title = hero.getAttribute("data-crumb") || (h1 ? h1.textContent.replace(/\s+/g, " ").trim() : "");
    if (h1) h1.insertAdjacentHTML("beforebegin", '<p class="page-hero-eyebrow">' + cfg.eyebrow + '</p>');

    var crumbs = [{ name: "홈", href: "index.html" }];
    if (cfg.parent) crumbs.push(cfg.parent);
    crumbs.push({ name: title });
    inner.insertAdjacentHTML("afterbegin", '<nav class="breadcrumb" aria-label="현재 위치">'
      + crumbs.map(function (c) { return c.href ? '<a href="' + c.href + '">' + c.name + '</a>' : '<span aria-current="page">' + c.name + '</span>'; }).join('<i>/</i>')
      + '</nav>');

    /* 경로 구조화 데이터 (구글 검색 결과에 '홈 > 시공사례' 표시) */
    var ld = document.createElement("script");
    ld.type = "application/ld+json";
    ld.text = JSON.stringify({
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": crumbs.map(function (c, i) {
        return { "@type": "ListItem", "position": i + 1, "name": c.name,
                 "item": C.siteUrl + "/" + (c.href ? c.href.replace("index.html", "") : location.pathname.split("/").pop()) };
      })
    });
    document.head.appendChild(ld);
  });

  /* 4) 현재 페이지 메뉴 강조 */
  var current = location.pathname.split("/").pop() || "index.html";
  var section = { "case": "gallery.html", area: "areas.html", post: "blog.html" };
  var heroKey = (document.querySelector(".page-hero[data-hero]") || {}).getAttribute
    ? document.querySelector(".page-hero[data-hero]").getAttribute("data-hero") : "";
  document.querySelectorAll(".main-nav a, .footer-col a").forEach(function (a) {
    var href = a.getAttribute("href");
    if (href === current || href === section[heroKey]) a.classList.add("is-current");
  });
})();
