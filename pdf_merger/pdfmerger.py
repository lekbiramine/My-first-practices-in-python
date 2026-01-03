import PyPDF2
import os

merger = PyPDF2.PdfMerger()

# Loop through all PDF files in the current directory
for file in os.listdir(os.curdir):
    if file.endswith(".pdf") and file != "EasyPharmacy+LaMedication.pdf":
        merger.append(file)

# Write the merged PDF once, after all files have been appended
with open("EasyPharmacy+LaMedication.pdf", "wb") as output_file:
    merger.write(output_file)

merger.close()
