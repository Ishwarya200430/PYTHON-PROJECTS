
# PDF Text-to-Speech Reader

CREATED BY:KUNDURU ISHWARYA

## Overview

This project provides a simple script that extracts text from a specific page of a PDF file and reads it aloud using text-to-speech. The script utilizes the `pyttsx3` library for text-to-speech functionality and the `PyPDF2` library for PDF text extraction.

## Requirements

- Python 3.x
- `pyttsx3` library
- `PyPDF2` library

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Ishwarya200430/PYTHON-PROJECTS.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd  https://github.com/Ishwarya200430/PYTHON-PROJECTS.git
   ```

3. **Install the required libraries:**

   You can install the required libraries using pip. Run the following command:

   ```bash
   pip install pyttsx3 PyPDF2
   ```

## Usage

1. **Prepare your PDF file:**

   Ensure that the PDF file you want to read is named `java_tutorial.pdf` and is located in the same directory as the script. You can modify the script to use a different filename or path if needed.

2. **Run the script:**

   Execute the script using Python:

   ```bash
   python your_script_name.py
   ```

   Replace `your_script_name.py` with the name of your Python script file.

## Code Explanation

Here's a brief explanation of what the script does:

1. **Imports the required libraries:**
   - `pyttsx3` for text-to-speech.
   - `PyPDF2` for reading PDF files.

2. **Initializes the text-to-speech engine:**

   ```python
   speaker = pyttsx3.init()
   ```

3. **Opens the PDF file:**

   ```python
   book = open('java_tutorial.pdf', 'rb')
   ```

4. **Creates a PDF reader object:**

   ```python
   pdfReader = PyPDF2.PdfReader(book)
   ```

5. **Extracts text from the 13th page:**

   ```python
   page = pdfReader.pages[12]
   text = page.extract_text()
   ```

6. **Speaks the extracted text:**

   ```python
   speaker.say(text)
   speaker.runAndWait()
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or comments, please contact [kunduruishwarya30@gmail.com]
