from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

BASE = Path(__file__).parent

loader = DirectoryLoader(
    path=str(BASE / 'books'),
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)