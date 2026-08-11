from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.resume import router as resume_router
from api.routes.scoring import router as scoring_router
from api.routes.shortlisting import router as shortlisting_router
from api.routes.jobs import router as jobs_router
from api.errors import api_error_handler
from api.logger import logger


app = FastAPI(
    title="Zecpath AI ATS API",
    description="API layer for the Zecpath AI recruitment system",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info("Zecpath AI ATS API started")

app.add_exception_handler(
    Exception,
    api_error_handler
)

app.include_router(resume_router)
app.include_router(scoring_router)
app.include_router(shortlisting_router)
app.include_router(jobs_router)


@app.get("/")
def root():
    return {
        "status": "running",
        "message": "Zecpath AI ATS API is running"
    }