import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title = "Checking Health Issues",layout = "wide")

working_dir = os.path.dirname(os.path.abspath(__file__))


#loading of the saved models
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
Heart_Disease_model = pickle.load(open('heart_model.sav','rb'))


#sidebar
with st.sidebar:
	selected = option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Heart Disease Prediction'],menu_icon = 'hospital-fill',icons = ['activity','heart'],default_index = 0)

if selected == 'Diabetes Prediction':
	st.title('Diabetes Prediction')
	col1,col2,col3 = st.columns(3)
	glucose = col1.slider('Glucose Label',0,600,120)
	bp = col2.slider('Blood Pressure Value',0,200,120)
	SKV = col3.slider('Skin Thickness Value',0,100,12)
	Insulin = col1.slider('Insulin Label',0,500,30)
	BMI = col2.slider('BMI Value',0.0,70.0,25.0)
	DPF = col3.slider('Diabetes Pedigree Function Value',0.0,2.5,0.5)
	Age = col1.slider('Age of the person',0,100,25)
	
	if st.button('Diabetes Test Result'):
		user_input = [glucose,bp,SKV,Insulin,BMI,DPF,Age]
		diab_pred = diabetes_model.predict([user_input])
		diab_diagnosis = 'The person is diabetic.' if diab_pred[0] == 1 else 'The person is not diabetic.'
		st.success(diab_diagnosis)


if selected == 'Heart Disease Prediction':
	st.title('Heart Disease Prediction')
	col1,col2,col3 = st.columns(3)
	age = col1.slider('Patient Age',0,77,52)
	cp = col2.slider('Chest Pain type',0,3,0)
	trestbps = col3.slider('Resting blood pressure',0,200,125)
	chol = col1.slider('Serum cholesterol',0,564,212)
	fbs = col2.slider('Fasting blood sugar',0,1,0)
	restecg = col3.slider('Resting electrocardiographic results',0,2,1)
	thalach = col1.slider('Maximum heart rate achieved',0,202,168)
	exang = col2.slider('Exercise-induced angina',0,1,0)
	oldpeak = col3.slider('ST depression induced by exercise relative to rest',0.0,6.2,1.0)
	slope = col1.slider('Slope of the peak exercise ST segment',0,2,2)
	ca = col2.slider('Number of major vessels colored by fluoroscopy',0,4,2)
	thal = col3.slider('Thalassemia (blood disorder test result)',0,3,3)
	gender = col1.selectbox("Select Gender:", options=["Male", "Female"])
	if (gender == "Male"): 
		sex = 1
	else:
		sex = 0
	st.write("You selected:", gender)

	if st.button('Heart Disease Test Result'):
		user_input = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
		heart_pred = Heart_Disease_model.predict([user_input])
		if heart_pred[0] == 1: 
			result = 'The person has Heart Disease.'
		elif heart_pred[0] == 0:
			result = 'The person has no Heart Diseases.'
		else:
			result = '__'
		st.success(result)








