/* ============================================
   결앤빛 커튼&블라인드 - 사이트 설정
   여기만 수정하면 모든 페이지에 자동 반영됩니다!
   ============================================ */

const SITE_CONFIG = {
    // 🌐 사이트 주소 (도메인이 정해지면 여기와 HTML의 gyeolnbit.co.kr 을 일괄 바꾸기)
    siteUrl: "https://gyeolnbit.co.kr",

    // 📞 연락처
    phone: "010-8353-5979",
    email: "wh597979@naver.com",

    // 💬 카카오 채널
    kakaoUrl: "https://pf.kakao.com/_PJixjX",

    // 📍 네이버 플레이스 (리뷰 보기 버튼에 연결, 없으면 "" 로 두면 버튼이 숨겨짐)
    naverPlaceUrl: "",

    // 📸 인스타그램 / 블로그 (없으면 "")
    instagramUrl: "",
    blogUrl: "",

    // 📋 Formspree (문의 폼) - 드리움과 같은 폼, 메일 제목으로 구분
    formspreeId: "xlgvaknw",
    formSubject: "[결앤빛] 새 견적 문의가 도착했습니다",

    // 🏢 회사 정보
    companyName: "결앤빛 커튼&블라인드",
    companyNameEn: "GYEOL & BIT",
    legalName: "드리움커튼블라인드",     // 사업자등록증의 상호 (드리움과 같은 사업자로 운영)
    ceo: "조규찬",
    bizNumber: "210-42-66972",  // 사업자등록번호
    address: "서울 · 경기 · 인천 방문 시공",

    // ⏰ 영업 시간
    businessHours: "연중무휴 24시 상담"
};

// 페이지가 로드되면 자동으로 모든 링크에 설정값 적용
document.addEventListener('DOMContentLoaded', () => {

    // 1. 전화번호 링크 자동 설정
    document.querySelectorAll('a[href^="tel:"], [data-link="phone"]').forEach(el => {
        el.href = "tel:" + SITE_CONFIG.phone;
    });

    // 2. 이메일 링크 자동 설정
    document.querySelectorAll('a[href^="mailto:"], [data-link="email"]').forEach(el => {
        el.href = "mailto:" + SITE_CONFIG.email;
    });

    // 3. 카카오 채널 링크 자동 설정
    document.querySelectorAll('.btn-kakao, [data-link="kakao"]').forEach(el => {
        el.href = SITE_CONFIG.kakaoUrl;
        el.target = "_blank";
        el.rel = "noopener";
    });

    // 4. 네이버 플레이스 링크 (주소가 비어 있으면 버튼 숨김)
    document.querySelectorAll('[data-link="naver"]').forEach(el => {
        if (SITE_CONFIG.naverPlaceUrl) {
            el.href = SITE_CONFIG.naverPlaceUrl;
            el.target = "_blank";
            el.rel = "noopener";
        } else {
            el.style.display = "none";
        }
    });

    // 5. Formspree 폼 자동 설정 (inquiry.html에서만 작동)
    const inquiryForm = document.querySelector('.inquiry-form');
    if (inquiryForm) {
        inquiryForm.action = `https://formspree.io/f/${SITE_CONFIG.formspreeId}`;
        const next = inquiryForm.querySelector('input[name="_next"]');
        if (next) next.value = SITE_CONFIG.siteUrl + "/thanks.html";
        const subject = inquiryForm.querySelector('input[name="_subject"]');
        if (subject) subject.value = SITE_CONFIG.formSubject;
    }

    // 6. 텍스트로 표시되는 전화번호 / 이메일 자동 업데이트
    document.querySelectorAll('[data-text="phone"]').forEach(el => {
        el.textContent = SITE_CONFIG.phone;
    });
    document.querySelectorAll('[data-text="email"]').forEach(el => {
        el.textContent = SITE_CONFIG.email;
    });
});
