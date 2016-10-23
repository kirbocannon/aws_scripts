import requests
import json
from RecAudio import recordAudio
from questionsEvaluation import *

recordAudio()

url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize'
json_file = '/Users/KennyB/Desktop/jsonCatch.json'
username = 'e519598d-bb0d-4d38-9355-eb4ebc1289fc'
password = 'wboCp3pIjhQY'
headers= {'Content-Type': 'audio/wav'}
audio = open('/Users/KennyB/Desktop/voiceRecordings/test.wav', 'rb')
qflag = False
fiflag = False
r = requests.post(url, data=audio, headers=headers, auth=(username, password))

#put into database. Maybe have a column that is subject, column that is phrase, column with other attributes
#also have a column for friends, family. You can have alexis tell you things about them if you say the column name
#for instance, saying Dad + birthday, alexis will tell you by looking this up in the database
#you could start using this app for clients too. Eventually create a mobile app. Learn C with cooco lol

# When Alexis hears these words, she'll know you are asking a question
questionFlags = ['who', 'what', 'where', 'when', 'why', 'how', 'server']

# writes text to a file captured from recordAudio() function. This is later analyzed by texttospeech
with open(json_file, 'w+') as jf:
    data = jf.write(r.text)

with open(json_file, 'r') as jf:
    data = json.load(jf)

for key, value in data.items():
    if key == 'results':
        voice_input = value[0]['alternatives'][0]['transcript']
        #print(voice_input)

for i in questionFlags: #initial check. Are you asking who a person is, thing? place?
    if i in voice_input:
        qflag = True

if qflag is True:
    questionInput(voice_input)










