def synthesize_text_file(text_file, NAME = 'en-US-Polyglot-1', RATE = 1, PITCH = 0, DB = 0):
    """Synthesizes speech from the input file of text."""
    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient()

    with open(text_file) as f:
        text = f.read()
        input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", name=NAME
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=RATE,
        pitch=PITCH,
        volume_gain_db=DB,
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
