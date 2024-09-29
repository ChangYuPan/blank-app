import streamlit as st
import streamlit.components.v1 as components
import base64

# 定義一個函數來將本地圖片轉換成 base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# 設定頁面標題
st.title("網頁測試測試")

# 更新後的 CSS 設定
st.markdown("""
<style>
/* 統一的圖片樣式 */
.responsive-img {
    width: 100%;
    border-radius: 8px;
    object-fit: cover;  /* 確保圖片根據容器大小調整而不會變形 */
}

/* 統一的容器樣式 */
.responsive-container {
    margin: 20px 0;
    text-align: center;
    font-size: calc(2vw + 16px);
    white-space: nowrap;
    overflow: hidden;
}
</style>
""", unsafe_allow_html=True)

# 第一部分
img1 = get_base64_of_image('images/這裡是什麼鬼地方.jpg')
st.markdown(f"""
<div class="section responsive-container" style="position: relative;">
    <img class="responsive-img" src="data:image/jpg;base64,{img1}" alt="背景圖片" style="filter: grayscale(75%);">
    <div style="position: absolute; top: 10%; left: 50%; transform: translate(-50%, -50%); color: white; font-weight: bold; z-index: 10;">
        這裡是 CY 的迷因基地
    </div>
    <div style="position: absolute; top: 16%; left: 50%; transform: translate(-50%, -50%); width: 90%; z-index: 10;">
        <div style="border-top: 1px solid white; margin: 10px 0;"></div>
    </div>
    <div style="position: absolute; top: 17%; left: 5%; color: white; z-index: 10; font-size: calc(2vw + 6px);">CYPan & CYPan</div>
    <div style="position: absolute; top: 17%; right: 5%; color: white; text-align: right; z-index: 10; font-size: calc(2vw + 6px);">2024 Oct. 20th</div>
    <p style="position: absolute; bottom: 10%; right: 5%; color: white; text-align: right; z-index: 10; font-size: calc(2vw + 8px);">
        歡迎來到 CY 的迷因基地<br>
        這裡可能是要寫點什麼<br>
        但可能也不會太多?!
    </p>
</div>
""", unsafe_allow_html=True)

# 第二部分（上下排列）
img2 = get_base64_of_image('images/真的好想好想要.jpg')
st.markdown(f"""
<div class="section responsive-container">
    <img class="responsive-img" src="data:image/jpg;base64,{img2}" alt="上方圖片">
</div>
<div class="section responsive-container">
    <p style="font-size: calc(2vw + 6px);>
        這邊是要給你各位的一段話<br>
        能不能針對每個人給還不知道<br>
        反正會放這邊
    </p>
</div>
""", unsafe_allow_html=True)

# 第三部分（自動輪播圖片）
# 內嵌 HTML 和 Bootstrap 的 Carousel
def get_html_repeat_imgs(imgs_path):
    template = """
    <div class="carousel-item {}">
        <img src="data:image/jpeg;base64,{}" class="blur-background">
        <img src="data:image/jpeg;base64,{}" class="foreground-image">
    </div>
    """
    html = ''
    for i, img_path in enumerate(imgs_path):
        active = 'active' if i == 0 else ''
        html += template.format(active, get_base64_of_image(img_path), get_base64_of_image(img_path))
    return html

imgs_path = [
    'images/今天很嗆是吧.jpg',
    'images/我又沒有唸書.jpg',
    'images/這裡是什麼鬼地方.jpg',
]
html_repeat_imgs = get_html_repeat_imgs(imgs_path)

# Carousel 的 HTML 代碼
carousel_code = f"""
<style>
    .carousel-item {{
        position: relative;  /* 使子元素可以絕對定位 */
        height: 100vh;
        overflow: hidden;  /* 隱藏溢出的內容 */
    }}
    .blur-background {{
        position: absolute;  /* 絕對定位 */
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        z-index: -1;  /* 確保在圖片下方 */
        filter: blur(10px);  /* 模糊效果 */
        width: 100%;  /* 調整為 100% 寬度 */
        height: 100%;  /* 調整為 100% 高度 */
        object-fit: cover;  /* 使模糊背景圖片填滿 */
    }}
    .foreground-image {{
        position: relative;  /* 使其層級高於背景 */
        z-index: 1;  /* 確保在背景之上 */
        width: 100%;
        height: 100%;
        object-fit: contain;  /* 使上層圖片保持比例並顯示完整 */
        display: block;  /* 確保圖片為塊狀顯示 */
        margin: auto;  /* 使圖片水平置中 */
    }}
</style>

<div id="carouselExample" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-inner">
    {html_repeat_imgs}
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
"""

# 顯示輪播元件
components.html(carousel_code, height=300)