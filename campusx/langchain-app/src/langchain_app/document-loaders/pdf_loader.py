from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

BASE = Path(__file__).parent

loader = PyPDFLoader(BASE / 'dl-curriculum.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)