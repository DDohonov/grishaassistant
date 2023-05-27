from recognize.rec import *
from response.init import *

#Good dumplings are very very tasty

while True:
    # старт записи речи с последующим выводом распознанной речи 
    voice_input = record_and_recognize_audio()
    print(voice_input)
    if voice_input == 'стоп':
        break
    else:
        for tolk in list_tolking:
            for req in tolk.request:
                if req in voice_input:
                    tolk.response(voice_input)
                    break

    tts_engine.runAndWait()
