import speech_recognition

# The Recognizer is initialized.
UserVoiceRecognizer = speech_recognition.Recognizer()
print("---> INCOMING CALLS 📞 <--")

while True:
    try:
        with speech_recognition.Microphone() as UserVoiceInputSource:
            UserVoiceRecognizer.adjust_for_ambient_noise(UserVoiceInputSource, duration=0.5)
            # The Program listens to the user voice input.
            UserVoiceInput = UserVoiceRecognizer.listen(UserVoiceInputSource)
            UserVoiceInput_converted_to_Text = UserVoiceRecognizer.recognize_google(UserVoiceInput)
            UserVoiceInput_converted_to_Text = UserVoiceInput_converted_to_Text.lower()
            print(UserVoiceInput_converted_to_Text)
            with open('read.txt', 'w') as sourceFile:
                #sourceFile.close()
                print(UserVoiceInput_converted_to_Text, file=sourceFile)
                sourceFile.close()

    except KeyboardInterrupt:
        print('A KeyboardInterrupt encountered; Terminating the Program !!!')
        break

    except speech_recognition.UnknownValueError:
        print("No User Voice detected OR unintelligible noises detected OR the recognized audio cannot be matched to text !!!")
        break

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
