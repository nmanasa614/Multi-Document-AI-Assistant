from langchain_community.document_loaders import Docx2txtLoader

def load_docx(file):
    loader = Docx2txtLoader(file)
    return loader.load()