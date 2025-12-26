from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.merge import router as merge_router

app = FastAPI(title="PDFWorks Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(merge_router)

@app.get("/")
def root():
    return {"message": "Backend is running"}