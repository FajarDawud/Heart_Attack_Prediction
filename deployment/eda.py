import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image
import pred


def run():
    st.title("Aplikasi Prediksi Serangan Jantung")
    image = Image.open('heart.jpeg')
    st.image(image, caption='Heart Attack')

    if "page" not in st.session_state:
        st.session_state["page"] = "EDA"
    
    st.sidebar.title("Menu")
    
    def change_page():
        st.session_state["page"] = st.session_state["nav"]
    
    st.sidebar.radio(
        "Pilih Halaman:",
        ["EDA", "Prediksi"],
        index=["EDA", "Prediksi"].index(st.session_state["page"]),
        key="nav",
        on_change=change_page
    )
    
    if st.session_state["page"] == "EDA":
        show_eda()
    else:
        pred.run()

# Fungsi untuk EDA
def show_eda():
    
    # Load dataset
    try:
        data = pd.read_csv("dataset.csv")
    except Exception as e:
        st.error("Gagal memuat dataset. Pastikan file tersedia.")
        return
    
    # Menampilkan beberapa data awal
    st.subheader("Tampilan Data")
    st.dataframe(data.head())
    
    # Menampilkan ringkasan statistik
    st.subheader("Ringkasan Statistik")
    st.write(data.describe())
    
    # Menampilkan distribusi data
    st.subheader("Distribusi Kolom Numerik")
    numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns
    selected_column = st.selectbox("Pilih Kolom:", numeric_columns)
    
    fig, ax = plt.subplots()
    sns.histplot(data[selected_column], kde=True, ax=ax)
    st.pyplot(fig)
    
    # Menampilkan korelasi

    # Tombol untuk pindah ke halaman prediksi
    if st.button("Go To Predict !"):
        st.session_state["page"] = "Prediksi"
        st.rerun()

# Fungsi-fungsi lainnya (Home dan Prediksi)
def show_home():
    st.title("Halaman Home")
    st.write("Selamat datang di aplikasi analisis data kesehatan!")
    
    if st.button("Go To EDA !"):
        st.session_state["page"] = "EDA"
        st.rerun()
if __name__ == "__main__":
    run()