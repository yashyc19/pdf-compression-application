from pdf_compressor import compress

input_file_path = "samplepdf100.pdf"
output_file_path = f"compressed_{input_file_path}"

compress(input_file_path, output_file_path, power=4)