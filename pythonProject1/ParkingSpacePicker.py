import cv2                                                              #openCV kütüphanesinin dahil edilmesi
import pickle                                                           #pickle kütüphanesinin dahil edilmesi
from Database import *
width, height = 107, 48                        #Denemeler sonrası görsel üzerindeki park alanlarını piksel olarak
create_table()                                                      # karşılıklarının değişkenlere atanması
try:                                                                    # Yapılan her değişikliği yakalayıp
    with open('CarParkPos', 'rb') as f:                                 # posList üzerinde değişiklik yapmak için
        posList = pickle.load(f)                                        # kullanılan Try - except yapısı
except:
    posList = []
def mouseClick(events, x, y, flags, params):                                #   ** Mouse ayarlamaları   **  #
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
        insert(x,y,0)
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            Ymax = y1+height
            Xmax = x1 + width
            if x1 < x < Xmax and y1 < y <Ymax:
                posList.pop(i)
                delete_coordinate()
    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)                                             #   ** Mouse ayarlamaları   **  #

while True:                               #  **Sonsuz Döngü içerisinde çünkü sürekli değişikliği görmek istiyoruz

    img = cv2.imread('carParkImg.png')            #  **Görselimizin okunması program içeriğine dahil edilmesi

    for pos in posList:                                              #  **Oluşturulan posList listesi
        cv2.rectangle(img, pos,                                  #içerisinde bulunan her dörtgene ulaşmak
                      (pos[0] + width, pos[1] + height),                # ve çerçevelerin çizimi
                      (255, 0, 255),                                 # amacı ile oluşturulan "for" döngüsü
                      2)
    cv2.imshow("Image", img)                                # **Dahil edilen görselin pencerede gösterilmesi

    cv2.setMouseCallback("Image", mouseClick)               # ** Mouse tuşlarının ayarlanması için yazılan fonksiyonu
                                                                            #çağıran openCV metodu

    if cv2.waitKey(1) & 0xFF == ord('q'):                   # Açılan pencerenin ekranda kalması ve kapanması için
        break                                                                # gereken ayarlamalar




