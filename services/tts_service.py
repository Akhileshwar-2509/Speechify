from google.cloud import texttospeech

def synthesize_text(text, language='en-US', voice_type='NEUTRAL', gender='MALE'):
    client = texttospeech.TextToSpeechClient()

    # Set up the voice parameters
    voice = texttospeech.VoiceSelectionParams(
        language_code=language,
        ssml_gender=texttospeech.SsmlVoiceGender[gender]
    )

    # Set up the audio configuration
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Convert text to speech
    synthesis_input = texttospeech.SynthesisInput(text=text)
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Save the audio output to a file
    with open('output.mp3', 'wb') as out:
        out.write(response.audio_content)
