from list_voices import list_voices
from synthesize_ssml_file import synthesize_ssml_file
from synthesize_ssml import synthesize_ssml
from synthesize_text_file import synthesize_text_file
from synthesize_text_with_audio_profile import synthesize_text_with_audio_profile
from synthesize_text import synthesize_text

# Before using the program, go to https://github.com/googleapis/python-texttospeech.git for environment set up and API authentification

# Input is restricted to 500 bytes

# Currently uses synthesize_text_file module which takes text files as input for convenience, for further specifications, look at synthesize_text_file.py

# Note that for any adjustments to parameters, all paratemers need to be explicitly set

# To check different voices, try at https://cloud.google.com/text-to-speech or check out list_voices.py
    # Best is en-US-Studio-M, but has 400 Input size limit since it's a preview voice, so currently default is en-US-Polyglot-1, the second most natural voice as alternative


# For adjustment of speaking rate, pitch and volume, look at: https://cloud.google.com/text-to-speech/docs/reference/rest/v1/AudioConfig
    # Ranges for adjustment:
        # speakingRate: Optional. Input only. Speaking rate/speed, in the range [0.25, 4.0]. 1.0 is the normal native speed supported by the specific voice. 2.0 is twice as fast, and 0.5 is half as fast. If unset(0.0), defaults to the native 1.0 speed. Any other values < 0.25 or > 4.0 will return an error.

        # pitch: Optional. Input only. Speaking pitch, in the range [-20.0, 20.0]. 20 means increase 20 semitones from the original pitch. -20 means decrease 20 semitones from the original pitch.
        
        # volumeGainDb: Optional. Input only. Volume gain (in dB) of the normal native volume supported by the specific voice, in the range [-96.0, 16.0]. If unset, or set to a value of 0.0 (dB), will play at normal native signal amplitude. A value of -6.0 (dB) will play at approximately half the amplitude of the normal native signal amplitude. A value of +6.0 (dB) will play at approximately twice the amplitude of the normal native signal amplitude. Strongly recommend not to exceed +10 (dB) as there's usually no effective increase in loudness for any value greater than that.

# Default configuration
# synthesize_text_file('input.txt')
# Adjusted configuration
synthesize_text_file('input.txt', 'en-US-Polyglot-1', 2, 12, 6)