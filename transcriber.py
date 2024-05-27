import speech_recognition as sr
from pydub import AudioSegment

def transcribe_audio_to_text(audio_file_path, output_file_path):
    recognizer = sr.Recognizer()

    try:
        # Convert audio to WAV format if it's not already
        if not audio_file_path.endswith('.wav'):
            audio = AudioSegment.from_file(audio_file_path)
            wav_file_path = audio_file_path.rsplit('.', 1)[0] + '.wav'
            audio.export(wav_file_path, format='wav')
        else:
            wav_file_path = audio_file_path

        with sr.AudioFile(wav_file_path) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)

        with open(output_file_path, 'w') as file:
            file.write(text)

        print("Transcription successful. Text written to:", output_file_path)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    audio_file_path = "C:\\Users\\YourUsername\\Desktop\\Recording.m4a"
    output_file_path = "C:\\Users\\YourUsername\\Desktop\\Transcription.txt"
    transcribe_audio_to_text(audio_file_path, output_file_path)
