from cgitb import text
import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

import requests
import json
import re

r = sr.Recognizer()
m = sr.Microphone()

# (듣기, STT)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko' or 'en-US')
        print('[나]'+ text)
        answer(text)
    except sr.UnknownValueError:
        print('인식 실패') # 음성인식 실패의 경우
    except sr.RequestError:
        print('요청 실패 : {0}'.format(e)) # API key error ...

# (TTS)
def speak(text):
    print('[인공비서]' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko'or 'en-US')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name): # voice.mp3 파일 삭제
        os.remove(file_name)



city = 'Seoul'
apiKey = "" # api key 입력
lang = 'kr'
units = 'metric'
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"

result = requests.get(api)
result = json.loads(result.text)

cityname = result['name'] # 도시 이름
temperature = result['main']['temp'] # 온도
weather = result['weather'][0]['main'] # 날씨
humidity = result['main']['humidity'] # 습기


# 대답
def answer(input_text):
    answer_text = ''
    if '운' in input_text:
        answer_text = '나만 운없어.'
    elif '큐브' in input_text:
        answer_text = '큐브는 운빨입니다.'
    elif '꿀' in input_text:
        answer_text = '꿀은 맛있습니다.'
        
    # weather    
    elif '날씨' in input_text:
        if weather == "Clear" :
            answer_text = f'{cityname} 의 날씨는 맑고 {temperature}도 입니다.'
        elif weather == "Clouds":
            answer_text = f'{cityname} 의 날씨는 흐리고 {temperature}도 입니다.'
        elif weather == "Rain":
            answer_text = f'{cityname} 의 날씨는 비가 내리고 {temperature}도 입니다.'
        elif weather == "Wind":
            answer_text = f'{cityname} 은 바람이 불며 {temperature}도 입니다.'
        else:
            answer_text= '네? 못 알아들었어요.'

    elif '종료'or 'exit' in input_text:
        answer_text = 'Goodbye'
        stop_listening(wait_for_stop=False) # 더 이상 듣지 않음
    else:
        answer_text = '네? 못 알아들었어요.'
    
    speak(answer_text)

speak('듣고 있습니다')
stop_listening = r.listen_in_background(m, listen)

while True:
    time.sleep(0.03)