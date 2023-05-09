import cv2


# harcascade = "model/haarcascade_russian_plate_number.xml" #especially for russian registration car plates
harcascade = "model/indian_license_plate.xml" #especially for indian registration car plates

cap = cv2.VideoCapture(0)

cap.set(3, 640) #width
cap.set(4, 480) #height


# min_area = 500 
min_area = 2000 #for indian registration num plates(2000-5000sq pixels)
plate_count = 0
while True:
    success, img = cap.read()

    plate_cascade = cv2.CascadeClassifier(harcascade)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(gray_img, 1.1, 4)

    for (x,y,w,h) in plates:
        area = w*h

        if(area>min_area): #check for no. of plate cars
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(img, "Number Plate: ", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            # roi->Image region of interest (ROI)
            img_roi = img[y: y+h, x: x+w]
            cv2.imshow("ROI", img_roi)

    cv2.imshow("Cam scanner", img)

    if(cv2.waitKey(1) & 0xFF==ord('q')): #To stop Cam window
        break

    if(cv2.waitKey(1) & 0xFF==ord('s')): #To capture num plates
        cv2.imwrite("car_num_plates/num_plate_"+str(plate_count)+".jpg", img_roi)
        cv2.rectangle(img, (0,200), (640,300), (0,255,0), cv2.FILLED)
        cv2.putText(img, "Plate saved", (150,265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0,0,255), 2)
        cv2.imshow("Results", img)
        cv2.waitKey(500)
        plate_count+=1
            
