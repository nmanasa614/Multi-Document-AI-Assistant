from langchain_community.document_loaders.csv_loader import CSVLoader

def load_csv(file):
    loader = CSVLoader(file)
    return loader.load()