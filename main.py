import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 설정
st.set_page_config(
    page_title="MBTI 단짝 포켓몬 찾기",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. 커스텀 CSS (따뜻한 크림/노란색 톤, 큰 글씨, 가독성 높은 스타일)
st.markdown("""
<style>
    /* 전체 배경색 - 따뜻하고 포근한 크림톤 */
    .stApp {
        background-color: #FFFDF0;
        color: #3E2723;
        font-family: 'Pretendard', 'Noto Sans KR', 'Segoe UI', sans-serif;
    }

    /* 메인 타이틀 디자인 */
    .main-title {
        font-size: 2.3rem !important;
        font-weight: 800;
        color: #5D4037;
        text-align: center;
        margin-top: 15px;
        margin-bottom: 8px;
    }

    .sub-title {
        font-size: 1.2rem !important;
        color: #8D6E63;
        text-align: center;
        margin-bottom: 25px;
        line-height: 1.5;
    }

    /* 결과 카드 컨테이너 */
    .pokemon-card {
        background-color: #FFF8E7;
        border: 3px solid #FFE082;
        border-radius: 24px;
        padding: 30px 20px;
        margin-top: 20px;
        margin-bottom: 25px;
        box-shadow: 0 8px 20px rgba(210, 180, 140, 0.2);
        text-align: center;
    }

    /* 포켓몬 이름 */
    .pokemon-name {
        font-size: 2.2rem;
        font-weight: 800;
        color: #4E342E;
        margin-top: 15px;
        margin-bottom: 8px;
    }

    /* 포켓몬 타입 뱃지 */
    .pokemon-type-badge {
        display: inline-block;
        background-color: #FFE082;
        color: #4E342E;
        font-weight: 700;
        font-size: 1.15rem;
        padding: 6px 18px;
        border-radius: 20px;
        margin-bottom: 15px;
    }

    /* 특징 & 이유 정보 상자 */
    .info-box {
        background-color: #FFFFFF;
        border-radius: 16px;
        padding: 18px 22px;
        margin-top: 14px;
        text-align: left;
        border: 2px solid #FFF3E0;
    }

    .info-header {
        font-size: 1.25rem;
        font-weight: 700;
        color: #6D4C41;
        margin-bottom: 6px;
    }

    .info-text {
        font-size: 1.15rem;
        color: #3E2723;
        line-height: 1.65;
        word-break: keep-all;
    }

    /* 드롭다운 라벨 크기 확대 */
    label[data-testid="stWidgetLabel"] {
        font-size: 1.25rem !important;
        font-weight: 700 !important;
        color: #4E342E !important;
    }

    /* 버튼 스타일 정의 */
    div.stButton > button {
        background-color: #FFB74D !important;
        color: #3E2723 !important;
        font-size: 1.3rem !important;
        font-weight: 800 !important;
        border-radius: 16px !important;
        padding: 12px 24px !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(255, 183, 77, 0.4) !important;
        width: 100% !important;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        background-color: #FFA726 !important;
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)


# 3. 16가지 MBTI별 단짝 포켓몬 데이터 세트
POKEMON_MBTI_DATA = {
    "INTJ": {
        "name_kr": "뮤츠",
        "name_en": "Mewtwo",
        "type": "🔮 에스퍼",
        "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
        "feature": "깊은 사고력과 압도적인 통찰력을 지닌 전설의 포켓몬",
        "reason": "전략적이고 독립적인 INTJ의 뛰어난 지성과 사색하는 태도를 누구보다 깊이 이해합니다. 복잡한 세상 속에서 거추장스러운 말 없이도 깊은 지적 교감을 나눌 수 있는 최고의 인생 파트너입니다."
    },
    "INTP": {
        "name_kr": "메타그로스",
        "name_en": "Metagross",
        "type": "⚙️ 강철 / 🔮 에스퍼",
        "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/376.png",
        "feature": "슈퍼컴퓨터보다 빠른 연산 능력과 호기심을 가진 지능파 포켓몬",
        "reason": "논
