from pathlib import Path
from langchain_community.document_loaders import CSVLoader

BASE = Path(__file__).parent

loader = CSVLoader(file_path=BASE / 'Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))
print(docs[1])