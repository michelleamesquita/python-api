import pytesseract as ocr
from PIL import Image
from googletrans import Translator
import cv2


image='manga2.jpg'
f=open(image)
text0 = str(ocr.image_to_string(Image.open(image)))
text=list(text0.split(' '))
translator = Translator()
pt=[]
for translation in text:
    # print(translation)
    translated = translator.translate(translation, src='en', dest='pt')
    # print(translated.text)
    pt.append((translated.text).replace('\n', ' '))
# pt=str(pt)
print(pt)
img = cv2.imread(image)
image_copy = img.copy()

d = ocr.image_to_data(Image.open(image),output_type=ocr.Output.DICT)
text2=list(text0.replace('\n', ' ').split(' '))

print(d["text"])
print(text2)

texto=[" DE AGORA EM DEIXE ESTAR JUNTOS PARA SEMPRE!"]

# fontScale
fontScale = 0.5
# Blue color in BGR
color = (0, 0, 0)
# Line thickness of 2 px
thickness = 2
# font
font = cv2.FONT_HERSHEY_SIMPLEX


for j in range(len(text2)):
    for i in range(len(d["text"])):

        if d["text"][i] == text2[j] and d["text"][i] not in '':
         (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
         #cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), -1)


aa=[]
for ele in pt:
        aa.append(ele)
        aa.append(" ")
k=0
if len(aa) != len(d["text"]):
    aa.append('')

for i in range(len(d["text"])):

  if len(aa)!=len(d["text"]):
    aa.append('')
  if len(aa)==len(d["text"]):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.putText(img, aa[0], (d['left'][18], d['top'][18] + d['height'][18]), font, fontScale, color, thickness, cv2.LINE_AA)
        k += 1
        cv2.putText(img, aa[k], (x, y + h), font,fontScale, color, thickness, cv2.LINE_AA)


cv2.imshow('img_copy', img)
cv2.waitKey(0)
