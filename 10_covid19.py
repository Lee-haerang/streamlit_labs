# 라이브러리 불러오기
import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 페이지 기본 설정 --------------------
st.set_page_config(
    page_title='코로나19 한국 대시보드',
    page_icon='🦠'
    layout='wide' # 전체 화면 너비 사용
)
st.title('KR 코로나19 한국 감염자 대시보드')

# 2. 파일 업로더 ----------------------------------
# 파일이 업로드 되지 않았다면 None 반환
uploaded_confirmed = st.file_uploader('확진자 csv파일 업로드', type=['csv'])
uploaded_deaths = st.file_uploader('사망자 csv파일 업로드', type=['csv'])
uploaded_recovered = st.file_uploader('회복자 csv파일 업로드', type=['csv'])

# 3. 세 파일이 모두 업로드 되었을 때만 분석 실행 -------------
#     업로드 전 : 파일 객체가 None -> False -> 분석 실행 안함 -> 다시 업로드 유도
#     업로드 후 : 파일 객체가 있다 -> True -> 분석 실행 가능
if uploaded_confirmed and uploaded_deaths and uploaded_recovered:

    # 4. 데이터 프레임으로 읽기 ------------------------------------------
    df_confirmed = pd.read_csv(uploaded_confirmed)
    df_deaths = pd.read_csv(uploaded_deaths)
    df_recovered = pd.read_csv(uploaded_recovered)

# 파일 미업로드 시 상태 안내 메시지------------------------------
else: # st.info() : 파란색 안내 박스로 사용자에게 보여준다!
    st.info('3개의 csv파일(확진자, 사망자, 회복자)을 모두 업로드 해주세요!')