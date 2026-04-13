import streamlit as st 
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
from PIL import Image

st.set_page_config('DEFECT AI',page_icon='🤖',layout='wide')
st.title('AI POWERED DEFECT ANALYZER 🤖🧠🇦🇮👾')
st.header(':blue[Prototype of automated structutal defect analyzer using AI]🎯')
st.subheader(''':red[AI powered structural defect analysis using Streamlit that allows users to upload the image of any structual defects and to get suggestions and recommendations for repair and rebuilt]🚀''')

with st.expander('➤ About the app:'):
    st.markdown(f'''This app helps to detect the defects like cracks , misallignment etc and provide
                - **Defect Detection**
                - **Recommendation**
                - **Suggestions for improvements** ''')
    
import os 

key = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=key)

input_image = st.file_uploader('Upload your file here📄',type=['png','jpeg','jpg'])
img =''
if input_image:
    img = Image.open(input_image).convert('RGB')
    st.image(img, caption='Uploaded Successfully')

prompt = f'''You are an quality engineer and civil engineer. you need to analyze the input image and provide 
necessary details for the below given questions in bullet points (max 3 points for each questions)

1.Identify the type of structural defect in the given image like cracks,bends,etc
2.Identify the factors that may have caused the defect
3.Calculate the lifespan of the structure if the defect is unattended
4.Provide necessary precautionary measures to prevent the defects from occuring
5.Identify the severity of the crack(low,medium,intense)
6.Estimate the cost for remedy
7.Provide different ways to fix the crack
8.Estimate the time required to fix the crack
9.Calculate the probability that the structure has similar defects in other places 
10.What is the probability of damages caused by the defects detected'''

model = genai.GenerativeModel('gemini-2.5-flash-lite')
def generate_result(prompt,image):
    result = model.generate_content(f'''Using the given{prompt} and given image {img}
                                    analyze the image and give the results as per the prompt''')
    return result.text

submit = st.button('Analyze the image 🎯')
if submit:
    with st.spinner('Results loading.....🚀'):
        response = generate_result(prompt,img)
        
        st.markdown('## :green[Results]')
        st.write(response)