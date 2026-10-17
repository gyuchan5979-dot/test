from common import *

# 사진에서 확인되는 시공 내용만 적었습니다. 지역 · 평수 · 고객 요청사항은 확인되면 추가하세요.
STORIES = {
    "01": dict(
        about="거실 통창에 베이지 겉커튼과 화이트 쉬폰 속커튼을 이중 레일로 시공했습니다. 낮에는 쉬폰만 쳐서 빛을 부드럽게 들이고, 저녁에는 겉커튼을 닫아 아늑하게 쓰는 구성입니다.",
        point=["천장 레일로 커튼이 천장부터 떨어져 층고가 높아 보이게", "벽 끝까지 이어지는 레일로 커튼을 열었을 때 창을 가리지 않게", "원목 바닥과 어울리는 베이지 톤 겉커튼"]),
    "02": dict(
        about="커튼이 없던 거실 창에 그레이 겉커튼과 화이트 쉬폰을 이중 레일로 시공했습니다. 시공 전후 사진을 나란히 보면 같은 창이 얼마나 달라지는지 확인할 수 있어요.",
        point=["그레이 겉커튼으로 밝은 바닥 · 가구와 대비되는 차분한 톤", "쉬폰을 함께 걸어 낮에도 시선은 가리고 빛은 들이게", "창 양옆 벽까지 넉넉하게 덮는 폭"]),
    "40": dict(
        about="동작구 롯데캐슬에듀포레 거실의 기존 콤비블라인드를 걷어내고 화사한 화이트 쉬폰 커튼으로 바꿨습니다. 기존 블라인드는 저희가 직접 철거했어요. 너무 얇기만 한 쉬폰은 밤에 비칠 수 있어서, 시선을 적당히 가려 주는 쉬폰으로 골라 낮엔 밝게, 사생활은 지켜지게 했습니다. 주름이 일정하게 떨어져 창 앞이 한 폭의 그림처럼 단정해졌어요.",
        point=["기존 콤비블라인드 철거부터 커튼 시공까지 한 번에", "시선을 적당히 가려 주는 쉬폰으로 낮 채광과 사생활을 함께", "천장 레일에서 바닥까지 일정하게 떨어지는 주름"]),
    "39": dict(
        about="목동 범신하이빌 집 전체를 화이트 톤 하나로 맞춰 시공했습니다. 같은 화이트여도 공간마다 제품은 다르게 골랐어요. 거실은 알루미늄 블라인드로 넓은 통창을 깔끔하고 관리 쉽게, 방 두 곳은 화이트 우드블라인드로 따뜻한 질감을 더해 포근하게, 세탁실 쪽 방은 아이스화이트 콤비블라인드로 빛은 은은하게 들이고 시선은 가리게 했습니다. 색은 하나로 맞추고 제품은 공간에 맞게, 그래서 어느 문을 열어도 하나로 이어지는 집이 됐어요.",
        point=["집 전체를 화이트 한 가지 톤으로 통일", "거실 통창은 관리 쉬운 알루미늄, 방은 질감 있는 우드", "세탁실 쪽 방은 콤비로 채광과 시선 차단을 함께"]),
    "38": dict(
        about="성남 수내동 빌라의 방 두 곳에 데님블루 암막커튼을 시공했습니다. 두 방 모두 샷시 사이즈에 딱 맞춰 맞춤 제작하고, 창틀 라인에 정확히 떨어지게 재단해 빛샘은 줄이고 보기에도 군더더기 없게 마감했어요. 흔한 무채색 대신 진한 데님블루로 은은한 색감을 더해, 암막이라 빛은 잡아 주면서도 하얀 방에 차분한 포인트가 됩니다.",
        point=["샷시 사이즈에 맞춘 맞춤 제작 · 창틀 라인에 맞춘 기장", "천장 몰딩 바로 아래 레일로 위쪽 빛샘 줄이기", "무채색 대신 데님블루로 하얀 방에 포인트"]),
    "37": dict(
        about="분당 매화마을 주공3단지 거실과 안방을 공간마다 다르게 시공했습니다. 거실은 하얀 도톰쉬폰으로 햇살은 화사하게 들이면서, 도톰한 원단이라 밖에서의 시선은 가려 줍니다. 안방은 샤넬 암막커튼 한 장으로 복도 쪽 시선을 자연스럽게 가리고 포근한 수면 공간으로 만들었어요. 같은 집이어도 공간마다 쓰임이 다르니, 거기에 맞춰 원단도 방식도 다르게 골랐습니다.",
        point=["거실 간접조명 라인 안쪽에 레일을 숨겨 조명과 커튼이 함께 떨어지게", "도톰쉬폰으로 낮에도 바깥 시선 차단 · 채광은 그대로", "안방은 창보다 넓게 덮는 암막 한 장으로 복도 쪽 시선까지"]),
    "36": dict(
        about="성동구 강변건영아파트 침실 두 곳에 그레이 샤넬 암막커튼을 시공했습니다. 창으로 들어오는 빛 때문에 잠을 설치신다는 고객님 이야기를 듣고, 두 방 모두 '잘 쉬는 공간'을 만드는 데 집중했어요. 빛을 확실히 잡아 아침에도 어둡고 아늑하게, 차분한 톤으로 방에 들어서면 마음이 가라앉는 분위기로 맞췄습니다. 샤넬 원단 특유의 은은한 결 덕분에 단색인데도 밋밋하지 않아요.",
        point=["침실 두 곳 모두 같은 원단 · 톤으로 통일", "벽 끝에서 끝까지 덮는 폭으로 창 양옆 빛샘 줄이기", "천장 몰딩 바로 아래 레일로 위쪽 빛샘 줄이기"]),
    "03": dict(
        about="안양 평촌 한가람신라아파트 안방에 블루그레이 샤넬 암막커튼을 나비주름으로 시공했습니다. 추석 연휴 기간에 실측부터 시공까지 진행한 현장이에요. 차분한 블루 톤이 흰 벽과 침구 사이에서 방을 한결 아늑하게 잡아 주고, 샤넬 원단 특유의 결이 빛에 따라 은은하게 살아나 단색 커튼인데도 밋밋하지 않습니다.",
        point=["나비주름으로 여닫을 때마다 주름이 단정하게 떨어지게", "천장 가까이 레일을 달아 위쪽 빛샘 줄이기", "벽 끝에서 끝까지 덮는 폭으로 창 양옆까지 가리기"]),
    "04": dict(
        about="벽돌 벽과 높은 창이 있는 매장에 화이트 쉬폰 커튼을 시공했습니다. 바깥 풍경과 햇빛은 살리면서 손님 자리로 들어오는 직사광선만 부드럽게 걸러 줍니다.",
        point=["층고가 높은 창 길이에 맞춘 긴 기장", "벽돌 · 원목 인테리어와 어울리는 가벼운 화이트 원단", "창마다 나누어 달아 자리별로 여닫기 쉽게"]),
    "05": dict(
        about="넓은 거실 창 전체에 화이트 쉬폰 커튼을 시공했습니다. 창을 가득 채운 쉬폰이 빛을 고르게 퍼뜨려 공간 전체를 밝고 부드럽게 만들어 줍니다.",
        point=["창 전체 폭을 덮는 넉넉한 원단 양", "바닥에 가깝게 맞춘 기장으로 깔끔한 마감", "천장 레일로 커튼이 위에서부터 떨어지게"]),
    "06": dict(
        about="주방 창에 허니콤 블라인드를 시공했습니다. 위에서 내리고 아래에서 올리는 상하 개폐 방식이라, 윗부분만 내려 시선은 가리고 아래로는 바깥 풍경을 볼 수 있습니다.",
        point=["창틀 안쪽에 맞춘 깔끔한 설치", "벌집 구조 공기층으로 창가 냉기 · 열기 완화", "물기와 기름이 닿는 주방에 관리 쉬운 원단"]),
    "07": dict(
        about="사무실 회의실 전면창에 우드 블라인드를 시공했습니다. 슬랫 각도를 돌려 회의 중 화면 반사를 줄이고, 필요할 때는 빛을 들일 수 있습니다.",
        point=["여러 개로 나누어 창 구간마다 따로 조절", "회의실 가구 톤과 맞춘 우드 컬러", "슬랫 각도로 빛의 양과 방향 조절"]),
    "08": dict(
        about="사무실 전면창에 선스크린 롤스크린을 시공했습니다. 내려도 바깥 풍경이 비쳐 보여 개방감은 유지하면서, 모니터 눈부심과 자외선을 줄여 줍니다.",
        point=["창 구간마다 나누어 단 롤스크린", "바깥이 비치는 선스크린 원단", "높이를 따로 조절해 자리별로 빛 관리"]),
    "09": dict(
        about="거실 통창에 오크 톤 우드 블라인드를 시공했습니다. 슬랫 사이로 들어오는 빛과 그림자가 흰 소파 · 밝은 바닥과 어우러져 따뜻한 분위기를 만듭니다.",
        point=["통창을 여러 개로 나누어 조작이 쉽게", "옆 작은 창까지 같은 제품으로 통일감", "슬랫 각도로 빛 조절"]),
}

