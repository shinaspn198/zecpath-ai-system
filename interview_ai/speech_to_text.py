import whisper


class SpeechToText:
    def __init__(self, model_name="base"):
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path):
        result = self.model.transcribe(audio_path)

        return {
            "text": result["text"].strip(),
            "language": result.get("language"),
        }


if __name__ == "__main__":
    stt = SpeechToText()

    audio_file = input("Enter audio file path: ")

    result = stt.transcribe(audio_file)

    print("\nTranscription:")
    print(result["text"])

    print("\nDetected Language:")
    print(result["language"])