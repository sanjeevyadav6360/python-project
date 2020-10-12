import cv2

# vid_file = cv2.VideoCapture('C:/Users/YADAV PC/Desktop/pedestrian2_200915.mp4')
vid_file = cv2.VideoCapture('C:/Users/YADAV PC/Desktop/car_200915.mp4')

car_tracker = cv2.CascadeClassifier('C:/Users/YADAV PC/Desktop/car_detector.xml')
pedestrian_tracker = cv2.CascadeClassifier('C:/Users/YADAV PC/Desktop/haarcascade_fullbody.xml')


while True:
    # Read Video
    (read_successful, frame) = vid_file.read()
    if read_successful:
        # Convert to greyscale
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # Detect Cars & Pedestrian
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)

    # Draw square around the cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Draw square around the pedestrians
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

    # Display the image
    cv2.imshow('Car & Pedestrian Detector', frame)

    # Hold it so it won't autoclose
    key = cv2.waitKey(1)

    # Stop if Q key is pressed
    if key == 81 or key == 113:
        break

# Release the videoCapture object
vid_file.release()

print('Code Completed')
