from pypdf import PdfReader, PdfWriter

def merge_pdfs(input_files, output_file):
    """
    Merges multiple PDF files into a single PDF file.

    :param input_files: List of file paths of input PDF files
    :param output_file: File path where the merged PDF will be saved
    """

    # Create a PdfWriter object to build the merged PDF
    writer = PdfWriter()

    # Loop through each input PDF file
    for pdf in input_files:

        # Open the current PDF for reading
        reader = PdfReader(pdf)

        # Add every page from the current PDF to the writer
        for page in reader.pages:
            writer.add_page(page)

    # Write all collected pages into the output PDF file
    with open(output_file, "wb") as f:
        writer.write(f)
