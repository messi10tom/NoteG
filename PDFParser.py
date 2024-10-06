from PyPDF2 import PdfReader

class PDFparser:
    """
    returns a collection of text from a PDF file
    
    """

    def __init__(self, filename=None):
        if filename:
             self.filename = filename if type(filename) == list  else [filename]
        else: 
            self.filename = []
        self.pages = None
        self.text = None

    def parse(self, filename=None):
        if self.filename:
            reader = PdfReader(self.filename)

        if filename:
            self.filename.append(filename)
            
            reader = PdfReader(filename)
            self.pages = len(reader.pages)
            self.text[filename] = {ix: page.extract_text() for ix, page in enumerate(reader.pages)}
        

    def sample(self, page=1, lines=100):
        print(self.filename[0])
        print(self.text[self.filename[0]][page][:lines])

    def get_num_of_pages(self):
        return len(self.text.split())

    def get_num_of_chars(self):
        return len(self.text)

    def get_num_of_lines(self):
        return self.text.count('\n')

    def get_num_of_paragraphs(self):
        return self.text.count('\n\n')

    def get_num_of_sentences(self):
        return self.text.count('.') + self.text.count('?') + self.text.count('!')