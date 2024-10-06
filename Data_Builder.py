from PDFParser import PDFparser
from pathlib import Path

PDFDIR = Path('Data') / 'pdfs'
parser = PDFparser()

for pdf in PDFDIR.glob('*.pdf'):
    parser.parse(pdf)

# parser.sample()


