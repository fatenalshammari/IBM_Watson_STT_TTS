  # authentacation:
from ibm_watson import TextToSpeechV1  
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


  # setting the url and apikey

authenticator = IAMAuthenticator("pPSM4sweUFAlI0sON7OIE3s-QfHDie967rKnKBKTL37u")


def main():

    tts = TextToSpeechV1(authenticator=authenticator)
    tts.set_service_url("https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/73d18600-891c-4f0e-845f-97451caacb8f")

    with open('text.txt', 'r') as a:
        text = a.read()

    with open('speech.mp3', 'wb') as audio_file:
        res = tts.synthesize(text, accept='audio/mp3').get_result()
        audio_file.write(res.content)


if __name__ == "__main__":
    main()