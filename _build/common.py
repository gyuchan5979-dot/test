import json, os, textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://gyeolnbit.co.kr"
BRAND = "결앤빛 커튼&블라인드"
PHONE = "010-8353-5979"
KAKAO = "https://pf.kakao.com/_PJixjX"

def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;")

def jsonld(obj):
    return ('    <script type="application/ld+json">\n'
            + textwrap.indent(json.dumps(obj, ensure_ascii=False, indent=4), "    ")
            + "\n    </script>\n")

def page(filename, title, desc, keywords, body, og_image="images/og-image.jpg",
         og_type="website", ld=None, extra_head="", cta=True):
    url = SITE + "/" + ("" if filename == "index.html" else filename)
    lds = "".join(jsonld(x) for x in (ld or []))
    html = f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- SEO 메타태그 -->
    <title>{esc(title)}</title>
    <meta name="description" content="{esc(desc)}">
    <meta name="keywords" content="{esc(keywords)}">
    <link rel="canonical" href="{url}">
    <meta property="og:type" content="{og_type}">
    <meta property="og:site_name" content="{esc(BRAND)}">
    <meta property="og:title" content="{esc(title)}">
    <meta property="og:description" content="{esc(desc)}">
    <meta property="og:image" content="{SITE}/{og_image}">
    <meta property="og:url" content="{url}">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="icon" href="images/favicon.svg" type="image/svg+xml">
{extra_head}{lds}
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;500;600&display=swap">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.css">
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
    <script>document.documentElement.classList.add('js');</script>
</head>
<body>

    <!-- 공통 헤더 (includes.js가 채움) -->
    <div id="site-header"></div>

    <main>
{textwrap.indent(textwrap.dedent(body).strip(), "    ")}
    </main>
{"""
    <!-- 하단 상담 섹션 (includes.js가 채움) -->
    <div id="site-cta"></div>
""" if cta else ""}
    <!-- 공통 푸터 (includes.js가 채움) -->
    <div id="site-footer"></div>

    <script src="js/config.js"></script>
    <script src="js/includes.js"></script>
    <script src="js/main.js"></script>
