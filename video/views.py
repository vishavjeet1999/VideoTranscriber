from django.shortcuts import render
from .models import *
import os
import speech_recognition as sr
from django.shortcuts import render
from MARVEL.settings import BASE_DIR


def videoUp(request):
    if request.method == 'POST':
        data = videoUpload()
        video = request.FILES['Video']
        data.video = video
        data.save()
        print(videoUpload.objects.latest('id'))
        file_url = videoUpload.objects.latest('id').video.url
        lang = request.POST['lang']

        Basepath = f"{BASE_DIR}/{file_url.split('.')[0]}.wav"
        command = f'ffmpeg -i "{BASE_DIR}/{file_url}" "{Basepath}"'
        print('base: ', Basepath)
        print('command: ', command)

        os.system(command)

        AUDIO_FILE = Basepath

        r = sr.Recognizer()
        a = sr.AudioFile(AUDIO_FILE)

        with a as source:
            audio = r.record(source, duration=100)

        print(type(audio))
        out = r.recognize_google(audio)
        from googletrans import Translator
        translator = Translator()
        out = translator.translate(out, dest=f"{lang}").text
        return render(request, 'index.html', {'out': out, 'status': 'Converted Successfully'})

    return render(request, 'index.html')
