import requests
import pyaudio
import wave
import sys


def voiceInputToAlexis(voice):
    url = 'https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize?voice=en-US_AllisonVoice'
    received_voice_file = '/Users/KennyB/Desktop/recievedVoice/received.wav'
    headers= {'Content-Type': 'application/json', 'Accept': 'audio/wav'}
    data = "{\"text\":\"%s\"}" %(voice)
    username = '48ff4651-e1f6-47d2-82d6-5d4fef7bc791'
    password = 'LUVEfWR3qn0x'
    request = requests.post(url, data=data, headers = headers, auth= (username, password))

    with open(received_voice_file, 'wb') as handle:
        handle.write(request.content)

    CHUNK = 1024

    wf = wave.open(received_voice_file, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()
    p.terminate()



