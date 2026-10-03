# 결앤빛 커튼&블라인드 홈페이지 관리 가이드

드리움(deurium.co.kr)과 **같은 구조**로 만들었습니다. 파일을 FTP로 그대로 올리면 됩니다.
(이 `README.md` 파일은 업로드하지 않아도 됩니다.)

## 폴더 구조

```
/index.html              메인
/gallery.html            시공사례 목록
/case-01.html ~ 06       시공사례 상세 (사례 1개 = 페이지 1개 → 검색 노출용)
/products.html           제품 안내 (#linen #chiffon #blackout #combi #wood #honeycomb #roll #motor)
/areas.html              시공 지역 목록
/area-xxx.html           지역 페이지 (강남·서초·송파·마포·분당·판교·일산·송도)
/blog.html, blog-N-xxx.html   매거진 (블로그)
/about.html  /faq.html  /inquiry.html  /thanks.html
/css/reset.css, style.css
/js/config.js            ★ 연락처 · 카톡 · 폼 설정
/js/includes.js          ★ 헤더 · 히어로 · 하단 상담영역 · 푸터 · 플로팅 버튼
/js/main.js              화면 동작 (메뉴, 슬라이드, 필터)
/images/...              사진
/sitemap.xml  /robots.txt
```

## 어디를 고치면 되나요?

| 바꾸고 싶은 것 | 파일 |
|---|---|
| 전화번호, 이메일, 카톡 주소, 문의 폼, 사업자 정보 | `js/config.js` |
| 상단 메뉴, 하단 푸터, 플로팅 버튼 | `js/includes.js` |
| 메인 히어로 슬라이드 사진·문구 | `js/includes.js` → `HOME_HERO_SLIDES` |
| 서브 페이지 히어로 배경 사진 | `js/includes.js` → `PAGE_HEROES` |
| 푸터 위 "상담" 영역 문구 | `js/includes.js` → `ctaHTML` |
| 새 지역 페이지 연결 | `js/includes.js` → `COMPLETED_AREAS` |
| 색상 · 글꼴 | `css/style.css` 맨 위 `:root` |

> 각 페이지의 **제목(h1)과 본문은 HTML에 그대로** 들어 있습니다. 검색엔진(특히 네이버)이
> JS로 넣은 글은 잘 못 읽기 때문에, 반복되는 틀(헤더·푸터·히어로 배경·경로)만 JS로 관리합니다.

## 사진 교체 (가장 먼저 할 일)

지금 들어 있는 회색 사진은 **자리표시용**이고, 사진 위에 파일명과 권장 크기가 적혀 있습니다.
**같은 파일명으로 FTP에 덮어쓰기**하면 바로 바뀝니다. (용량은 장당 300KB 이하 권장)

| 폴더 | 파일 | 권장 크기 |
|---|---|---|
| `images/hero/` | hero-01~03.jpg (메인 슬라이드) | 1920×1080 |
| `images/hero/` | hero-gallery / products / areas / blog / about / faq / inquiry / cta .jpg | 1920×1080 |
| `images/cases/` | case-01.jpg (대표), case-01-2.jpg, case-01-3.jpg … case-06 | 1600×1200 |
| `images/products/` | linen, chiffon, blackout, combi, wood, honeycomb, roll, motor .jpg | 900×1200 (세로) |
| `images/before-after/` | before.jpg, after.jpg (**같은 위치·구도**에서 촬영) | 1600×900 |
| `images/about/` | about-01.jpg, about-02.jpg | 1000×1250 (세로) |
| `images/blog/` | blog-1~3.jpg | 1200×800 |
| `images/` | og-image.jpg (카톡·SNS 공유 미리보기) | 1200×630 |

## ⚠️ 예시 문구 교체

- **시공사례 6개(case-01~06)** 의 지역 · 평수 · 내용은 **예시**입니다. 실제 현장 내용으로 바꿔 주세요.
  (`gallery.html` 카드, `index.html` 최근 사례 카드, 각 `case-0N.html` 모두)
- **고객 후기** 3칸은 "예시" 표시가 붙은 자리표시 카드입니다. `index.html`에서 실제 후기 문장 · 고객명 · 지역 · 제품으로 바꾸고 `<span class="sample-tag">예시</span>` 줄을 지우세요.
  지어낸 후기는 표시광고법 위반이 될 수 있으니 실제 후기만 올려 주세요.
- 네이버 플레이스가 있으면 `config.js`의 `naverPlaceUrl`에 주소를 넣으면 "네이버 리뷰 보기" 버튼이 나타납니다.

## 새 페이지 추가하는 법

**시공사례 추가**
1. `case-06.html`을 복사해 `case-07.html`로 저장 → 제목·지역·본문·사진 경로 수정
2. 사진을 `images/cases/case-07.jpg`, `case-07-2.jpg`, `case-07-3.jpg`로 업로드
3. `gallery.html`의 카드 하나를 복사해 맨 위에 붙이고 번호·문구 수정 (`data-cat` 분류 확인)
4. `sitemap.xml`에 주소 한 줄 추가

**지역 페이지 추가**
1. `area-gangnam.html`을 복사해 `area-gwangjin.html` 등으로 저장 → 지역명·동 목록·소개 글 수정
   (지역마다 소개 글을 **다르게** 써야 검색엔진이 중복 페이지로 보지 않습니다)
2. `js/includes.js`의 `COMPLETED_AREAS`에 `"광진": "area-gwangjin.html",` 추가
3. `areas.html`에서 해당 지역 `<span>`을 링크로 바꾸기
4. `sitemap.xml`에 추가

**매거진 글 추가**: `blog-1-curtain-length.html` 복사 → 내용 수정 → `blog.html` 카드 추가 → `sitemap.xml` 추가

## 도메인 정하면

현재 임시 주소 `https://gyeolnbit.co.kr` 이 들어 있습니다. 도메인이 정해지면
FTP 프로그램이나 에디터(VS Code 등)의 **전체 찾아 바꾸기**로 모든 파일에서 `gyeolnbit.co.kr` 을 새 도메인으로 바꿔 주세요.
(`js/config.js`, 모든 `.html`, `sitemap.xml`, `robots.txt`)

## 검색 노출 (SEO) 설정 순서

1. **네이버 서치어드바이저** (searchadvisor.naver.com) → 사이트 등록 → HTML 태그 인증
   → 받은 `<meta name="naver-site-verification" ...>` 를 `index.html` 의 `<head>` 주석 자리에 붙여넣기
2. 네이버 서치어드바이저 → 요청 → **사이트맵 제출**: `https://도메인/sitemap.xml`
3. **구글 서치콘솔** (search.google.com/search-console) 도 같은 방식으로 인증 + 사이트맵 제출
4. 새 페이지를 추가할 때마다 `sitemap.xml` 갱신 → 서치어드바이저에서 "웹 페이지 수집 요청"

이미 들어 있는 것: 페이지별 title · description · keywords, canonical, OG(공유 미리보기), 
구조화 데이터(업체 정보 · FAQ · 게시글 · 경로), sitemap.xml, robots.txt, 모바일 대응.

**드리움과 함께 운영할 때 주의**: 같은 업체의 두 사이트가 비슷한 문장을 쓰면 네이버가 유사 문서로 보고
한쪽만 노출할 수 있습니다. 결앤빛의 문구는 드리움과 겹치지 않게 새로 썼으니, 앞으로 글을 추가할 때도
드리움 글을 복사하지 말고 **새로 써 주세요.** 시공사례도 드리움에 올린 사진과 다른 사진을 쓰는 것이 좋습니다.
