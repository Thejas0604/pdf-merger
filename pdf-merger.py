from PyPDF2 import PdfMerger
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, "files")

merger = PdfMerger()

for pdf in os.listdir(path):
    if pdf.endswith(".pdf"):
        merger.append(os.path.join(path, pdf))

merger.write("merged-pdf.pdf")
merger.close()