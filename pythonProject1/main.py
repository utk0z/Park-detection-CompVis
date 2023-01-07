import cv2                                                              #openCV kütüphanesinin dahil edilmesi
import pickle                                                           #pickle kütüphanesinin dahil edilmesi
import numpy as np                                                      #numpy kütüphanesinin dahil edilmesi
from Database import *
import firebase_admin
from firebase_admin import credentials, firestore

cap = cv2.VideoCapture('carPark.mp4')                                       # Video'yu yakalama
with open('CarParkPos', 'rb') as f:                                     # ParkingSpacePicker.py dosyasında
    posList = pickle.load(f)                                            # oluşturduğumuz CarParkPos dosyasını
                                                                        #       binary modunda okuma
width, height = 107, 48                                     # oluşturulan dörtgenlerin genişlik ve yükseklik değerleri
sayac=0
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)

def checkParkingSpace(imgPro):
    spaceCounter = 0
    for pos in posList:
        x, y = pos
        imgCrop = imgPro[y:y + height, x:x + width]
        count = cv2.countNonZero(imgCrop)
        if count < 850:
            color = (0, 255, 0)
            thickness = 2
            spaceCounter += 1
            update_isfree(x,y,1)
        else:
            color = (0, 0, 255)
            thickness = 2
            update_isfree(x, y, 0)
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
while True:
    create_table()
    if(sayac==120):
        print("zaman geldi")
        conn = sql.connect("isFree.db")
        cursor = conn.cursor()

        # Veritabanındaki verileri okuyun ve Firebase Firestore veritabanında mevcut verileri güncelleyin
        cursor.execute("SELECT id,isFree FROM COORDİNATES ")
        rows = cursor.fetchall()
        db = firestore.client()
        for row in rows:
            data = {
                'id': row[0],
                'isFree': row[1],
                # ... diğer sütunlar için aynı şekilde
            }
            # Firestore veritabanında mevcut verileri bulun ve güncelleyin
            doc_ref = db.collection('isFree').where('id', '==', row[0]).limit(1).get()
            if doc_ref:
                for doc in doc_ref:
                    doc_ref = doc.reference
                    doc_ref.update(data)
            else:
                # Veri yoksa, yeni bir belge oluşturun
                db.collection('isFree').add(data)

        # Bağlantıyı kapatın
        conn.close()
        sayac=0

    #videodaki olunan frame'in toplam frame sayısına eşit olduğunda başa almasını sağlayan kod parçası
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)
    checkParkingSpace(imgDilate)
    cv2.imshow("Image", img)
    sayac= sayac+1
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break