from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import shutil
import os
import uuid
from pdf_utils.merger import merge_pdfs

router = APIRouter()

@router.post("/merge")
async def merge(files: list[UploadFile] = File(...)):
    if(len(files) < 2):
        raise HTTPException(400, "Upload atleast 2 PDF Files !!")
    
    os.makedirs("temp", exist_ok=True)

    input_files = []
    output_file = f"temp/merged_{uuid.uuid4()}.pdf"

    try:
        for file in files:
            if(file.content_type != "application/pdf"):
                raise HTTPException(400, "Only PDF Files allowed !!")
            
            file_path = f"temp/{file.filename}"

            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            
            input_files.append(file_path)

        merge_pdfs(input_files, output_file)

        return FileResponse(output_file, media_type="application/pdf", filename="merged.pdf")
    
    finally:
        for file in input_files:
            if os.path.exists(file):
                os.remove(file)