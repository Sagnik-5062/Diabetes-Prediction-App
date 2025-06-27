import pickle
import streamlit as st
import numpy as np
import pandas as pd

#loading the diabetes model
with open("Diabetes_Model.sav","rb") as f:
    model_data=pickle.load(f)
    model = model_data['model']
    scaler = model_data['scaler']

st.set_page_config(page_title="Diabetes Prediction App",
                   layout="wide",
                   page_icon="🧑‍⚕️")
#Prediction function
def diabetes_prediction(input_data):
    feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    input_df = pd.DataFrame([input_data_reshaped[0]], columns=feature_names)
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)
    # input_scaled = scaler.transform(input_data_reshaped)
    # prediction = model.predict(input_scaled)

    # if prediction[0] == 0:
    #     return 'The person is Not Diabetic'
    # else:
    #     return 'The person is Diabetic'
    return prediction[0]
#Risk Level
# def Probability(input_data):
#     probability = model.predict_proba(input_data)[0][1]  # Value between 0 and 1
#     if probability < 0.3:
#         risk_level = "Low"
#         color = "🟢"
#     elif 0.3 <= probability < 0.7:
#         risk_level = "Medium"
#         color = "🟠"
#     else:
#         risk_level = "High"
#         color = "🔴"
#     st.markdown(f"Risk Level: {color} **{risk_level}**")
#     st.markdown(f"Probability of having diabetes: **{probability:.2f}**")
#main app
def main():
    st.title("🧑‍⚕️ Diabetes Prediction App 🧑‍⚕️")

    # input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness Value(mm)')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI Value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')

    with col2:
        Age = st.text_input('Age')

    # diagnosis=""
    if st.button('Diabetes Test Result'):
        try:
            user_input = [float(Pregnancies), float(Glucose), float(BloodPressure),
                          float(SkinThickness), float(Insulin), float(BMI),
                          float(DiabetesPedigreeFunction), float(Age)]
            diagnosis = diabetes_prediction(user_input)
            print(diagnosis)
            # print(diagnosis)
            if diagnosis==0:
                st.success("The Person is Not Diabetic")
            elif diagnosis==1:
                st.error("The Person is Diabetic")
            else:
                st.write("Can't Infer Anything From The Given Data")
            
        except ValueError:
            st.write('Please enter valid numeric values in all fields.')

    
    





if __name__=="__main__":
    main()