</body>
</html>
'''
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    return filename

# ---------- 공통 데이터 ----------

# 실제 시공 사진 기준 사례 (지역 · 평수는 확인되면 place 에 추가)
CASES = [
    dict(id="01", cat="curtain", tag="겉커튼 + 쉬폰", place="거실",
         title="베이지 겉커튼과 쉬폰으로 레이어드한 거실",
         products="베이지 겉커튼 + 화이트 쉬폰(이중 레일)", photos=["시공 후 거실 전체", "겉커튼과 쉬폰 원단 디테일"]),
    dict(id="02", cat="curtain", tag="겉커튼 + 쉬폰", place="거실",
         title="빈 창에서 완성까지, 그레이 겉커튼과 쉬폰 이중 커튼",
         products="그레이 겉커튼 + 화이트 쉬폰(이중 레일)", photos=["시공 후", "시공 전"]),
    dict(id="03", cat="curtain", tag="암막 커튼", place="안방", area="평촌",
         loc="안양 평촌 한가람신라아파트", date="2026년 9월",
         title="안양 한가람신라아파트 안방, 블루그레이 샤넬 암막커튼",
         products="블루그레이 샤넬 암막커튼 (나비주름)", photos=["커튼을 닫은 모습", "커튼을 연 모습"]),
    dict(id="04", cat="curtain commercial", tag="쉬폰 커튼", place="매장",
         title="벽돌 벽 매장의 높은 창, 화이트 쉬폰 커튼",
         products="화이트 쉬폰 커튼", photos=["매장 창가 전체", "높은 창 전면"]),
    dict(id="05", cat="curtain", tag="쉬폰 커튼", place="거실",
         title="넓은 창을 가득 채운 화이트 쉬폰 커튼",
         products="화이트 쉬폰 커튼", photos=["시공 후 거실 전체", "다른 각도", "공간 전체"]),
    dict(id="06", cat="blind", tag="허니콤 블라인드", place="주방",
         title="위는 가리고 아래는 여는 주방 창 허니콤 블라인드",
         products="허니콤 블라인드(상하 개폐)", photos=["윗부분만 내린 모습", "전체를 내린 모습"]),
    dict(id="07", cat="blind commercial", tag="우드 블라인드", place="사무실 회의실",
         title="회의실 전면창을 정리한 우드 블라인드",
         products="우드 블라인드", photos=["회의실 전체", "창가 디테일"]),
    dict(id="08", cat="blind commercial", tag="롤스크린", place="사무실",
         title="바깥 풍경은 살리고 눈부심은 줄인 사무실 롤스크린",
         products="선스크린 롤스크린", photos=["사무실 전면창", "다른 각도"]),
    dict(id="09", cat="blind", tag="우드 블라인드", place="거실",
         title="오크 톤 우드 블라인드로 채운 거실 통창",
         products="우드 블라인드", photos=["시공 후 거실"]),
    dict(id="10", cat="curtain", tag="겉커튼 + 쉬폰", place="거실", title="그레이 겉커튼 사이로 들어오는 쉬폰의 빛", products="그레이 겉커튼 + 화이트 쉬폰(이중 레일)", photos=["시공 후 전체", "쉬폰 원단 디테일"]),
    dict(id="11", cat="blind", tag="롤스크린", place="드레스룸", title="은은하게 빛을 거르는 드레스룸 롤스크린", products="린넨 질감 롤스크린", photos=["정면", "측면"]),
    dict(id="12", cat="curtain", tag="암막 커튼", place="방", title="그레이 암막 커튼으로 차분하게 정리한 방", products="그레이 암막 커튼", photos=["커튼 전체", "세로 디테일", "다른 각도"]),
    dict(id="13", cat="blind", tag="롤스크린", place="방", title="두 창을 나눠 단 화이트 롤스크린", products="화이트 롤스크린", photos=["모두 내린 모습", "한쪽만 올린 모습"]),
    dict(id="14", cat="curtain", tag="쉬폰 커튼", place="거실", title="펜던트 조명 아래 화이트 쉬폰 커튼", products="화이트 쉬폰 커튼", photos=["창가 디테일", "거실 전체"]),
    dict(id="15", cat="curtain", tag="쉬폰 커튼", place="거실", title="산 조망을 살린 밝은 거실 쉬폰 커튼", products="화이트 쉬폰 커튼", photos=["시공 후 거실"]),
    dict(id="16", cat="blind", tag="허니콤 블라인드", place="세탁실", title="세탁실 창 허니콤 블라인드", products="허니콤 블라인드", photos=["시공 후"]),
    dict(id="17", cat="blind", tag="롤스크린", place="거실", title="린넨 질감 롤스크린으로 꾸민 거실 창가", products="린넨 질감 롤스크린", photos=["시공 후 거실"]),
    dict(id="18", cat="blind", tag="롤스크린", place="아이방", title="잠드는 시간을 위한 아이방 암막 롤스크린", products="암막 롤스크린", photos=["롤스크린을 내린 모습"]),
    dict(id="19", cat="blind", tag="알루미늄 블라인드", place="거실 · 베란다", area="구로",
         loc="구로 개봉동 현대1차아파트", date="2026년 10월",
         title="기존 커튼을 걷어내고 거실 통창까지 이어 단 아이보리 알루미늄 블라인드",
         products="아이보리 알루미늄 블라인드 (기존 커튼 철거 포함)", photos=["시공 후 거실 통창", "코너 창과 베란다 문까지", "시공 전 (기존 커튼)"]),
    dict(id="20", cat="blind commercial", tag="콤비 블라인드", place="사무실", title="사무실 대형 창 콤비 블라인드", products="콤비 블라인드", photos=["사무실 창가", "다른 각도"]),
    dict(id="21", cat="blind commercial", tag="콤비 블라인드", place="사무실", title="입주 전 빈 사무실에 맞춘 콤비 블라인드", products="콤비 블라인드", photos=["시공 후"]),
    dict(id="22", cat="blind", tag="콤비 블라인드", place="베란다", title="햇빛 강한 베란다 창 콤비 블라인드", products="콤비 블라인드", photos=["시공 후"]),
    dict(id="23", cat="blind", tag="콤비 블라인드", place="확장 공간", title="유리 파티션 공간까지 이어진 화이트 콤비 블라인드", products="화이트 콤비 블라인드", photos=["공간 전체", "원단 디테일"]),
    dict(id="24", cat="blind", tag="콤비 블라인드", place="베란다", title="길게 이어진 베란다 창 콤비 블라인드", products="콤비 블라인드", photos=["시공 후"]),
    dict(id="25", cat="blind", tag="콤비 블라인드", place="거실", title="거실 통창을 덮은 화이트 블라인드", products="화이트 콤비 블라인드", photos=["시공 후 거실"]),
    dict(id="26", cat="blind", tag="우드 블라인드", place="다이닝", title="원형 조명과 어울린 다이닝 화이트 우드 블라인드", products="화이트 우드 블라인드", photos=["시공 후 다이닝"]),
    dict(id="27", cat="blind", tag="우드 블라인드", place="침실", title="화이트 우드 블라인드와 커튼을 함께 쓴 침실", products="화이트 우드 블라인드 + 커튼", photos=["시공 후 침실"]),
    dict(id="28", cat="curtain", tag="쉬폰 커튼", place="방", title="빛이 고르게 퍼지는 화이트 쉬폰 커튼", products="화이트 쉬폰 커튼", photos=["창 전체", "주름 디테일"]),
    dict(id="29", cat="curtain", tag="쉬폰 커튼", place="방", title="바닥까지 떨어지는 화이트 쉬폰 커튼", products="화이트 쉬폰 커튼", photos=["시공 후"]),
    dict(id="30", cat="curtain", tag="쉬폰 커튼", place="거실", title="간접조명과 어우러진 쉬폰 커튼", products="화이트 쉬폰 커튼", photos=["시공 후 거실"]),
    dict(id="31", cat="curtain", tag="겉커튼 + 쉬폰", place="거실", title="핑크베이지 겉커튼과 쉬폰으로 따뜻해진 거실", products="핑크베이지 겉커튼 + 쉬폰", photos=["시공 후 거실"]),
    dict(id="32", cat="blind commercial", tag="롤스크린", place="라운지", title="오디오 라운지 대형 창 롤스크린", products="롤스크린", photos=["시공 후"]),
    dict(id="33", cat="curtain", tag="암막 커튼", place="상가 공간", title="도심 창가의 그레이 암막 커튼", products="그레이 암막 커튼", photos=["창가 디테일"]),
    dict(id="34", cat="blind commercial", tag="롤스크린", place="사무실", title="사무실 창 그레이 롤스크린", products="그레이 롤스크린", photos=["시공 후"]),
    dict(id="35", cat="curtain", tag="커튼", place="서재", title="책장이 있는 서재의 그레이 커튼", products="그레이 커튼", photos=["시공 후 서재"]),
    dict(id="42", cat="curtain", tag="쉬폰 커튼", place="거실 · 작은방", area="구로",
         loc="구로 구로동 상우아파트", date="2026년 10월",
         kw_extra="구로동 쉬폰커튼, 상우아파트 커튼, 구로동 커튼, 작은방 쉬폰커튼, 커튼 레일 설치",
         title="답답하지 않게, 거실과 작은방에 화이트 쉬폰",
         products="화이트 쉬폰 커튼 (안방 커튼 레일 서비스 설치)", photos=["거실 시공 후", "작은방 시공 후", "작은방 다른 각도", "거실 창가 디테일"]),
    dict(id="41", cat="curtain", tag="쉬폰 커튼", place="거실 · 안방", area="구로",
         loc="구로 대림동 이화우성아파트", date="2026년 10월",
         kw_extra="대림동 쉬폰커튼, 이화우성아파트 커튼, 차르르 쉬폰, 구로 거실커튼, 안방 쉬폰커튼, 재시공 고객",
         title="베란다 콤비에 이어, 거실과 안방은 차르르 쉬폰으로",
         products="화이트 차르르 쉬폰 커튼", photos=["거실 시공 후", "쉬폰 원단 디테일", "안방 시공 후", "시공 전 (안쪽으로 지난번 베란다 외창 콤비)"]),
    dict(id="40", cat="curtain", tag="쉬폰 커튼", place="거실", area="동작",
         loc="동작구 롯데캐슬에듀포레", date="2026년 10월",
         kw_extra="롯데캐슬에듀포레 커튼, 동작구 거실커튼, 사생활보호 커튼, 블라인드 철거 커튼 교체, 콤비블라인드 철거",
         title="기존 콤비블라인드를 걷어내고, 화사한 화이트 쉬폰으로",
         products="화이트 쉬폰 커튼 (기존 콤비블라인드 철거 포함)", photos=["시공 후 거실 전체", "쉬폰 원단 디테일", "시공 전 (기존 콤비블라인드)"]),
    dict(id="39", cat="blind", tag="집 전체 블라인드", place="거실 · 방 3곳", area="양천",
         loc="목동 범신하이빌", date="2026년 10월",
         kw="목동 블라인드, 목동 범신하이빌, 범신하이빌 블라인드, 양천구 블라인드, 목동 알루미늄 블라인드, 목동 우드블라인드, 목동 콤비블라인드, 집 전체 블라인드, 화이트 우드블라인드, 아이스화이트 콤비블라인드",
         title="화이트 하나로 이어지는 집, 공간마다 다른 블라인드",
         products="알루미늄 블라인드(거실) + 화이트 우드블라인드(방 2곳) + 아이스화이트 콤비블라인드", photos=["거실 알루미늄 블라인드", "방 화이트 우드블라인드", "세탁실 쪽 방 아이스화이트 콤비블라인드", "다른 방 화이트 우드블라인드", "거실 시공 전"]),
    dict(id="38", cat="curtain", tag="암막 커튼", place="방 2곳", area="분당",
         loc="분당 수내동 빌라", date="2026년 10월",
         kw_extra="성남 커튼, 성남 암막커튼, 수내동 암막커튼, 데님블루 커튼, 맞춤커튼 제작, 빌라 커튼",
         title="샷시 크기에 딱 맞춘 데님블루 암막커튼, 방 두 곳",
         products="데님블루 암막커튼 (창 길이 맞춤 제작)", photos=["방 1 시공 후", "방 2 시공 후", "다른 각도", "시공 전"]),
    dict(id="37", cat="curtain", tag="쉬폰 커튼", place="거실 · 안방", area="분당",
         loc="분당 매화마을 주공3단지", date="2026년 10월",
         kw_extra="매화마을주공3단지 커튼, 분당 도톰쉬폰, 분당 암막커튼, 안방 암막커튼",
         title="거실은 도톰쉬폰으로 빛을, 안방은 샤넬 암막으로 쉼을",
         products="화이트 도톰쉬폰 + 샤넬 암막커튼", photos=["거실 도톰쉬폰 시공 후", "안방 샤넬 암막커튼 시공 후", "안방 불을 끄고 커튼을 닫은 모습", "거실 시공 전"]),
    dict(id="36", cat="curtain", tag="암막 커튼", place="침실 2곳", area="성동",
         loc="성동구 강변건영아파트", date="2026년 10월",
         title="빛 때문에 잠을 설치던 침실 두 곳, 그레이 샤넬 암막커튼으로",
         products="그레이 샤넬 암막커튼", photos=["침실 1 시공 후", "불을 끄고 커튼을 닫은 모습", "침실 2 시공 후", "시공 전 (침실 1)"]),

]

PRODUCTS = [
    dict(id="linen", alt="겉커튼 시공 사진", name="린넨 커튼", en="LINEN CURTAIN", short="자연스러운 결과 은은한 채광",
         desc="린넨 특유의 굵은 결이 햇빛을 부드럽게 퍼뜨려, 거실 전체를 따뜻한 톤으로 바꿔 줍니다. 결앤빛이 가장 많이 시공하는 커튼으로, 화이트·아이보리·오트밀 계열이 꾸준히 사랑받아요.",
         feature="자연스러운 주름과 질감, 은은한 빛 투과", space="거실, 침실, 통창", care="물세탁 가능 원단과 드라이 전용 원단이 있어 상담 시 안내", pair="쉬폰 속커튼, 전동 레일"),
    dict(id="chiffon", alt="쉬폰 커튼 시공 사진", name="쉬폰 커튼", en="CHIFFON CURTAIN", short="낮에는 가볍게, 밤에는 레이어드",
         desc="얇고 가벼운 쉬폰은 낮 동안 바깥 시선은 흐리게 하고 빛은 그대로 들입니다. 암막이나 린넨과 이중 레일로 함께 다는 경우가 많아요.",
         feature="가볍고 비치는 원단, 바람에 흔들리는 실루엣", space="거실, 침실(이중 커튼의 속커튼)", care="가벼워 세탁과 건조가 쉬움", pair="암막 커튼, 린넨 커튼"),
    dict(id="blackout", alt="암막 커튼 시공 사진", name="암막 커튼", en="BLACKOUT CURTAIN", short="숙면과 홈시어터를 위한 차광",
         desc="빛을 막아 주는 암막 원단은 침실과 아이방에 특히 많이 찾으십니다. 원단만큼 중요한 것이 시공으로, 커튼 길이와 레일 위치를 정확히 잡아야 옆과 위로 새는 빛을 줄일 수 있어요.",
         feature="차광 · 단열 · 소음 완화", space="침실, 아이방, 홈시어터, 서향 창", care="원단에 따라 세탁 방법이 달라 상담 시 안내", pair="쉬폰 커튼(이중 레일)"),
    dict(id="combi", alt="콤비 블라인드 시공 사진", name="콤비 블라인드", en="COMBI BLIND", short="줄 하나로 채광을 조절",
         desc="빛이 통하는 망사 원단과 막는 원단이 번갈아 겹쳐, 줄을 당겨 채광을 단계적으로 조절할 수 있습니다. 깔끔하고 합리적이라 신축 입주 때 가장 많이 선택하세요.",
         feature="채광 조절, 깔끔한 일자 라인, 합리적인 가격", space="거실, 주방, 작은 방", care="먼지떨이·청소기 브러시로 간단히", pair="린넨 커튼(거실 레이어드)"),
    dict(id="wood", alt="우드 블라인드 시공 사진", name="우드 블라인드", en="WOOD BLIND", short="슬랫 사이로 떨어지는 빛과 그림자",
         desc="원목 슬랫의 각도를 돌려 빛의 양과 방향을 섬세하게 조절할 수 있습니다. 서재나 원목 가구가 있는 공간에 잘 어울리며, 햇빛이 만드는 줄무늬 그림자가 매력이에요.",
         feature="슬랫 각도 조절, 원목 질감, 내구성", space="서재, 거실, 카페 · 사무실", care="물기에 약해 욕실·주방 싱크대 앞은 다른 제품 권장", pair="린넨 커튼"),
    dict(id="honeycomb", alt="허니콤 블라인드 시공 사진", name="허니콤 블라인드", en="HONEYCOMB BLIND", short="벌집 구조 공기층으로 단열",
         desc="벌집 모양 단면에 공기층이 생겨 창가 냉기와 열기를 줄여 줍니다. 위에서 내리고 아래에서 올리는 탑다운·바텀업 방식으로 프라이버시와 채광을 동시에 챙길 수 있어요.",
         feature="단열, 부드러운 빛 확산, 상하 개폐 옵션", space="침실, 아이방, 베란다 확장 창", care="가벼운 먼지 털기 위주로 관리", pair="암막 원단 선택 가능"),
    dict(id="roll", alt="롤스크린 시공 사진", name="롤스크린", en="ROLL SCREEN", short="군더더기 없는 가장 단순한 선",
         desc="한 장의 원단을 위아래로 말아 올리는 가장 간결한 방식입니다. 선스크린 원단은 바깥 풍경을 살리면서 자외선과 눈부심을 줄여 사무실·카페에서 많이 씁니다.",
         feature="미니멀한 디자인, 원단 종류 다양(일반·암막·선스크린)", space="주방, 사무실, 카페, 드레스룸", care="원단을 펼친 상태에서 먼지 제거", pair="커튼과 겹쳐 쓰기 좋음"),
    dict(id="motor", alt="높은 창 시공 사진", name="전동 커튼 · 블라인드", en="MOTORIZED", short="높은 창도 리모컨 하나로",
         desc="손이 닿지 않는 복층 창, 무거운 통창 커튼을 리모컨이나 스마트폰으로 여닫습니다. 설치 전 콘센트 위치와 배선 경로를 실측 때 함께 확인해 드려요.",
         feature="리모컨·예약 개폐, 제품에 따라 스마트홈 연동", space="복층 거실, 대형 통창, 상업공간", care="모터 점검은 A/S 기간 내 무상", pair="린넨 · 암막 커튼, 롤스크린"),
]

AREAS = [
    dict(key="강남", file="area-gangnam.html", full="서울 강남구", region="서울",
         dongs=["압구정동","신사동","논현동","청담동","삼성동","대치동","역삼동","도곡동","개포동","일원동","수서동","세곡동"],
         intro="강남구는 고층 아파트의 넓은 거실 통창과 재건축 신축 단지 입주가 많은 지역입니다. 창이 크고 층이 높을수록 햇빛과 시선 관리가 함께 필요해, 린넨과 쉬폰을 이중으로 거는 구성을 많이 추천드려요.",
         tip="재건축 신축 단지는 입주 일정이 몰리는 시기에 실측 예약이 빠르게 찹니다. 입주 3~4주 전에 실측을 잡아 두시면 이사 당일에 맞춰 시공할 수 있어요.",
         picks=["린넨 커튼","쉬폰 커튼","전동 커튼 · 블라인드"], case="01"),
    dict(key="서초", file="area-seocho.html", full="서울 서초구", region="서울",
         dongs=["서초동","잠원동","반포동","방배동","양재동","내곡동"],
         intro="한강변 반포·잠원 일대는 남향 거실에 오후 햇빛이 깊게 들어오는 집이 많습니다. 시야를 살리면서 눈부심만 줄이는 원단 선택이 관건이에요.",
         tip="한강 조망 창은 낮 시간에 커튼을 닫기 아까운 경우가 많아, 바깥이 비치는 쉬폰이나 선스크린 롤스크린을 먼저 보여드립니다.",
         picks=["쉬폰 커튼","롤스크린","린넨 커튼"], case="01"),
    dict(key="송파", file="area-songpa.html", full="서울 송파구", region="서울",
         dongs=["잠실동","신천동","송파동","석촌동","삼전동","가락동","문정동","방이동","오금동","풍납동","거여동","마천동","장지동","위례동"],
         intro="잠실·가락 일대 대단지 아파트와 문정·위례의 신축, 그리고 석촌호수 주변 카페와 매장까지 주거·상업 공간이 고루 섞인 지역입니다.",
         tip="상가와 카페는 영업에 지장이 없도록 마감 후 시공 일정도 가능합니다. 상담 시 영업 시간을 알려주세요.",
         picks=["콤비 블라인드","롤스크린","우드 블라인드"], case="06"),
    dict(key="마포", file="area-mapo.html", full="서울 마포구", region="서울",
         dongs=["아현동","공덕동","도화동","용강동","대흥동","염리동","신수동","서강동","서교동","합정동","망원동","연남동","성산동","상암동"],
         intro="공덕·아현의 신축 아파트, 상암의 오피스와 주거단지, 연남·망원의 주택과 카페까지 창의 형태가 다양한 지역입니다. 작은 창이 여러 개인 집이 많아 블라인드 비중이 높아요.",
         tip="재택근무 공간이나 서재는 모니터 반사를 줄이는 것이 중요해, 슬랫 각도로 빛 방향을 바꿀 수 있는 우드 블라인드를 많이 추천드립니다.",
         picks=["우드 블라인드","롤스크린","콤비 블라인드"], case="03"),
    dict(key="분당", file="area-bundang.html", full="경기 성남시 분당구", region="경기",
         dongs=["정자동","서현동","수내동","야탑동","이매동","금곡동","구미동","분당동","동원동"],
         intro="1기 신도시로 입주한 지 오래된 아파트가 많아, 리모델링이나 이사 후 커튼을 새로 맞추시는 경우가 많습니다. 기존 커튼박스 깊이가 얕은 집도 있어 실측 때 레일 방식을 꼼꼼히 봐야 해요.",
         tip="커튼박스가 좁으면 이중 레일이 들어가지 않을 수 있습니다. 이럴 때는 천장형 레일이나 블라인드 + 커튼 조합으로 해결해 드려요.",
         picks=["암막 커튼","쉬폰 커튼","허니콤 블라인드"], case="02"),
    dict(key="판교", file="area-pangyo.html", full="경기 성남시 판교", region="경기",
         dongs=["판교동","삼평동","백현동","운중동","대장동","하산운동"],
         intro="백현·삼평의 아파트, 운중동 일대 단독주택과 타운하우스, 그리고 테크노밸리의 사무실까지 공간의 규모와 높이가 다양한 지역입니다.",
         tip="단독주택은 창마다 크기와 방향이 달라 방 하나하나 실측이 필요합니다. 방문 시간을 여유 있게 잡아 한 번에 모든 창을 상담해 드려요.",
         picks=["전동 커튼 · 블라인드","린넨 커튼","우드 블라인드"], case="05"),
    dict(key="일산", file="area-ilsan.html", full="경기 고양시 일산", region="경기",
         dongs=["백석동","마두동","장항동","정발산동","풍산동","식사동","주엽동","대화동","탄현동","일산동","덕이동"],
         intro="정발산·마두 일대의 1기 신도시 아파트와 식사·덕이의 신축 단지, 주변 타운하우스까지 고르게 시공하고 있습니다.",
         tip="층고가 높은 타운하우스 거실은 손으로 여닫기 어려워 전동 레일을 많이 선택하십니다. 실측 때 전원 위치를 함께 확인해 드려요.",
         picks=["전동 커튼 · 블라인드","린넨 커튼","콤비 블라인드"], case="05"),
    dict(key="송도", file="area-songdo.html", full="인천 연수구 송도", region="인천",
         dongs=["송도동","연수동","동춘동","옥련동","청학동","선학동"],
         intro="송도국제도시는 고층 신축 아파트와 큰 통창이 특징입니다. 바다와 공원 조망을 살리면서 서향 햇빛을 다스리는 구성이 가장 많이 요청됩니다.",
         tip="신축 입주 시기에는 거실부터 방까지 한 번에 맞추는 경우가 많아, 공간별 제품을 섞어도 톤이 어긋나지 않도록 원단 색을 맞춰 제안드려요.",
         picks=["콤비 블라인드","린넨 커튼","허니콤 블라인드"], case="04"),
]

from areas_more import MORE as _MORE
AREAS += _MORE

POSTS = [
    dict(file="blog-1-curtain-length.html", cat="선택 가이드", date="2026-10-01",
         title="커튼 길이, 바닥에 닿게? 살짝 띄우게?",
         desc="같은 원단도 길이에 따라 분위기와 관리가 달라집니다. 바닥에서 1cm 띄우기, 바닥에 닿게, 끌리게 세 가지 방식의 장단점을 실제 시공 기준으로 정리했어요.",
         kw="커튼 길이, 커튼 기장, 커튼 실측, 커튼 바닥, 거실 커튼 길이, 커튼 재는 법"),
    dict(file="blog-2-blind-by-window.html", cat="선택 가이드", date="2026-10-02",
         title="창 종류별 블라인드 고르는 법 (통창 · 베란다 · 작은 창)",
         desc="통창, 확장 베란다 창, 작은 방 창은 같은 블라인드라도 맞는 제품이 다릅니다. 창 형태별로 실패 없는 블라인드 선택 기준을 알려드려요.",
         kw="블라인드 추천, 콤비블라인드, 우드블라인드, 허니콤블라인드, 롤스크린, 통창 블라인드, 베란다 블라인드"),
    dict(file="blog-3-motorized-curtain.html", cat="시공 노트", date="2026-10-03",
         title="전동 커튼, 설치 전에 꼭 확인할 3가지",
         desc="전동 커튼은 설치 후 바꾸기 어려운 것들이 있습니다. 전원 위치, 레일 길이와 무게, 조작 방식까지 실측 전에 확인하면 좋은 3가지를 정리했어요.",
         kw="전동커튼, 전동커튼 설치, 전동블라인드, 전동레일, 복층 커튼, 통창 커튼"),
]

from posts_more import NEW_POSTS as _NP
for _i, _p in enumerate(POSTS):
    _p.setdefault("img", f"blog/blog-{_i+1}.jpg")
POSTS += _NP
from posts_more2 import NEW_POSTS2 as _NP2
POSTS += _NP2

def case_card(c, wide=False, cls=""):
    return f'''<a href="case-{c["id"]}.html" class="case-card{" wide" if wide else ""}{cls}" data-cat="{c["cat"]}">
    <div class="case-img">
        <img src="images/cases/case-{c["id"]}.jpg" alt="{c["place"]} {c["tag"]} 실제 시공 사진" loading="lazy">
        <span class="case-badge">{c["tag"]}</span>
    </div>
    <div class="case-info">
        <span class="case-loc">{(c["loc"].split()[0] + " " + c["loc"].split()[1] + " · ") if c.get("loc") else ""}{c["place"]} · {c["tag"]}</span>
        <h3>{c["title"]}</h3>
    </div>
</a>'''

def post_card(p, i):
    return f'''<a href="{p["file"]}" class="post-card">
    <div class="post-img"><img src="images/{p["img"]}" alt="{p["title"]}" loading="lazy"></div>
    <span class="post-cat">{p["cat"]}</span>
    <h3>{p["title"]}</h3>
    <p>{p["desc"]}</p>
    <span class="post-date">{p["date"].replace("-", ".")}</span>
</a>'''

def product_by_name(name):
    return next(p for p in PRODUCTS if p["name"] == name)
