from llama_index.core import SimpleDirectoryReader, Document
import sys
from exception import customexception
from logger import logging
import tempfile
import os

def load_data(file_object):
    """
    Load a PDF or TXT document from a file object.
    Parameters:
    - file_object: A file-like object (e.g., from st.file_uploader)
    Returns:
    - A list containing the loaded document.
    """
    try:
        logging.info("Data loading started...")
        
        # Create a temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Save the uploaded file to the temporary directory
            temp_file_path = os.path.join(temp_dir, file_object.name)
            with open(temp_file_path, "wb") as f:
                f.write(file_object.getvalue())
            
            # Use SimpleDirectoryReader to load the file from the temporary directory
            loader = SimpleDirectoryReader(temp_dir)
            documents = loader.load_data()
        
        logging.info("Data loading completed...")
        return documents
    except Exception as e:
        logging.info("Exception in loading data...")
        raise customexception(e, sys)