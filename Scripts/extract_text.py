import pdfplumber
import os

folder = "data/raw_reports"
for file in os.listdir(folder):
    if file.endswith('.pdf'):
        with pdfplumber.open(os.path.join(folder, file)) as pdf:
            text = ''
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            print(f"\n--- {file} ---\n")
            print(text[:500])
