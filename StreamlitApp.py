import streamlit as st
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model

def main():
    st.set_page_config("QA with Documents")
    
    st.header("QA with Documents")
    
    uploaded_file = st.file_uploader("Upload your document", type=["pdf", "txt"])
    
    user_question = st.text_input("Ask your question")
    
    if st.button("Submit & Process"):
        if uploaded_file is not None:
            with st.spinner("Processing..."):
                try:
                    document = load_data(uploaded_file)
                    model = load_model()
                    query_engine = download_gemini_embedding(model, document)
                    
                    response = query_engine.query(user_question)
                    
                    st.write(response.response)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please upload a document first.")

if __name__ == "__main__":
    main()