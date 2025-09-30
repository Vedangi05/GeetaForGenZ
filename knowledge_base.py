import os
from PyPDF2 import PdfReader

class KnowledgeBase:
    def __init__(self, pdf_folder="gita_pdfs"):
        self.pdf_folder = pdf_folder
        self.texts = self._load_pdfs()

    def _load_pdfs(self):
        """Load all PDFs from the folder and extract text"""
        texts = []
        for filename in os.listdir(self.pdf_folder):
            if filename.endswith(".pdf"):
                path = os.path.join(self.pdf_folder, filename)
                reader = PdfReader(path)
                content = ""
                for page in reader.pages:
                    content += page.extract_text() + "\n"
                texts.append(content)
        return texts

    def get_context(self, query: str, max_chars=2000):
        """
        Return the most relevant PDF text snippet for a given query.
        For simplicity, we return the first 2000 chars here.
        """
        # Can be improved with semantic search later
        return "\n".join(self.texts)[:max_chars]
