import os
import docx #pip install python-docx
import asyncio
from subprocess import Popen, PIPE
from pdfminer.high_level import extract_text #pip install pdfminer

class Mydocuments:
    def __init__(self):
        self.cache = []
        self.search_cache = []
        self.flag = False
        
    def get_cache(self):
        return self.cache
    
    def get_search_cache(self):
        return self.search_cache
    
    def get_flag(self):
        return self.flag
        
    def get_documents(self):
        drive_list = os.popen('wmic logicaldisk get caption').read().rstrip().split()[1:]
        cache = []

        for drive in drive_list:
            result = os.popen('dir /s /b /a-d {0}\*.pdf {0}\*.hwp {0}\*.docx'.format(drive)).read().rstrip().split('\n')
            cache += result
        
        self.cache = cache
        self.flag = True
        
    def search_documents(self, keywords):
        result = []
        
        for c in self.cache:
            name = c.split('\\')[-1]
            for keyword in keywords:
                if keyword.upper() in name.upper():
                    result.append(c)
                    break
        
        self.search_cache = list(set(result))

    def print_docx(self, path):
        fullText = []
        doc = docx.Document(path)
        
        for para in doc.paragraphs:
            if para.text:
                fullText.append(para.text)
        
        return " ".join(fullText).replace('\n', ' ').replace('"', '\'')
        #for text in fullText:
        #   print(text)
           
    def print_pdf(self, path):
        from PyPDF2 import PdfReader
        reader = PdfReader(path)
        pages = reader.pages
        text = ""
        for page in pages:
            sub = page.extract_text()
            text += sub

        return (text.replace('\n', ' ').replace('"', '\''))

    def print_hwp(self, path):
        process = Popen(['hwp5txt', path], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        data = stdout.decode('utf-8')
        
        return data.replace('\n', ' ').replace('"', '\'')
    
doc = Mydocuments()
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write(doc.print_docx('C:\\Users\\norma_rna10\\Downloads\\노르마_IoT Care_기술적 차별성_231107.docx'))