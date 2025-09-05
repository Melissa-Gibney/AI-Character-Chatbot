import whisper

class STT:

    model = whisper.load_model("base")
    result = model.transcribe("audio.mp3")

    def getText(self, audio) -> str:
        return self.model.transcribe(audio)["text"]