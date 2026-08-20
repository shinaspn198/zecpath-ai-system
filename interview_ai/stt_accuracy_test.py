from pathlib import Path
from interview_ai.speech_to_text import SpeechToText


def test_audio_file(stt, audio_path):
    result = stt.transcribe(str(audio_path))

    print(f"\nAudio: {audio_path.name}")
    print(f"Language: {result['language']}")
    print(f"Transcript: {result['text']}")


if __name__ == "__main__":
    stt = SpeechToText(model_name="base")

    audio_folder = Path("data/audio_tests")

    audio_files = list(audio_folder.glob("*.wav"))

    if not audio_files:
        print("No test audio files found.")
        print("Add WAV files to data/audio_tests/")
    else:
        for audio_file in audio_files:
            test_audio_file(stt, audio_file)