PT = {
    "겉커튼": ["낮에는 쉬폰, 저녁에는 겉커튼으로 바꿔 쓰는 이중 레일", "천장 레일로 커튼이 위에서부터 떨어져 층고가 높아 보이게", "벽 끝까지 이어지는 레일로 열었을 때 창을 가리지 않게"],
    "쉬폰": ["빛은 들이고 바깥 시선은 흐리게 하는 얇은 원단", "창 전체 폭을 덮는 넉넉한 원단 양", "바닥에 가깝게 맞춘 기장으로 깔끔한 마감"],
    "암막": ["빛을 막아 주는 차광 원단", "주름이 일정하게 떨어지는 마감", "레일 위치와 폭을 넉넉하게 잡아 빛샘 줄이기"],
    "커튼": ["공간 분위기에 맞춘 원단 색", "천장 가까이 단 레일", "주름이 일정하게 떨어지는 마감"],
    "롤스크린": ["군더더기 없는 일자 라인", "창 구간마다 나누어 높이를 따로 조절", "원단 종류(일반 · 암막 · 선스크린)를 공간에 맞게 선택"],
    "허니콤": ["벌집 구조 공기층으로 창가 냉기 · 열기 완화", "부드럽게 퍼지는 빛", "창 크기에 맞춘 깔끔한 설치"],
    "콤비": ["줄 하나로 채광을 단계적으로 조절", "창 구간마다 나누어 조작이 쉽게", "깔끔한 일자 라인"],
    "우드": ["슬랫 각도로 빛의 양과 방향 조절", "공간 톤에 맞춘 우드 컬러", "창 크기에 맞춘 깔끔한 설치"],
    "알루미늄": ["얇은 슬랫으로 가볍고 깔끔한 인상", "슬랫 각도로 빛 조절", "넓은 창을 여러 개로 나누어 조작이 쉽게"],
}
ABOUT = {
    "10": "거실 창에 그레이 겉커튼과 화이트 쉬폰을 이중 레일로 시공했습니다. 겉커튼을 양옆으로 열면 쉬폰을 통해 들어오는 빛이 공간을 부드럽게 채웁니다.",
    "11": "드레스룸 창에 린넨 질감 롤스크린을 시공했습니다. 옷이 햇빛에 바래지 않도록 빛을 걸러 주면서 방은 밝게 유지합니다.",
    "12": "방 창 전체에 그레이 암막 커튼을 시공했습니다. 빛을 막아 화면을 보거나 쉬는 공간으로 쓰기 좋게 구성했습니다.",
    "13": "방의 두 창에 화이트 롤스크린을 하나씩 나눠 달았습니다. 창마다 따로 올리고 내릴 수 있어 필요한 쪽만 열 수 있습니다.",
    "14": "거실 창에 화이트 쉬폰 커튼을 시공했습니다. 펜던트 조명과 밝은 원목 톤 사이에서 쉬폰이 빛을 부드럽게 퍼뜨립니다.",
    "15": "산이 보이는 거실 창에 화이트 쉬폰 커튼을 시공했습니다. 베란다 문 쪽은 열어 두고 나머지 창을 가려 조망과 채광을 함께 살렸습니다.",
    "16": "세탁실 창에 허니콤 블라인드를 시공했습니다. 바깥 시선을 가리면서 창가의 냉기와 열기를 줄여 줍니다.",
    "17": "거실 창에 린넨 질감 롤스크린을 시공했습니다. 내려도 은은하게 빛이 비쳐 창가 테이블 공간을 밝고 아늑하게 만들어 줍니다.",
    "18": "아이방 창에 암막 롤스크린을 시공했습니다. 낮잠과 밤잠 시간에 방을 어둡게 만들어 주는 구성입니다.",
    "19": dict(
        about="구로구 개봉동 현대1차아파트에 아이보리 알루미늄 블라인드를 전체 시공했습니다. 오래 쓰던 커튼은 저희가 직접 철거해 드리고, 베란다 작은 창부터 이어지는 거실 통창까지 창마다 샤시 크기에 딱 맞춰 달았어요. 알루미늄 블라인드는 물기와 습기에 강해 베란다와 거실처럼 자주 여닫는 공간에 특히 잘 맞습니다.",
        point=["기존 커튼 철거부터 시공까지 한 번에", "샤시 크기에 맞춰 창마다 나누어 제작 · 따로 여닫기", "물기 · 습기에 강한 알루미늄 슬랫으로 베란다까지 같은 톤"]),
    "20": "사무실 대형 창에 콤비 블라인드를 시공했습니다. 모니터 쪽으로 들어오는 빛을 줄 하나로 조절할 수 있습니다.",
    "21": "입주 전 빈 사무실에 콤비 블라인드를 시공했습니다. 가구를 들이기 전에 창부터 정리해 입주 일정에 맞췄습니다.",
    "22": "햇빛이 강하게 드는 베란다 창에 콤비 블라인드를 시공했습니다. 바깥 풍경은 비쳐 보이면서 직사광선은 줄여 줍니다.",
    "23": "유리 파티션으로 나뉜 확장 공간의 창마다 화이트 콤비 블라인드를 시공했습니다. 같은 제품으로 맞춰 공간이 하나로 이어져 보입니다.",
    "24": "길게 이어진 베란다 창에 콤비 블라인드를 시공했습니다. 구간을 나누어 달아 필요한 곳만 열고 닫을 수 있습니다.",
    "25": "거실 통창에 화이트 블라인드를 시공했습니다. 넓은 창을 깔끔한 일자 라인으로 정리해 거실이 더 넓어 보입니다.",
    "26": "다이닝 공간 창에 화이트 우드 블라인드를 시공했습니다. 원형 펜던트 조명과 어두운 테이블 사이에서 밝은 블라인드가 공간을 환하게 잡아 줍니다.",
    "27": "침실 창에 화이트 우드 블라인드와 커튼을 함께 시공했습니다. 블라인드로 빛을 조절하고 커튼으로 아늑함을 더했습니다.",
    "28": "방 창에 화이트 쉬폰 커튼을 시공했습니다. 바깥 빛이 쉬폰을 지나며 고르게 퍼져 방 전체가 부드럽게 밝아집니다.",
    "29": "방 창에 바닥까지 떨어지는 화이트 쉬폰 커튼을 시공했습니다. 주름이 바닥까지 고르게 이어져 정돈된 인상을 줍니다.",
    "30": "간접조명이 있는 거실 창에 쉬폰 커튼을 시공했습니다. 저녁에는 조명이 쉬폰 주름에 비쳐 분위기 있는 공간이 됩니다.",
    "31": "거실 창에 핑크베이지 겉커튼과 쉬폰을 함께 시공했습니다. 따뜻한 색감의 겉커튼이 간접조명과 어우러집니다.",
    "32": "오디오 라운지의 대형 창에 롤스크린을 시공했습니다. 창 구간마다 나누어 달아 공간 분위기에 맞게 빛을 조절합니다.",
    "33": "도심 상가 건물 창에 그레이 암막 커튼을 시공했습니다. 바깥 간판 불빛과 시선을 막아 실내를 차분하게 만들어 줍니다.",
    "34": "사무실 창에 그레이 롤스크린을 시공했습니다. 바깥 시선을 가리면서 창 아래쪽은 열어 둘 수 있게 높이를 조절할 수 있습니다.",
    "35": "책장이 있는 서재 창에 그레이 커튼을 시공했습니다. 책이 햇빛에 바래지 않도록 빛을 막아 주는 구성입니다.",
}
for k, v in ABOUT.items():
    tag = next(c["tag"] for c in CASES if c["id"] == k)
    key = next((t for t in PT if tag.startswith(t)), "커튼")
    STORIES[k] = v if isinstance(v, dict) else dict(about=v, point=PT[key])

