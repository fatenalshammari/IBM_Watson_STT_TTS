 # authentacation:
from ibm_watson import SpeechToTextV1  
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


  # setting the url and apikey

authenticator = IAMAuthenticator("mPy_Q7-ZeS-6yMq8MHfJGbLD3GcyUlp6fVvoGRZSoTtM")


def main():

    stt = SpeechToTextV1(authenticator=authenticator)
    stt.set_service_url("https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/45bb2bc3-f82b-4171-91e7-6dae6a54322a")

    #with open('text.txt', 'r') as f:
    #   text = f.read()

    with open('speech.mp3', 'rb') as audio_file:
        res = stt.recognize(audio=audio_file, content_type='audio/mp3').get_result()


if __name__ == "__main__":
    main()