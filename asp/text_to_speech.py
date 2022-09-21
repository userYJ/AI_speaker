from gtts import gTTS
from playsound import playsound

file_name = 'sample.mp3'

# 영어 문장
# text = 'Don't dwell on the past'
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name)

# 한글 문장
# text = '간단한 인공지능 비서입니다.'
# tts_ko = gTTS(text=text, lang='ko')
# tts_ko.save(file_name)

# playsound(file_name) # 바로 play

with open('sample.txt', 'r', encoding='utf8') as f:
    text = f.read()

tts_ko = gTTS(text=text, lang='en')
tts_ko.save(file_name)
playsound(file_name)