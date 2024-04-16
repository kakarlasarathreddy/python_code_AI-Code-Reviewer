from openai import OpenAI
import streamlit as st
import json

f = open(r"C:\Users\HOME\OneDrive\Documents\openai_key.text")
openai_api_key = f.read()
client = OpenAI(api_key = openai_api_key)

#########################################
st.title("🔍PYTHON CODE DEBUGGER")
st.subheader("📣Review your code here.")

###########################################

prompt = st.text_area("📝Enter your python code")

if st.button("💡Generate") == True:
        st.balloons()
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
            {"role": "system", "content": """You are a friendly AI Assistant of python code debugger .
            you will take a python code as an user input. Your job role is to explain the bugs and fix the bug.
            and generate the correct code in output. you will generate output in JSON file.
            your output sample is given below:
            {"Bugs": "errors of code" , "Fixed_code": "correct code"}"""},
            {"role": "user", "content": f"explain the Bugs and Fixed_code: {prompt}"}
            ],
            temperature = 0.5
        )
 
        review = (response.choices[0].message.content)

        st.write(review)
