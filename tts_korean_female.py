import os
from google.cloud import texttospeech
# Set the credentials for Google Cloud APIs
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "stt-key.json"
def text_to_speech(text, filename="output.mp3"):
    client = texttospeech.TextToSpeechClient()

    # 한국어, 여성 음성 설정
    voice = texttospeech.VoiceSelectionParams(
        language_code="ko-KR",  # 한국어
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,  # 여성 음성
        name="ko-KR-Wavenet-A",  # Wavenet 음성 선택 (여성 목소리)
    )

    # 오디오 설정 (MP3 형식)
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # 텍스트를 SSML로 변환
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # TTS 요청
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # 음성 파일 저장
    with open(filename, "wb") as out:
        out.write(response.audio_content)
    print(f"Speech saved as {filename}")

# 사용 예시
text = "원석님 머하시나요"
text_to_speech(text, "output.mp3")
