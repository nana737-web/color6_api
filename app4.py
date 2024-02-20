import streamlit as st
import cv2
import numpy as np
import PIL
import matplotlib.pyplot as plt
import extcolors
import datetime



st.title('色検出アプリ')

file_path = st.file_uploader('', type=['png', 'jpg', 'jpeg'])
# img = cv2.imdecode(file_path)
# st.image(img)

if file_path :
    # ファイルをバイト列として読み込む
    image_bytes = file_path.read()
    
    # バイト列から画像をデコードする
    img = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)

    # 画像を表示する
    # BGR チャンネルで表示（一般的な画像フォーマットはRGBであるため）
    cv2.imwrite("write.jpg",img) 


filename = "write.jpg"
n = 5

img = PIL.Image.open(filename).resize((256,256)) #軽量化のため、縮小
colors, pixelCount = extcolors.extract_from_image(img, tolerance = 12, limit = n)
colorCodes = ['#{:02x}{:02x}{:02x}'.format(*rgb[0]) for rgb in colors]
colorRates = [rgb[1] for rgb in colors]
plt.pie(colorRates,labels=colorCodes,colors=colorCodes)
dt_now = datetime.datetime.now()
plt.savefig(filename+f"{dt_now}"+"_Color.jpg")


img = filename+f"{dt_now}"+"_Color.jpg"

st.image(img)

