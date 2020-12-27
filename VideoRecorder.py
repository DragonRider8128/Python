import cv2
import numpy as np

#Welcome
print("Welcome to PyVideo! Please select an option: ")
print("1 - Normal video")
print("2 - Slow motion video")
print("3 - Speed motion video")
print("4 - Crazily fast video")
print("5 - Exit")
print("DISCLAIMER: ALL VIDEOS WILL NOT HAVE AUDIO.")
choice = input("\nEnter option here: ")
while choice not in["1","2","3","4","5"]:
    choice = input("Invalid input. Please try again ")
#Run option
if choice != "5":
    video_name = input("Enter a name for your video: ")

if choice == "1":
    speed = 24
elif choice == "2":
    speed = 10
elif choice == "3":
    speed = 60
elif choice == "4":
    speed = 500
else:
    exit()
camera = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
recorder = cv2.VideoWriter(video_name + ".avi",fourcc,speed,(640,480))

while True:
    b, img = camera.read()
    cv2.imshow(video_name,img)
    recorder.write(img)
    key = cv2.waitKey(1)&0xFF
    if key == ord("q"):
        recorder.release()
        break
camera.release()
cv2.destroyAllWindows()
