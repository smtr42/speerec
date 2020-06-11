import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

def run():
    r = sr.Recognizer()
    mic = sr.Microphone()
    # print(sr.Microphone.list_microphone_names())
    with mic as source:
        # if needed to adjust ambient noise
        r.adjust_for_ambient_noise(source)
        # records input from the source until silence is detected
        audio = r.listen(source)

        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        # try recognizing the speech in the recording
        # if a RequestError or UnknownValueError exception is caught,
        #     update the response object accordingly
        try:
            response["transcription"] = r.recognize_google(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"

        return response

if __name__ == "__main__":
    run()

