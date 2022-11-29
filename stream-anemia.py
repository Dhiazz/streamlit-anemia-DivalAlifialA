import pickle
import streamlit as st

# membaca model
anemia_model =  pickle.load(open('anemia_model.sav', 'rb'))

#Judul Web
st.title('Data Mining Prediksi Penyakit Anemia')

Gender = st.text_input('Jenis Kelamin')

Hemoglobin = st.text_input('Masukan Jumlah protein dalam sel darah merah')

MCH = st.text_input('Masukan jumlah rata-rata di setiap sel darah merah')

MCHC = st.text_input('masukan ukuran konsentrasi rata-rata hemoglobin')

MCV = st.text_input('masukan rata-rata sel darah merah Anda')

# code untuk kelompok jenis bunga
anemia_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi'):
    ane_prediction = anemia_model.predict([[Gender, Hemoglobin, MCH, MCHC, MCV]])
    
    if(ane_prediction[0] == 1):
        anemia_diagnosis = 'Pasien mengidap anemia'
    else :
        ane_diagnosis = 'Pasien tidak mengidap anemia'

    st.success(anemia_diagnosis)