import pyttsx3
import PyPDF2
speaker=pyttsx3.init()
book = open('java_tutorial.pdf','rb')
pdfReader = PyPDF2.PdfReader(book)
page= pdfReader.pages[7]
text=page.extract_text()
speaker.say(text)
speaker.runAndWait()
