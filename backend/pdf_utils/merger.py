from pypdf import PdfReader, PdfWriter

def merge_pdfs(input_files, output_file):
    writer = PdfWriter()

    for pdf in input_files:
        reader = PdfReader(pdf)
        for page in reader.pages:
            writer.add_page(page)
    
    with open(output_file, "wb") as f:
        writer.write(f);