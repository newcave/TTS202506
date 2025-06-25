import streamlit as st
from TTS.api import TTS
import os

# 모델 캐싱
@st.cache_resource
def load_tts_model():
    return TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

st.set_page_config(page_title="Open TTS Demo", page_icon="🎙️")
st.title("🎙️ 오픈소스 TTS 웹앱")
st.write("텍스트를 입력하면 음성으로 변환합니다 (powered by Coqui TTS).")

# 텍스트 입력
text_input = st.text_area("텍스트를 입력하세요", "Hello, welcome to the open-source TTS demo.")

# 버튼 클릭 시 처리
if st.button("🎧 음성 생성"):
    if text_input.strip() == "":
        st.warning("텍스트를 입력하세요.")
    else:
        tts = load_tts_model()
        output_path = "output.wav"
        tts.tts_to_file(text=text_input, file_path=output_path)
        st.audio(output_path, format="audio/wav")
        st.success("✅ 음성이 생성되었습니다!")
