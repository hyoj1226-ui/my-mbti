import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 단짝 포켓몬 찾기",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. 커스텀 CSS (따뜻한 크림/노란색 톤, 큰 글씨)
st.markdown("""
<style>
    .stApp {
        background-color: #FFFDF0;
        color: #3E2723;
        font-family: 'Pretendard', 'Noto Sans KR', 'Segoe UI', sans-serif;
    }
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
    .pokemon-name {
        font-size: 2.2rem;
        font-weight: 800;
        color: #4E342E;
        margin-top: 15px;
        margin-bottom: 8px;
    }
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
    label[data-testid="stWidgetLabel"] {
        font-size: 1.25rem !important;
        font-weight: 700 !important;
        color: #4E342E !important;
    }
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
        "reason": "논리적이고 끊임없이 지식을 탐구하는 INTP와 완벽한 호흡을 자랑합니다. 세상의 원리를 함께 분석하고 복잡한 문제를 풀어가는 최고의 지적 탐구 메이트입니다."
    },
    "ENTJ": {
        "name_kr": "리자몽",
        "name_en": "Charizard",
        "type": "🔥 불꽃 / 🕊️ 비행",
        "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
        "feature": "강렬한 카리스마와 꺾이지 않는 과감한 열정을 품은 포켓몬",
        "reason": "목표를 향해 강력한 리더십으로 돌진하는 ENTJ의 대담함과 꼭 들어맞습니다. 어떤 거친 도전과 높은 장벽이 막아서더라도 당당하게 정상을 향해 진격하는 든든한 콤비입니다."
    },
    "ENTP": {
        "name_kr": "팬텀",
        "name_en": "Gengar",
        "type": "👻 고스트 / ☠️ 독",
        "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png",
        "feature": "재치 있는 장난과 창의적인 아이디어가 끊이지 않는 포켓몬",
        "reason": "독창적이고 유쾌한 모험을 즐기는 ENTP와 항상 환상의 짝꿍을 이룹니다. 허를 찌르는 아이디어와 예측불허의 즐거움으로 매일을 기분 좋은 에너지가 가득하게 만들어 줍니다."
    },
    "INFJ": {
        "name_kr": "가디안",
        "name_en": "Gardevoir",
        "type": "🔮 에스퍼 / 🌸 페어리",
        "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png",
        "feature": "타인의 마음을 깊이 감지하고 다정하게 보호해 주는 포켓몬",
        "reason": "타인의 감정을 세심히 살피고 통찰력이 뛰어난 INFJ의 깊은 내면을 온전히 감싸줍니다. 말없이 곁에 있는 것만으로도 거대한 위로와 진실된 신뢰를 나누는 우정의 단짝입니다."
    },
    "INFP": {
        "name_kr": "이브이",
        "name_en": "Eevee",
        "type": "⭐ 노말",
        "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
        "feature": "무한한 가능성을 가슴에 품은 따뜻하고 사랑스러운 포켓몬",
        "reason": "풍부한 감성과 풍성한 상상력을 지닌 INFP의 따뜻한 본질을 그대로 닮아있습니다. 당신이 가진 고유한 가치와 어떤 꿈이든 온 마음으로 따뜻하게 응원해 주는 둘도 없는 친구입니다."
    },
    "ENFJ": {
        "name_kr": "망나뇽",
        "name_en": "Dragonite",
        "type": "🐉 드래곤 / 🕊️ 비행",
        "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/149.png",
        "feature": "어려움에 처한 이를 다정하게 돕는 상스런 수호자 포켓몬",
        "reason": "주변 사람들을 이끌고 따뜻한 에너지를 베푸는 ENFJ의 이타적인 마음과 깊게 통합니다. 넓은 품으로 사람들을 아우르며 선한 영향력을 퍼뜨리는 최고의 조력자입니다."
    },
    "ENFP": {
        "name_kr": "피카츄",
        "name_en": "Pikachu",
        "type": "⚡ 전기",
        "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        "feature": "언제나 매력이 넘치며 톡톡 튀는 에너지를 뿜어내는 포켓몬",
        "reason": "호기심 많고 매 순간 열정적으로 일상을 즐기는 ENFP의 분위기 메이커 역할을 톡톡히 해냅니다. 지루할 틈 없이 세상을 탐험하고 매일매일 새로운 기쁨을 선사합니다."
    },
    "ISTJ": {
        "name_kr": "이상해씨",
        "name_en": "Bulbasaur",
        "type": "🌿 풀 / ☠️ 독",
        "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png",
        "feature": "성실함과 차분한 태도로 맡은 바 책임을 끝까지 다하는 포켓몬",
        "reason": "원칙을 중요시하고 차분하게 과업을 해내는 ISTJ에게 변함없는 신뢰를 줍니다. 화려함보다는 묵묵함과 실속으로 일상의 든든하고 안정적인 버팀목이 되어주는 존재입니다."
    },
    "ISFJ": {
        "name_kr": "해피너스",
        "name_en": "Blissey",
        "type": "⭐ 노말",
        "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png",
        "feature": "모두의 안녕을 살피고 온기와 기쁨을 아낌없이 나누는 포켓몬",
        "reason": "주변 사람들을 세심하고 헌신적으로 보살피는 ISFJ의 따스한 배려심과 똑 닮았습니다. 서로의 지친 하루를 감싸안고 포근한 평화를 선사하는 정겨운 파트너입니다."
    },
    "ESTJ": {
        "name_kr": "윈디",
        "name_en": "Arcanine",
        "type": "🔥 불꽃",
        "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/59.png",
        "feature": "당당한 위엄과 강한 책임감, 굳건한 충성심을 보여주는 포켓몬",
        "reason": "체계적이고 명확한 판단력으로 주도하는 ESTJ의 발걸음에 가장 확실한 신뢰를 보탭니다. 정해진 목표를 향해 흐트러짐 없이 서로를 지지하며 나아가는 명예로운 단짝입니다."
    },
    "ES
