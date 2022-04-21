
import dlib
import cv2
import imutils

## loading detector
detector = dlib.simple_object_detector("stop_sign3.svm")
cap = cv2.VideoCapture('stop_sign.mp4')

while cap.isOpened():
    # Reading the video stream
    ret, image = cap.read()
    boxes = detector(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    if ret:
        for b in boxes:
            (x, y, w, h) = (b.left(), b.top(), b.right(), b.bottom())
            cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 2)
            cv2.putText(image, 'stop sign', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        cv2.imshow("Image", image)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()