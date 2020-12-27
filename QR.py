import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

#Ask user for QR code content and file name
while True:
    print("Welcome to PyQR, the QR code generator and decoder made completely with python! You can generate and decode QR codes within seconds!")
    print("1 - Generate QR code")
    print("2 - Decode QR code")
    print("3 - Exit")
    choice = input("Select one: ")
    print("\n")

    while choice not in ["1","2","3"]:
        choice = input("Invalid input. Please try again: ")

    if choice == "1":
        print("Just enter your content and file name and your QR code is generated! You can find the file in the same folder as this program.")
        content = input("Enter text or URL for QR code: ")
        file_name = input("Enter a name for your file: ")

        qr = pyqrcode.create((content))
        qr.png(file_name +".png", scale = 8)
        print("QR code generated.")

    elif choice == "2":
        print("Decode QR codes to find out what content in contains. Here's how: ")
        print("1.) Make sure your QR code file is a .png file.")
        print("2.) Move your file to the same folder as this program.")
        print("3.) Enter the file name. Do NOT TYPE .PNG IN FRONT.")
        print("4.) Your QR code will be decoded!")
        print("IMPORTANT: QR CODES WILL NOT BE SCANNED. YOU WILL SIMPLY BE DISPLAYED THE CONTENT IT CONTAINS.")
        print("\n")
        qr_to_decode = input("Enter file name: ")

        try:
            decoded = decode(Image.open(qr_to_decode + ".png"))
            print(decoded[0].data.decode("ascii"))
        except:
            print("File does not exist or is not a .png file.")
    else:
        exit()
    print("\n")
