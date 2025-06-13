import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="🎮 가위✌️ 바위✊ 보✋ 게임!",
    page_icon="🪨✂️📄",
    layout="centered",
)

# 타이틀
st.markdown("""
    <h1 style='text-align:center; color:#FF6F61; font-family:Comic Sans MS;'>
        🎮 가위✌️ 바위✊ 보✋ 게임! 🎉
    </h1>
    <h3 style='text-align:center; color:#6A5ACD;'>
        컴퓨터와 신나는 대결을 벌여보세요! 😎
    </h3>
    <hr style="border:2px solid #FF6F61;">
""", unsafe_allow_html=True)

# 사용자 선택지
choices = {
    "가위 ✌️": "scissors",
    "바위 ✊": "rock",
    "보 ✋": "paper"
}

user_choice = st.radio("👉 당신의 선택을 골라주세요:", list(choices.keys()), horizontal=True)

if st.button("🕹️ 대결 시작!"):
    user = choices[user_choice]
    computer = random.choice(list(choices.values()))

    # 승부 결정 로직
    if user == computer:
        result = "😐 비겼어요!"
    elif (user == "scissors" and computer == "paper") or \
         (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock"):
        result = "🎉 당신이 이겼어요! 🏆"
    else:
        result = "😢 컴퓨터가 이겼어요!"

    emoji_map = {
        "rock": "✊",
        "paper": "✋",
        "scissors": "✌️"
    }

    # 결과 출력
    st.markdown("---")
    st.markdown(f"<h2 style='text-align:center;'>👤 당신: {emoji_map[user]} vs 🤖 컴퓨터: {emoji_map[computer]}</h2>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align:center; color:#FF4500;'>{result}</h1>", unsafe_allow_html=True)
    
    # 승리하면 풍선!
    if "이겼어요" in result:
        st.balloons()

st.markdown("---")
st.markdown("<p style='text-align:center; color:#888;'>🔥 계속 도전해서 컴퓨터를 이겨보세요! 🔥</p>", unsafe_allow_html=True)

