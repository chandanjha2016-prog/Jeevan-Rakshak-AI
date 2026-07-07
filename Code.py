
import streamlit as st
from transformers import pipeline
import torch

st.set_page_config(page_title="Jeevan Rakshak AI", layout="wide")
st.title("🛡️ Jeevan Rakshak AI - Powered by LLaMA 3.3 70B")
st.write("Mission: Insan, Janwar, Paudha - Sabki Raksha")

@st.cache_resource
def load_llama():
    return pipeline(
        "text-generation",
        model="meta-llama/Llama-3.3-70B-Instruct",
        torch_dtype=torch.bfloat16,
        device_map="auto"
    )

llm = load_llama()

tab1, tab2, tab3 = st.tabs(["🧍 Insan", "🐶 Janwar", "🌱 Paudha"])

with tab1:
    human_input = st.text_input("Insan ko kya takleef hai?")
    if st.button("Raksha Karo", key="h"):
        prompt = f"Tum doctor + safety expert ho. Hindi me 3 line me madad do: {human_input}"
        res = llm(prompt, max_new_tokens=150)
        st.success(res[0]['generated_text'])

with tab2:
    animal_input = st.text_input("Janwar ko kya hua?")
    if st.button("Raksha Karo", key="a"):
        prompt = f"Tum vet doctor ho. Hindi me madad + NGO no do: {animal_input}"
        res = llm(prompt, max_new_tokens=150)
        st.success(res[0]['generated_text'])

with tab3:
    plant_input = st.text_input("Paudhe ko kya problem hai?")
    if st.button("Raksha Karo", key="p"):
        prompt = f"Tum krishi expert ho. Hindi me upay batao: {plant_input}"
        res = llm(prompt, max_new_tokens=150)
        st.success(res[0]['generated_text'])
