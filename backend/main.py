from fastapi import FastAPI

app = FastAPI(title="PDFWorks Backend")

@app.get("/")
def root():
    return {"message": "Backend is running"}