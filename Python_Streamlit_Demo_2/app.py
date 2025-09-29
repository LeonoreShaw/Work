import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

st.set_page_config(layout="wide")
st.title("激光器功率诊断工具 — Streamlit Demo")

uploaded_file = st.file_uploader("上传 CSV 文件 (包含 time,power,water_temp,spot_cx,spot_cy,spot_sizex,spot_sizey)", type=["csv"])
if uploaded_file is None:
    st.info("请上传CSV文件，或使用示例 sample.csv。")
else:
    df = pd.read_csv(uploaded_file)
    st.subheader("数据预览")
    st.dataframe(df.head())

    required = ["time","power","water_temp","spot_cx","spot_cy","spot_sizex","spot_sizey"]
    if not all(c in df.columns for c in required):
        st.error(f"CSV 必须包含列: {required}")
    else:
        # Convert
        df["time"] = pd.to_datetime(df["time"], errors="coerce")
        df = df.sort_values("time").reset_index(drop=True)
        df[["power","water_temp","spot_cx","spot_cy","spot_sizex","spot_sizey"]] = df[["power","water_temp","spot_cx","spot_cy","spot_sizex","spot_sizey"]].apply(pd.to_numeric, errors="coerce")

        st.subheader("功率趋势")
        fig, ax = plt.subplots(figsize=(8,3))
        ax.plot(df["time"], df["power"], marker="o")
        ax.set_xlabel("time"); ax.set_ylabel("power")
        st.pyplot(fig)

        st.subheader("相关性热图")
        corr = df[["power","water_temp","spot_cx","spot_cy","spot_sizex","spot_sizey"]].corr()
        fig2, ax2 = plt.subplots(figsize=(6,5))
        sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax2)
        st.pyplot(fig2)

        st.subheader("线性回归分析")
        X = df[["water_temp","spot_cx","spot_cy","spot_sizex","spot_sizey"]].fillna(method="ffill").fillna(method="bfill")
        y = df["power"].fillna(method="ffill").fillna(method="bfill")
        model = LinearRegression().fit(X, y)
        coeffs = dict(zip(X.columns, model.coef_))
        st.write(coeffs)
        main = max(coeffs, key=lambda k: abs(coeffs[k]))
        st.success(f"诊断：功率下降主要受 {main} 影响 (coef={coeffs[main]:.3f})")
