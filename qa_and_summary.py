def query_index(index, question):
    engine = index.as_query_engine()
    return engine.query(question)

def summarize(index):
    engine = index.as_query_engine()
    return engine.query("Summarize the key findings and methods of the paper.")
