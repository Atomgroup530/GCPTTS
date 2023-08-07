def list_voices():
    """Lists the available voices."""
    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient()

    # Performs the list voices request
    voices = client.list_voices()

    for voice in voices.voices:
        # Display the supported language codes for this voice. Example: "en-US"
        for language_code in voice.language_codes:
            if language_code == 'en-US':    # if statement added to narrow down to English (US), can remove and put line 15 before the for loop to see full list
                # Display the voice's name. Example: tpc-vocoded
                print(f"Name: {voice.name}")
                # print(f"Supported language: {language_code}")

                ssml_gender = texttospeech.SsmlVoiceGender(voice.ssml_gender)

                # Display the SSML Voice Gender
                print(f"SSML Voice Gender: {ssml_gender.name}\n")

                # Display the natural sample rate hertz for this voice. Example: 24000
                # print(f"Natural Sample Rate Hertz: {voice.natural_sample_rate_hertz}\n")
