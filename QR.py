import cv2
from pysafebrowsing import SafeBrowsing
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT) #GREEN LED
GPIO.output(14,GPIO.LOW)
GPIO.setup(15,GPIO.OUT) #RED LED
GPIO.output(15,GPIO.LOW)


#API_KEY de la Google Safe Browsing API
s = SafeBrowsing('AIzaSyD7WLC7dCjgDQ_3HM75mGdrpaZRb_HBWi8')

cap = cv2.VideoCapture(0)

# metoda de detectie a codului QR
detector = cv2.QRCodeDetector()

while True:
    
    _, img = cap.read()
    
    data, bbox, _ = detector.detectAndDecode(img)
    
    #Cutie albastra + data
    if(bbox is not None):
        for i in range(len(bbox)):
            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255,
                     0, 0), thickness=2)
        cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (42, 73, 228), 2)
        
        #Printarea datelor in terminal + cod control pini
        
        if data:
            
            print("Data gasita: ", data)
            r = s.lookup_urls([data])
          
            value = True
            
            if (value in r.get(data).values()):
                print ("Site-ul detectat este malicios.")
                GPIO.output(15,GPIO.HIGH)
                time.sleep(2)
                GPIO.output(15,GPIO.LOW)
                
            else:
                print ("Site-ul detectat nu este malicios.")
                GPIO.output(14,GPIO.HIGH)
                time.sleep(2)
                GPIO.output(14,GPIO.LOW)
             
            
    # Display live
    cv2.imshow("Detector Cod QR", img)
    
    #Inchidere program
    if(cv2.waitKey(1) == ord("q")):
        break
    
# Inchidere ferestre
cap.release()
cv2.destroyAllWindows()