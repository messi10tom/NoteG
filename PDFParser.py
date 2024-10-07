from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

PDFDIR = Path('Data') / 'pdfs'


def pdfparser(dir: Path) -> dict:

    parser = {}

    for pdf in dir.glob('*.pdf'):
        pdf_loader = PyPDFLoader(
            file_path = pdf,
            extract_images = True
        )
        parser[pdf.name] = pdf_loader

    return parser

parser = pdfparser(PDFDIR)
sample_loader = next(iter(parser.values()))

docs = []
docs_lazy = sample_loader.lazy_load()

for doc in docs_lazy:
    docs.append(doc)
    
print(docs[0].page_content[:100])
print(docs[0].metadata)