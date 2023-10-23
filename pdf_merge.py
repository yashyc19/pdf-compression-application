import os
from PyPDF2 import PdfMerger

def merge_pdfs(file_paths: list, output_path='merged_file.pdf'):
    merger = PdfMerger()
    for path in file_paths:
        merger.append(path)

    with open(output_path, 'wb') as output_file:
        merger.write(output_file)

# Example usage
pdf_files = ['assets/dummy.pdf', 'assets/dummypdf25.pdf', 'assets/dummypdf100.pdf']  # List of paths to PDF files to merge
output_merged_pdf = 'merged_file.pdf'  # Path where the merged PDF will be saved

merge_pdfs(pdf_files, output_merged_pdf)
print(f"PDF files have been merged into {output_merged_pdf}.")
# print path of the merged pdf file
print(f"Path of the merged pdf is {os.path.abspath(output_merged_pdf)}")
# print the size of the merged pdf in mb/ kb/ gb
print(f"Size of the merged pdf is {os.path.getsize(output_merged_pdf)/(1024*1024)} MB")