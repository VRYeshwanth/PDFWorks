from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import shutil
import os
import uuid
from pdf_utils.merger import merge_pdfs

router = APIRouter()

@router.post("/merge")
async def merge(files: list[UploadFile] = File(...)):
    """
    Receives multiple PDF files, merges them into a single PDF,
    and returns the merged file to the user.
    """

    # Ensure at least two PDFs are uploaded
    if len(files) < 2:
        raise HTTPException(400, "Upload atleast 2 PDF Files !!")

    # Create a temporary folder to store uploaded and output files
    os.makedirs("temp", exist_ok=True)

    # List to keep track of saved input PDF file paths
    input_files = []

    # Generate a unique output file name to avoid collisions
    output_file = f"temp/merged_{uuid.uuid4()}.pdf"

    try:
        # Loop through each uploaded file
        for file in files:

            # Validate that the uploaded file is a PDF
            if file.content_type != "application/pdf":
                raise HTTPException(400, "Only PDF Files allowed !!")

            # Decide where to save the uploaded file
            file_path = f"temp/{file.filename}"

            # Write uploaded file data (stream) into a real PDF file
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            # Store the saved file path for merging and cleanup
            input_files.append(file_path)

        # Call the PDF merge function with input PDFs and output path
        merge_pdfs(input_files, output_file)

        # Send the merged PDF back to the user
        return FileResponse(
            output_file,
            media_type="application/pdf",
            filename="merged.pdf"
        )

    finally:
        # Cleanup: delete all temporary input PDF files
        # This runs even if an error occurs
        for file in input_files:
            if os.path.exists(file):
                os.remove(file)
