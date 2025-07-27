from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from dotenv import load_dotenv

# Import routers
from app.auth.router import router as auth_router
from app.core.router import router as core_router
from app.services.router import router as services_router
from app.tax_engine.router import router as tax_router
from app.submission.router import router as submission_router
from app.state.router import router as state_router
from app.payment.router import router as payment_router
from app.admin.router import router as admin_router

load_dotenv()

app = FastAPI(
    title="Auto Tax Filing Demo API",
    description="Production-ready tax filing application API",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files
app.mount("/static", StaticFiles(directory="../static"), name="static")

# Health check endpoint for Railway
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "tax-auto-demo"}

# Include routers
app.include_router(auth_router, prefix="/api/auth", tags=["Authentication"])
app.include_router(core_router, prefix="/api/core", tags=["Core"])
app.include_router(services_router, prefix="/api/services", tags=["Services"])
app.include_router(tax_router, prefix="/api/tax", tags=["Tax Engine"])
app.include_router(submission_router, prefix="/api/submission", tags=["Submission"])
app.include_router(state_router, prefix="/api/state", tags=["State"])
app.include_router(payment_router, prefix="/api/payment", tags=["Payment"])
app.include_router(admin_router, prefix="/api/admin", tags=["Admin"])

@app.get("/")
async def root():
    return {"message": "Auto Tax Filing Demo API", "status": "running"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
