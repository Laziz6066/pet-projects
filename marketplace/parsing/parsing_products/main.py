import vlc
from gtts import gTTS


def assitant(mytext):
    audio = gTTS(text=mytext, lang="ru", slow=False)
    audio.save("example.mp3")
    audio_file = "example.mp3"
    p = vlc.MediaPlayer(audio_file)
    p.play()
    while True:
        if p.get_state() == vlc.State.Ended:
            break
    p.release()

