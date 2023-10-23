from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_file_path, custom_start, custom_end, fixed_value):
    if custom_start and custom_end:
        msg = split_custom_range(input_file_path, custom_start, custom_end)
        return(msg)
    elif fixed_value:
        msg = split_fixed_value(input_file_path, fixed_value)
        return(msg)
    else:
        return("Invalid parameters provided.")

def split_custom_range(input_file_path, start, end):
    reader = PdfReader(input_file_path)
    writer = PdfWriter()

    for page_num in range(start-1, end):
        writer.add_page(reader.pages[page_num])

    input_file_path = input_file_path.split(".")[0]
    with open(f"{input_file_path}_{start}_to_{end}.pdf", 'wb') as output_pdf:
        writer.write(output_pdf)

    return(f"PDF has been split from page {start} to {end}.")

def split_fixed_value(input_file_path, fixed_value):
    reader = PdfReader(input_file_path)

    page_count = len(reader.pages)
    num_splits = page_count // fixed_value

    for i in range(num_splits):
        writer = PdfWriter()
        for j in range(fixed_value):
            writer.add_page(reader.pages[i * fixed_value + j])

        input_file_path = input_file_path.split(".")[0]
        with open(f"{input_file_path}_part_{i + 1}.pdf", 'wb') as output_pdf:
            writer.write(output_pdf)

    return(f"PDF has been split into {num_splits} parts with {fixed_value} pages each.")
