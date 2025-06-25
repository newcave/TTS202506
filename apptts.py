import streamlit as st
from gtts import gTTS
import os

st.set_page_config(page_title="Korean TTS Web App", page_icon="🗣️")
st.title("🗣️ 텍스트를 음성으로 변환 (gTTS)")
st.markdown("🔊 입력한 텍스트를 Google TTS로 음성으로 변환합니다.")

text = st.text_area("📄 텍스트 입력", "안녕하세요. K-water AI 랩 입니다.")

if st.button("🎧 음성 생성하기"):
    if text.strip() == "":
        st.warning("⚠️ 텍스트를 입력해주세요.")
    else:
        tts = gTTS(text, lang="ko")
        output_path = "output.mp3"
        tts.save(output_path)
        st.audio(output_path)
        st.success("✅ 음성이 생성되었습니다!")
