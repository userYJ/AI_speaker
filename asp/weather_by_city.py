import requests
import json
import speech_recognition as sr
import re

# 마이크로부터 음성 듣기
r = sr.Recognizer()
with sr.Microphone() as source:
    print("말씀 하세요")
    audio = r.listen(source) # 마이크로부터 음성 듣기

try:
    # 구글 API
    # 영어 문장
    text = r.recognize_google(audio, language='ko' or 'en-US' )
    print(text)

    # 한글 문장
    # text = r.recognize_google(audio, language='ko')
    # print(text)

except sr.UnknownValueError:
    print('인식 실패') # 음성인식 실패의 경우
except sr.RequestError:
    print('요청 실패 : {0}'.format(e)) # API key error ...


keyword = text
keyword = re.sub('[^a-zA-Z]', '', keyword)
city = keyword

if "재팬" in text:
    city = "Japna"
elif "서울" in text:
    city = "Seoul"
elif "뉴욕" in text:
    city = "NewYork"
elif "런던" in text:
    city ="London"

# city = text
apiKey = "" # api key 입력
lang = 'kr'
units = 'metric'
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"

result = requests.get(api)
result = json.loads(result.text)

# print(result)
cityname = result['name'] # 도시 이름
temperature = result['main']['temp'] # 온도
weather = result['weather'][0]['main'] # 날씨
humidity = result['main']['humidity'] # 습기

print(cityname)
print(temperature)
print(humidity)
if weather =='Clear':
    print('맑습니다')
elif weather =='Clouds':
    print('흐립니다.')
elif weather =='Rain':
    print('비가 내립니다.')
elif weather =='Wind':
    print('바람이 붑니다.')
