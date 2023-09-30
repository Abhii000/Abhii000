import speech_recognition as sr

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            print("You said:", text)
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand your speech.")
        except sr.RequestError as e:
            print(f"Error requesting speech recognition: {e}")

if __name__ == "__main__":
    main()
