import requests
from io import BytesIO
from docx import Document
import re
class readdoc:
    def __init__(self,link=''):
        self.file_id = re.search(r"/d/([a-zA-Z0-9_-]+)", link).group(1)
        self.doc_link = f"https://drive.google.com/uc?export=download&id={self.file_id}"



    
    def read_with_h2(self):      
        # Download the document content
        self.response = requests.get(self.doc_link)
        self.doc_content = self.response.content

        # Read the Word document
        self.doc = Document(BytesIO(self.doc_content))

        for paragraph in self.doc.paragraphs:
            print("<h2>"+paragraph.text+"</h2>")