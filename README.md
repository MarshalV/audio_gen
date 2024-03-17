# Speech Synthesis Application

This application is designed to synthesize speech from text using the "Bark" model and PyQt5 library to create a graphical user interface (GUI).

## Features

- **Voice Presets**: Users can select from a list of voice presets for speech synthesis.
- **Audio Generation**: The application generates audio from the input text using the selected voice preset.
- **Playback Control**: Users can play, pause, and resume audio playback.
- **Progress Monitoring**: The application displays the current playback position and total duration of the audio.
- **Save Audio**: Users can save the synthesized audio as a WAV file.

## Getting Started

1. **Dependencies Installation**: Install the required dependencies by running:
pip install PyQt5 transformers torch soundfile


vbnet
Copy code

2. **Running the Application**: Execute the `main.py` file to launch the application.

3. **Importing Text**: Click the "import" button to import text into the application.

4. **Selecting Voice Presets**: Choose a voice preset from the dropdown menu labeled "presets".

5. **Generating Audio**: Click the "process" button to start the speech synthesis process.

6. **Playback**: Users can control audio playback using the play, pause, and resume buttons.

7. **Saving Audio**: Once the synthesis process is complete, users can save the synthesized audio by clicking the "save" button.

