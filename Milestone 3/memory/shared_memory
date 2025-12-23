from langchain.memory import VectorStoreRetrieverMemory
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def create_shared_memory():
    # Local embeddings (NO API calls)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_texts(
        ["Initial shared memory"], embeddings
    )

    return VectorStoreRetrieverMemory(
        retriever=vectorstore.as_retriever()
    )
