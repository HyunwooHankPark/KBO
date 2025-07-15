import streamlit as st
import pandas as pd
import plotly.express as px

# 파일 업로드
st.title("⚾ KBO 팀별 투수 기록 비교 분석 대시보드")
uploaded_file = st.file_uploader("📂 KBO 피칭 데이터 파일 업로드 (xlsx)", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    # 팀, 연도, 지표 선택
    years = st.multiselect("연도를 선택하세요", sorted(df["year"].unique()), default=sorted(df["year"].unique()))
    teams = st.multiselect("팀을 선택하세요", sorted(df["team"].unique()), default=sorted(df["team"].unique()))
    metric = st.selectbox("비교할 피칭 지표 선택", ["ERA", "WHIP", "strikeouts_9", "walks_9", "homeruns_9"])

    # 필터링
    filtered = df[(df["year"].isin(years)) & (df["team"].isin(teams))]

    # 그래프 출력
    st.subheader(f"{metric} - 연도별 팀 비교")
    fig = px.line(filtered, x="year", y=metric, color="team", markers=True)
    st.plotly_chart(fig, use_container_width=True)

    # 표 출력
    st.subheader("📊 데이터 요약")
    st.dataframe(filtered[["year", "team", metric, "wins", "losses", "win_loss_percentage"]].sort_values(by=["year", "team"]))
