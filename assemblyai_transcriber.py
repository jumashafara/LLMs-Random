import assemblyai as aai

# replace with your API token
aai.settings.api_key = f"3282ce6eca0a47519f6f69dbbaa38da6"

# URL of the file to transcribe
FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

print(transcript.text)
