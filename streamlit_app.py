import streamlit as st
import base64

# 定義一個函數來將本地圖片轉換成 base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# 設定頁面標題
st.title("網頁測試測試")

# 第一部分
img1 = get_base64_of_image('images/這裡是什麼鬼地方.jpg')
st.markdown(f"""
<div class="section" style="margin: 40px 0; position: relative; text-align: center;">
    <img src="data:image/jpg;base64,{img1}" alt="背景圖片" style="width: 100%; border-radius: 8px; filter: grayscale(100%);">
    <div style="position: absolute; top: 10%; left: 50%; transform: translate(-50%, -50%); color: white; font-size: 44px; font-weight: bold; width: 80%">這裡是 CY 的迷因基地</div>
    <div style="position: absolute; top: 16%; left: 50%; transform: translate(-50%, -50%); width: 90%;">
        <div style="border-top: 1px solid white; margin: 10px 0;"></div>
    </div>
    <div style="position: absolute; top: 17%; left: 5%; color: white; font-size: 28px;">CYPan & CYPan</div>
    <div style="position: absolute; top: 17%; right: 5%; color: white; font-size: 28px; text-align: right;">2024 Oct. 20th</div>
    <p style="position: absolute; bottom: 10%; right: 5%; color: white; font-size: 32px; text-align: right;">歡迎來到 CY 的迷因基地</p>
</div>
""", unsafe_allow_html=True)

# 第二部分
img2 = get_base64_of_image('images/真的好想好想要.jpg')
st.markdown(f"""
<div class="section" style="margin: 40px 0; display: flex; flex-wrap: wrap; justify-content: space-between;">
    <div style="flex: 1; margin: 10px; min-width: 300px; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
        <img src="data:image/jpg;base64,{img2}" alt="左側圖片" style="width: 100%; border-radius: 8px;">
    </div>
    <div style="flex: 1; margin: 10px; min-width: 300px; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
        <p style="font-size: 24px">
            這邊是要給你各位的一段話<br>
            能不能針對每個人給還不知道<br>
            反正會放這邊
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# 第三部分
img3_1 = get_base64_of_image('images/我又沒有唸書.jpg')
st.markdown(f"""
<div class="section" style="margin: 40px 0; position: relative; overflow: hidden;">
    <div class="carousel" style="display: flex; transition: transform 0.5s ease;">
        <img src="data:image/jpg;base64,{img3_1}" alt="圖片1" style="width: 100%; flex: none;">
    </div>
</div>
""", unsafe_allow_html=True)

# 第四部分
img4_1 = get_base64_of_image('images/你要出多少.jpg')
img4_2 = get_base64_of_image('images/我只有七塊.jpg')
st.markdown(f"""
<div class="section" style="margin: 40px 0; display: flex; justify-content: space-between; align-items: center;">
    <div style="flex: 1; margin: 10px; display: flex; justify-content: center;">
        <img src="data:image/jpg;base64,{img4_1}" alt="左側圖片" style="width: 100%; border-radius: 8px;">
    </div>
    <div style="flex: 1; margin: 10px; display: flex; justify-content: center;">
        <img src="data:image/jpg;base64,{img4_2}" alt="右側圖片" style="width: 100%; border-radius: 8px;">
    </div>
</div>
""", unsafe_allow_html=True)