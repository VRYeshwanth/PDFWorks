from fastapi import FastAPI
from routes.merge import router as merge_router

app = FastAPI(title="PDFWorks Backend")

app.include_router(merge_router)

@app.get("/")
def root():
    return {"message": "Backend is running"}