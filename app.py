import streamlit as st

st.set_page_config(page_title="Multi Document AI Assistant")

st.title("📄 Multi Document AI Assistant")

uploaded_files = st.file_uploader(
    "Upload Documents",
    type=["pdf","docx","txt","csv"],
    accept_multiple_files=True
)

question = st.text_input("Ask your question")

if uploaded_files:
    st.success(f"{len(uploaded_files)} files uploaded")

if st.button("Ask"):
    st.write("Answer will appear here.")