import streamlit as st
import pandas as pd
import pickle
from PIL import Image


def run():
    with open('best_dt.pkl', 'rb') as model_file:
            best_dt = pickle.load(model_file)
    
    st.title("Halaman Prediksi")
    st.write("Silakan masukkan data untuk melakukan prediksi.")
    
    with st.form(key='form_patient'):
        st.write('## **---IDENTITAS---**')
        name = st.text_input("Name", value="--nama-anda--")
        age = st.number_input("🎂Age", min_value=0, max_value=100, value=10, step=1)
        gender = st.radio("🚻Gender", ('Male', 'Female'))

        st.markdown('---')
        st.write('# Anamnesis / Riwayat Pasien')
        cholesterol = st.number_input("🩸Cholesterol", min_value=50, max_value=299, value=100)
        alcohol_consumption = st.radio("🍻Pengonsumsi Alkohol", (1, 2, 3, 4))
        diet = st.radio("🥗Diet", ('Unhealthy', 'Moderate', 'Healthy'))
        chestpain_type = st.radio("💔Tipe Sakit Dada", ('Non-anginal', 'Atypical', 'Asymptomatic', 'Typical'))
        st.write('Typical = Sesak')
        st.write('Atypical = Nyeri punggung di bagian Rahang/Punggung')
        st.write('Non-Anginal = Nyeri seperti ditusuk jarum')
        st.write('Asymptomatic = Sakit jantung tanpa nyeri')
        stresslevel = st.radio("😟Tingkat Stress", (1,2,3,4,5,6,7,8))
        medication = st.radio("💊Sedang Menjalani Pengobatan", ('Yes', 'No'))
        maxheartrate = st.number_input("💓Detak Jantung Maksimal", min_value=90, max_value=250, value=90)
        st.markdown('---')
        st.write('***Pilih 1 = Iya, Pilih 0 = Tidak***')
        smoker = st.radio("🚬Perokok", ('1', '0'))
        diabetes = st.radio("🩺Diabetes", ('1', '0'))
        hypertension = st.radio("⚠️Hipertensi", ('1', '0'))
        family_history = st.radio("👨‍👩‍👧‍👦Riwayat Keluarga", ('1', '0'))
        previousheart = st.radio("💔Riwayat Sakit Jantung", (1, 0))
        strokehistory = st.radio("⚡Riwayat Stroke", (1, 0))
        st.markdown('---')
        st.write('## ***Pemeriksaan Fisik***')
        bmi = st.number_input("⚖️BMI", min_value=15.0, max_value=50.0, value=50.0)
        blood_pressure = st.number_input("💉Tekanan Darah", min_value=70, max_value=220, value=70)
        heart_rate = st.number_input("❤️Detak Jantung", min_value=50, max_value=299, value=100)
        
        st.write('## ***Pemeriksaan Penunjang***')
        ecgresults = st.radio("📉ECG Results", ('ST-T abnormality', 'LV hypertrophy', 'Normal'))
        stdpression = st.slider("📊ST Depression", 0.0, 5.0, 0.0)
        exerciseinduced = st.radio("🏋️‍♂️Nyeri Dada", ('🏋️‍♂️Yes', 'No'))
        numberofvessels = st.radio("🩸Jumlah Pembuluh Darah Utama", (0, 1, 2, 3))
        
        submitted = st.form_submit_button("Predict !")
    
    if submitted:
        new_patient = pd.DataFrame([{
            'Name': name,
            'Age': age,
            'Gender': gender,
            'Cholesterol': cholesterol,
            'BloodPressure': blood_pressure,
            'HeartRate': heart_rate,
            'BMI': bmi,
            'Smoker': smoker,
            'Diabetes': diabetes,
            'Hypertension': hypertension,
            'FamilyHistory': family_history,
            'AlcoholConsumption': alcohol_consumption,
            'Diet': diet,
            'StressLevel': stresslevel,
            'Medication': medication,
            'ChestPainType': chestpain_type,
            'ECGResults': ecgresults,
            'MaxHeartRate': maxheartrate,
            'ST_Depression': stdpression,
            'ExerciseInducedAngina': exerciseinduced,
            'NumberOfMajorVessels': numberofvessels,
            'PreviousHeartAttack': previousheart,
            'StrokeHistory': strokehistory
        }])
        
        st.dataframe(new_patient)
        pred = best_dt.predict(new_patient)
        status = "tidak mengalami serangan jantung" if pred[0] == 0 else "mengalami serangan jantung"
        st.success(f"Pasien bernama {name} terprediksi {status}.")

if __name__ == "__main__":
    run()
