from langchain_community.document_loaders import TextLoader

def load_txt(file):
    loader = TextLoader(file)
    return loader.load()