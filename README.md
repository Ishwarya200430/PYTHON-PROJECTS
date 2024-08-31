

# Funny Alexa: Your Voice-Activated Assistant

Created by : KUNDURU ISHWARYA

## Overview
Alexa is a simple voice-activated assistant built using Python. It can perform various tasks such as playing songs, telling the time, fetching Wikipedia summaries, telling jokes, and more. This assistant uses several libraries to handle speech recognition, text-to-speech, and browser control.

## Features

- **Play Music**: Play songs on YouTube using voice commands.
- **Current Time**: Get the current time spoken out loud.
- **Wikipedia Search**: Retrieve and speak out summaries from Wikipedia.
- **Jokes**: Get a random joke.
- **Custom Responses**: Includes playful responses to specific questions.

## Installation

To get started, you'll need to install several Python libraries. Open your command prompt or terminal and run the following commands:

```sh
pip install SpeechRecognition
pip install pyttsx3
pip install pywhatkit
pip install wikipedia
pip install pyjokes
```

## Usage

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/romantic-alexa.git
   cd romantic-alexa
   ```

2. **Run the Assistant**

   Make sure your microphone is set up and working. Then, run the assistant script:

   ```sh
   python romantic_alexa.py
   ```

3. **Voice Commands**

   - **Play a song**: Say "Alexa, play [song name]".
   - **Current time**: Say "Alexa, time".
   - **Wikipedia information**: Say "Alexa, who the heck is [person name]".
   - **Joke**: Say "Alexa, joke".

## How It Works

- **Speech Recognition**: Listens for voice commands and converts them into text using the Google Web Speech API.
- **Text-to-Speech**: Converts text responses into spoken words using `pyttsx3`.
- **YouTube Control**: Uses `pywhatkit` to play songs on YouTube.
- **Wikipedia**: Fetches information from Wikipedia.
- **Jokes**: Retrieves jokes using the `pyjokes` library.

## Troubleshooting

- Ensure your microphone is properly configured and working.
- Make sure you have an active internet connection.
- If you encounter any issues, check the Python package documentation or raise an issue on the [GitHub repository](https://github.com/yourusername/Funny-alexa/issues).

## Contributing

Feel free to fork the repository, make changes, and submit pull requests. Contributions are always welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please reach out to [kunduruishwarya30@gmail.com].

