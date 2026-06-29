def retrieve(db, question):

    retriever = db.as_retriever()

    docs = retriever.get_relevant_documents(question)

    return docs