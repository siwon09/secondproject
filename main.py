import streamlit as st
import random

st.set_page_config(
    page_title="가위✌️ 바위✊ 보✋ 게임!",
    page_icon="🎮",
    layout="centered",
)

# 🧡 타이틀
st.markdown("<h1 style='text-align: center; color: orange;'>🎮 가위✌️ 바위✊ 보✋ 게임!</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>컴퓨터와 대결해보세요! 누가 더 강할까요? 😎</h3>", unsafe_allow_html=True)
st.markdown("---")

# 선택 옵션
choices = {
    "가위 ✌️": "scissors",
    "바위 ✊": "rock",
    "보 ✋": "paper"
}

user_choice = st.radio("👉 당신의 선택은?", list(choices.keys()), horizontal=True)

if st.button("🔫 대결 시작!"):
    user = choices[user_choice]
    computer = random.choice(list(choices.values()))

    # 결과 판단
    result = ""
    if user == computer:
        result = "😐 비겼어요!"
    elif (user == "scissors" and computer == "paper") or \
         (user == "rock" and computer == "