FILTERS = [("all", "전체"), ("curtain", "커튼"), ("blind", "블라인드"), ("commercial", "상업공간")]

def photo_src(cid, i):
    return f"images/cases/case-{cid}.jpg" if i == 0 else f"images/cases/case-{cid}-{i+1}.jpg"

def build():
    cards = "\n".join(case_card(c) for c in CASES)
    filters = "\n".join(f'<button type="button" class="filter-btn{" is-active" if k == "all" else ""}" data-filter="{k}">{v}</button>' for k, v in FILTERS)
    body = f'''
<section class="page-hero" data-hero="gallery">
    <div class="container">
        <h1>시공사례</h1>
        <p class="lead">결앤빛이 직접 시공하고 촬영한 실제 현장입니다.<br>비슷한 공간을 찾아 우리 집을 미리 그려 보세요.</p>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="filter-bar" role="group" aria-label="시공사례 분류">
{textwrap.indent(filters, "            ")}
        </div>

        <!-- ===== 사례 카드 =====
             새 사례 추가 방법
             1) case-09.html 을 복사해 case-10.html 로 저장하고 내용 수정
             2) 사진을 images/cases/case-10.jpg (+ case-10-2.jpg ...) 로 업로드
             3) 아래 카드 하나를 복사해 맨 위에 붙이고 번호 · 문구 수정
             data-cat: curtain(커튼) blind(블라인드) commercial(상업공간) — 여러 개는 띄어쓰기
        -->
        <div class="case-grid is-even">
{textwrap.indent(cards, "            ")}
        </div>
    </div>
</section>
'''
    ld = [{
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "결앤빛 시공사례",
        "url": SITE + "/gallery.html",
        "hasPart": [{"@type": "CreativeWork", "name": c["title"], "url": f'{SITE}/case-{c["id"]}.html'} for c in CASES]
    }]
    page("gallery.html",
         "시공사례 | 실제 커튼·블라인드 시공 사진 | 결앤빛",
         "결앤빛이 직접 시공한 커튼·블라인드 실제 사례 모음. 거실 이중 커튼, 침실 암막커튼, 매장 쉬폰커튼, 주방 허니콤블라인드, 사무실 우드블라인드·롤스크린까지.",
         "커튼 시공사례, 블라인드 시공사례, 거실 커튼, 암막커튼 시공, 쉬폰커튼 시공, 허니콤블라인드 시공, 우드블라인드 시공, 사무실 롤스크린",
         body, ld=ld)

    for i, c in enumerate(CASES):
        s = STORIES[c["id"]]
        prev_c = CASES[i - 1] if i > 0 else None
        next_c = CASES[i + 1] if i < len(CASES) - 1 else None
        prod = next((p for p in PRODUCTS if p["name"].startswith(c["tag"].split()[0])), None)
        points = "\n".join(f"<li>{x}</li>" for x in s["point"])
        figs = "\n".join(
            f'<figure><img src="{photo_src(c["id"], k)}" alt="{c["place"]} {c["tag"]} {cap}" loading="lazy"><figcaption>{cap}</figcaption></figure>'
            for k, cap in enumerate(c["photos"]))
        pager = ""
        pager += (f'<a href="case-{prev_c["id"]}.html"><small>← 이전 사례</small><strong>{prev_c["title"]}</strong></a>' if prev_c else '<a href="gallery.html"><small>←</small><strong>사례 목록</strong></a>')
        pager += (f'<a href="case-{next_c["id"]}.html"><small>다음 사례 →</small><strong>{next_c["title"]}</strong></a>' if next_c else '<a href="gallery.html"><small>→</small><strong>사례 목록</strong></a>')
        prod_link = f"<a href='products.html#{prod['id']}'>{prod['name']} 자세히 보기</a> · " if prod else ""
        body = f'''
<!-- ===== 사례 상세 =====
     사진: {", ".join(photo_src(c["id"], k).split("/")[-1] for k in range(len(c["photos"])))}
     지역 · 평수 · 고객 요청사항을 알고 있다면 공간 정보와 본문에 추가하세요. (예: 공간 → "인천 송도 · 아파트 34평 거실")
-->
<section class="page-hero" data-hero="case" data-hero-img="images/cases/case-{c["id"]}.jpg" data-crumb="{c["place"]} {c["tag"]}">
    <div class="container">
        <h1>{c["title"]}</h1>
        <div class="tag-row">
            <span class="tag">{c["place"]}</span>
            <span class="tag">{c["tag"]}</span>
        </div>
    </div>
</section>

<section class="section">
    <div class="container-narrow">
        <dl class="case-spec">
            <div><dt>공간</dt><dd>{c["place"]}</dd></div>
            <div><dt>제품</dt><dd>{c["products"]}</dd></div>
            <div><dt>{"지역" if c.get("loc") else "사진"}</dt><dd>{c.get("loc") or f'실제 시공 현장 {len(c["photos"])}장'}</dd></div>
            <div><dt>{"시공" if c.get("date") else "상담"}</dt><dd>{c.get("date") or "무료 방문 실측"}</dd></div>
        </dl>

        <article class="prose">
            <h2>시공 내용</h2>
            <p>{s["about"]}</p>

            <div class="case-photos{" is-single" if len(c["photos"]) == 1 else ""}">
{textwrap.indent(figs, "                ")}
            </div>

            <h3>시공 포인트</h3>
            <ul>
{textwrap.indent(points, "                ")}
            </ul>

            <div class="note-box">
                <strong>비슷한 공간이라면</strong>
                이 사례 번호(case-{c["id"]})를 알려주시면 같은 구성으로 상담해 드려요.
                {prod_link}<a href="inquiry.html">무료 방문 견적 신청</a>
            </div>
        </article>

        <nav class="pager" aria-label="다른 사례">
            {pager}
        </nav>
    </div>
</section>
'''
        ld = [{
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": c["title"],
            "description": f'{c["place"]} {c["products"]} 실제 시공 사례',
            "image": f'{SITE}/images/cases/case-{c["id"]}.jpg',
            "author": {"@type": "Organization", "name": BRAND},
            "publisher": {"@type": "Organization", "name": BRAND},
            "about": {"@type": "Service", "serviceType": c["tag"] + " 시공"}
        }]
        tag0 = c["tag"].split()[0]
        if c.get("loc"):
            parts = c["loc"].split()
            if len(parts) == 2: parts = [parts[0], parts[0], parts[1]]
            city = parts[0]; sub = parts[1]; apt = " ".join(parts[2:])
            t = f'{city} {tag0}커튼 시공 | {sub + " " if sub != city else ""}{apt} {c["place"].replace(" · ", "·")} {c["products"].split(" (")[0]} | 결앤빛' if c["cat"].startswith("curtain") else f'{city} {c["tag"]} 시공 | {sub + " " if sub != city else ""}{apt} {c["place"].replace(" · ", "·")} | 결앤빛'
            d = f'{c["loc"]} {c["place"]} {c["products"]} 실제 시공 사례 ({c.get("date","")}). {s["about"][:60]}…'
            kw = (f'{city} 커튼, {sub} 커튼, {apt} 커튼, {city} {tag0}커튼, {c["place"].split()[0]} {tag0}커튼, {", ".join(c["products"].split(" (")[0].split(" + "))}, {city} 블라인드'
                  if c["cat"].startswith("curtain") else
                  f'{city} 블라인드, {sub} 블라인드, {apt} 블라인드, {city} {c["tag"]}, {c["tag"]} 시공, 거실 {c["tag"]}, 베란다 블라인드, {city} 블라인드 시공')
        else:
            t = f'{c["place"]} {c["tag"]} 시공사례 - {c["title"]} | 결앤빛'
            d = f'{c["place"]} {c["products"]} 실제 시공 사례. {s["about"][:70]}…'
            kw = f'{c["place"]} {tag0}, {tag0} 시공, {tag0} 시공사례, {c["place"]} 커튼, {c["place"]} 블라인드, 커튼 시공사례'
        if c.get("kw_extra"): kw += ", " + c["kw_extra"]
        if c.get("kw"): kw = c["kw"]
        kw = ", ".join(dict.fromkeys(k.strip() for k in kw.split(",")))
        page(f'case-{c["id"]}.html', t, d, kw,
             body, og_image=f'images/cases/case-{c["id"]}.jpg', og_type="article", ld=ld)
