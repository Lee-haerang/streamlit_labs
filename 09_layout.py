import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

# 1. 메인 페이지 제목
st.title('This is main page')

# 2. 사이드바 (sidebar)
with st.sidebar:
    st.title('This is sidebar')
    side_option = st.multiselect(
        label='your selection is',
        options=['Car', 'Airplane', 'Train', 'Ship', 'Bicycle'],
        placeholder='select transportation'
    )
    st.write(side_option)

# 3. 메인 : 이미지 넣기
img2 = Image.open('./input/image2.jpg')
img3 = Image.open('./input/image3.jpg')

# 4. 이미지 세로 나열
st.header('Lemonade')
st.image(img2, width=300, caption='Image from Unsplash')

st.header('Cocktail')
st.image(img3, width=300, caption='Image from Unsplash')

# 5. 컬럼 레이아웃
col1, col2 = st.columns(2) # 동일한 너비의 2열로 분할
with col1:
    st.header('Lemonade')
    st.image(img2, width=300, caption='Image from Unsplash')

with col2:
    st.header('Cocktail')
    st.image(img3, width=300, caption='Image from Unsplash')

# 6. 탭 레이아웃
tab1, tab2 = st.tabs(['Table', 'Graph'])

# 데이터 준비
df = pd.read_csv('./input/medical_cost.csv')
# region이 northwest 필터링
df = df.query('region == "northwest"')

with tab1:
    st.table(df.head(5))

with tab2:
    fig, ax = plt.subplots()  # fig: 전체 그림의 캔버스(도화지), ax: 그래프가 그려지는 축(axes)
    sns.scatterplot(data=df, x='bmi', y='charges', ax=ax)
    st.pyplot(fig)
