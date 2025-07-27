import spacy
import os

# Load spaCy's large English NLP model
nlp = spacy.load("en_core_web_sm")

folder = "data/raw_reports"
for filename in os.listdir(folder):
    if filename.endswith(".pdf.txt"):  # These should've been saved as filename.pdf.txt earlier
        filepath = os.path.join(folder, filename)
        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()

        print(f"\n--- Entities found in: {filename} ---\n")
        doc = nlp(text)

        for ent in doc.ents:
            print(f"{ent.text} ({ent.label_})")
