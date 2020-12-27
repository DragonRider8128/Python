import pyttsx3
import PyPDF2

print("Welcome to PyBook! Turn any page of any PDF to an audiobook. Here's how:")
print("1 - Move the PDF file to the same folder as this program.")
print("2 - Run PyBook.")
print("3 - Enter pdf name (Example - test.pdf).")
print("4 - Enter the page number you want to read.")
print("\n")
try:
    book_choice = input("Enter file name (example: python.pdf). ")
    page_choice = input("Which page do you want to read? ")
    book = open(book_choice, "rb")
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speaker = pyttsx3.init()
    page = pdfReader.getPage(int(page_choice) - 1)
    text = page.extractText()
    speaker.say(text)
    print("Reading...")
    speaker.runAndWait()
except:
    print("\n")
    print("ERROR. Possible causes could be: File does not exist, file is not a PDF, file is not in the same folder or the page number entered is too high and does not exist in the PDF.\n")
