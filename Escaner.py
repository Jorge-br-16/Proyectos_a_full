import cv2
url = "http://192.168.1.2:8080/video"  #se puede cambiar el url a cualquier con ip
cap = cv2.VideoCapture(url)
while(cap.isOpened()):
    camera, frame = cap.read()
    try:
        cv2.imshow('Imagen',
                   cv2.resize(frame,
                              (1000,700)))
        key =  cv2.waitKey(1)
        if key== ord('q'):
            break
    except cv2.error:
        print("Fin")
        break
cv2.destroyAllWindows()