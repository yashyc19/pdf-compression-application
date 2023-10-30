from PyPDF2 import PdfMerger

def merge_pdfs(file_paths: list, output_path='merged_file.pdf'):
    merger = PdfMerger()
    for path in file_paths:
        merger.append(path)

    with open(output_path, 'wb') as output_file:
        merger.write(output_file)

# merge_pdfs(['file1.pdf', 'file2.pdf', 'file3.pdf'], 'output.pdf')
