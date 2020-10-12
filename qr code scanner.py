import cv2
from pyzbar.pyzbar import decode
import webbrowser

from warnings import filterwarnings
filterwarnings('ignore')

# Capture the video from default camera
capture = cv2.VideoCapture(0)

print('--------------------------------------------------------------------------------------------\n')

recieved_data = None
while True:
    # reading frame from the camera
    _, frame = capture.read()
    # Decoding the QR Code 
    decoded_data = decode(frame)
    try:
        data = decoded_data[0][0]
        if data != recieved_data:
            recieved_data = data
            print("\n", data,"\n")
    except:
        pass
    
    # Showing video.
    cv2.imshow("QR CODE Scanner", frame)

    # To exit press Esc Key.
    key = cv2.waitKey(1)
    if key == 27:
        break

ndata=data.decode("utf-8")

# open webbrowser
webbrowser.open('https://google.com/?#q=' + ndata)    
webbrowser.open('https://www.youtube.com/results?search_query=' + ndata)
# webbrowser.open('https://en.wikipedia.org/wiki/'+ ndata)

print('Code Completed')
