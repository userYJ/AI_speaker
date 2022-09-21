import speech_recognition as sr

# 마이크로부터 음성 듣기
r = sr.Recognizer()
with sr.Microphone() as source:
    print("말씀 하세요")
    audio = r.listen(source) # 마이크로부터 음성 듣기

# 파일로부터 음성 불러오기 (wav, aiff/aiff-c, flac 가능, mp3 불가)
# r = sr.Recognizer()
# with sr.AudioFile('sample.wav') as source:
#     audio = r.record(source)

try:
    # 구글 API
    # 영어 문장
    # text = r.recognize_google(audio, language='en-US')
    # print(text)

    # 한글 문장
    text = r.recognize_google(audio, language='ko')
    print(text)

except sr.UnknownValueError:
    print('인식 실패') 
except sr.RequestError:
    print('요청 실패 : {0}'.format(e)) # API key error ...